import json
import requests
import datetime

TELE_TOKEN='TOKEN'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

# a dictionary that stores all tasks
todos = {}

def start(chat_id):
  start_message = f"Hello! I'm a bot that will help you not to forget anything.⏰\nFor more information, type 'help' in the menu 😉"
  send_message(start_message, chat_id)

def delete_task(chat_id, c_date, task):
  if todos.get(chat_id) is not None:
      if todos[chat_id].get(c_date) is not None:
          todos[chat_id][c_date].remove(task)
          if len(todos[chat_id][c_date]) == 0:
              del todos[chat_id][c_date]
          if len(todos[chat_id]) == 0:
              del todos[chat_id]

def add_task(chat_id, c_date, task):
  add_todo(chat_id, c_date, task)
  send_message("Task successfully added.", chat_id)

def add_todo(chat_id, c_date, task):
  if todos.get(chat_id) is not None:
      if todos[chat_id].get(c_date) is not None:
          todos[chat_id][c_date].append(task)
      else:
          todos[chat_id][c_date] = [task]
  else:
      todos[chat_id] = {c_date: [task]}

def send_message(text, chat_id):
  url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
  requests.post(url)

# a dictionary that stores the state of the conversation
conversation_states = {}

def lambda_handler(event, context):
 try:
  # Extract the relevant information from the event
  update = json.loads(event['body'])
  
  # Handle the Telegram bot logic based on the update
  command = update['message']['text']
  chat_id = update['message']['chat']['id']
  
  if command == '/start':
      start(chat_id)
      conversation_states[chat_id] = 'idle'
  elif command == 'add task':
      # Handle the 'Add task' command
      send_message("Please enter the task details:", chat_id)
      conversation_states[chat_id] = 'waiting for task details'
  elif command == 'show tasks':
      # Handle the 'Show tasks' command
      tasks = todos.get(chat_id, {}).get(datetime.date.today(), [])
      if tasks:
          send_message("Your tasks for today are: " + ', '.join(tasks), chat_id)
      else:
          send_message("No tasks available.", chat_id)
      conversation_states[chat_id] = 'idle'
  elif command == 'help':
      # Handle the 'Help' command
      send_message("You can add a task by sending 'add task'. You can show your tasks by sending 'show tasks'. You can delete a task by sending 'delete task'.", chat_id)
      conversation_states[chat_id] = 'idle'
  elif command == 'delete task':
      # Handle the 'Delete task' command
      send_message("Please enter the task details to delete:", chat_id)
      conversation_states[chat_id] = 'waiting for delete task details'
  else:
      # Handle the user's input
      if conversation_states.get(chat_id) == 'waiting for task details':
          task = command
          add_task(chat_id, datetime.date.today(), task)
          conversation_states[chat_id] = 'idle'
      elif conversation_states.get(chat_id) == 'waiting for delete task details':
          task = command
          delete_task(chat_id, datetime.date.today(), task)
          send_message("Task successfully deleted.", chat_id)
          conversation_states[chat_id] = 'idle'
      else:
            send_message("I don't understand... Press 'help' in the menu 🙄", chat_id)
            conversation_states[chat_id] = 'idle'
  
  # Return a response to the client (if using API Gateway)
  response = {
      "statusCode": 200,
      "body": "OK"
  }
 except Exception as e:
  print(f"Error processing update: {e}")
  response = {
      "statusCode": 500,
      "body": "Internal Server Error"
  }
 
 return response


