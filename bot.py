import json
from asyncio.log import logger
import telebot
from telebot import types
from telebot_calendar import Calendar, CallbackData, ENGLISH_LANGUAGE
import datetime

token = 'TOKEN'
bot = telebot.TeleBot('TOKEN')
calendar = Calendar(language=ENGLISH_LANGUAGE)
calendar_1 = CallbackData('calendar_1', 'action', 'year', 'month', 'day')
now = datetime.datetime.now()
# a dictionary that stores all tasks
todos = {}

# bot start and button output
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    button1 = types.KeyboardButton('Add task 📝')
    button2 = types.KeyboardButton('Show tasks 📋')
    button3 = types.KeyboardButton('Help 🆘')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    start_message = f"Hello, {message.from_user.first_name}! I'm a bot that will help you not to forget anything.😉" 
    bot.send_message(message.chat.id, start_message, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def hepling(message):
    bot.send_message(message.chat.id, '''
I will help you to add tasks and keep track of them. ⏰
To add a task, click on the "Add task" button.
To view all tasks, click on the "Show tasks" button.
To delete a task, click on the "❌" button next to the task on "Show tasks" menu.
''')

# task deletion function
def delete_task(chat_id, c_date, task):
    if todos.get(chat_id) is not None:
        if todos[chat_id].get(c_date) is not None:
            todos[chat_id][c_date].remove(task)
            if len(todos[chat_id][c_date]) == 0:
                del todos[chat_id][c_date]
            if len(todos[chat_id]) == 0:
                del todos[chat_id]


@bot.message_handler(content_types=['text'])
def call(message):
    if message.text == 'Add task 📝':
        bot.send_message(message.chat.id, 'Choose a date:', reply_markup=calendar.create_calendar(
            name=calendar_1.prefix,
            year=now.year,
            month=now.month)
                         )
    elif message.text == 'Show tasks 📋':
        if not todos.get(message.chat.id):
            bot.send_message(message.chat.id, 'No tasks are set.')
        else:
            for chat_id, dates in todos.items():
                if chat_id == message.chat.id:
                    for date, tasks in dates.items():
                        tasks_text = '\n'.join(f'- {task}' for task in tasks)
                        text = f'Tasks for {date}:\n{tasks_text}'
                        keyboard = types.InlineKeyboardMarkup()
                        for task in tasks:
                            button = types.InlineKeyboardButton(text=f'❌ {task}', callback_data=f'delete:{date}:{task}')
                            keyboard.add(button)
                        bot.send_message(message.chat.id, text, reply_markup=keyboard)
    elif message.text == 'Help 🆘':
        bot.send_message(message.chat.id, '''
I will help you to add tasks and keep track of them. ⏰
To add a task, click on the "Add task" button.
To view all tasks, click on the "Show tasks" button.
To delete a task, click on the "❌" button next to the task on "Show tasks" menu.
''')
    else:
        bot.send_message(message.chat.id, "I don't understand... Press 'Help' in the menu 🙄 ")

# deletes the task and displays a message about the successful deletion of this task.
@bot.callback_query_handler(func=lambda call: call.data.startswith('delete:'))
def delete_callback(call):
    _, date, task = call.data.split(':')
    delete_task(call.message.chat.id, date, task)
    bot.answer_callback_query(call.id, text=f'Task "{task}" on {date} successfully deleted')

# the function is a callback request handler. It is called when you click on the calendar buttons
@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1.prefix))
def callback_inline(call: types.CallbackQuery):
    name, action, year, month, day = call.data.split(calendar_1.sep)
    date = calendar.calendar_query_handler(bot=bot, call=call, name=name, action=action, year=year, month=month,
                                           day=day)
    if action == 'DAY':
        c_date = date.strftime("%d.%m.%Y")
        bot.send_message(chat_id=call.from_user.id, text=f'You chose {c_date}')
        msg = bot.send_message(chat_id=call.from_user.id, text='What to plan: ')
        bot.register_next_step_handler(msg, lambda message: add_task(message, chat_id=call.from_user.id, c_date=c_date))
    elif action == 'CANCEL':
        bot.send_message(chat_id=call.from_user.id, text='Cancelled 🚫')

# the function of adding a new task
def add_task(message, chat_id, c_date):
    add_todo(chat_id, c_date, message)
    text = f'Task successfully added on {c_date} ✅'
    bot.send_message(chat_id=chat_id, text=text)

# the function adds a task to the todos dictionary
def add_todo(chat_id, c_date, message):
    task = message.text
    if todos.get(chat_id) is not None:
        if todos[chat_id].get(c_date) is not None:
            todos[chat_id][c_date].append(task)
        else:
            todos[chat_id][c_date] = [task]
    else:
        todos[chat_id] = {c_date: [task]}


bot.polling(none_stop=True)

def lambda_handler(event, context):
    try:
        # Extract the relevant information from the event
        update = json.loads(event['body'])
        
        # Handle the Telegram bot logic based on the update
        bot.process_new_updates([types.Update.de_json(update)])
        
        # Return a response to the client (if using API Gateway)
        response = {
            "statusCode": 200,
            "body": "OK"
        }
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        response = {
            "statusCode": 500,
            "body": "Internal Server Error"
        }
    
    return response
