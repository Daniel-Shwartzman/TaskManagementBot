<!-- ABOUT THE PROJECT -->
## About The Project

The Task Management Bot is a serverless application designed to assist in task management. It is deployed using AWS Lambda, API Gateway for endpoint management, CloudWatch Logs for logging, and a webhook for communication.


### Key features of this project:
- Serverless architecture
- AWS
- Python



### Built With
The project is built with Python, AWS Lambda, AWS API Gateway, AWS CloudWatch Logs:

[![Python][Python]][Python-url]     [![AWS Lambda][AWS Lambda]][lambda-url]     [![API Gateway][API Gateway]][api-gateway-url]     [![CloudWatch][CloudWatch]][cloudwatch-url]




<!-- Getting Started Section -->
## Getting Started
To get started, follow the steps below:


<!-- Requirements Section -->
### Requirements

- Python 
- requests
- AWS account

  
<!-- Installation Section -->
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Daniel-Shwartzman/task-management-bot.git
   cd task-management-bot
    ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
    ```



## Setup

### AWS Lambda

1. Open the AWS Lambda Console:
   - Go to the AWS Lambda Console.
     
2. Create a Lambda Function:
   - Click the "Create function" button.
     
3. Select Author from Scratch:
   - Choose "Author from scratch."
     
4.Configure the Basic Information:
  - Function Name: Enter a unique name for your function.
  - Runtime: Choose the runtime for your function (e.g., Python, Node.js).
  - Role: Choose an existing role or create a new one with basic Lambda permissions.

5.Click "Create Function":
  - After configuring the basic information, click the "Create function" button.

### AWS API Gateway

1.Open the API Gateway Console:
  - Go to the API Gateway Console.
    
2.Create a New API:
  - Click the "Create API" button.
    
3.Choose "HTTP API":

4.Configure Your API:
  - Enter a name for your API.
  - Optionally, add a description.
  - Click the "Create API" button.



### Webhook

#### For Windows:
```bat
Invoke-RestMethod -Uri "https://api.telegram.org/bot<TOKEN>/setWebhook?url=<Your_API_Invoke_URL>" -Method Post
```

#### For Linux:
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=<Your_API_Invoke_URL>"
```


## Deployment Package
1. Copy bot.py and paste it in Lambda.
2. Config webhook
3. Click deploy
4. Run a test (optinal)



## Notes
1. Make sure the lambda handler is your module name.lamda_handler (ex. bot.lamda_handler)
2. Make sure you set your API Gateway as HTTP API and POST
3. Don't forget to config the webhook




### Screenshots
![Screenshot](static/images/login-screenshot.png)
![Screenshot](static/images/dashboard-screenshot.png)
![Screenshot](static/images/darkmode-screenshot.png)

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-FDEE00?style=for-the-badge&labelColor=black&logo=python&logoColor=FDEE00
[Python-url]: https://www.python.org
[AWS Lambda]: https://img.shields.io/badge/AWS_Lambda-FF4F00?style=for-the-badge&labelColor=black&logo=amazon-aws&logoColor=FF4F00
[lambda-url]: https://aws.amazon.com/lambda/?nc2=type_a
[API Gateway]: https://img.shields.io/badge/API_Gateway-DE3163?style=for-the-badge&labelColor=black&logo=amazon-aws&logoColor=DE3163
[api-gateway-url]: https://aws.amazon.com/api-gateway/?nc2=type_a
[CloudWatch]: https://img.shields.io/badge/CloudWatch-D0417E?style=for-the-badge&labelColor=black&logo=amazon-aws&logoColor=D0417E
[cloudwatch-url]: https://aws.amazon.com/cloudwatch/?nc2=type_a




