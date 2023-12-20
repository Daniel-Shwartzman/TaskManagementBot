<!-- ABOUT THE PROJECT -->
## About The Project

The Task Management Bot is a serverless application designed to assist in task management. It is deployed using AWS Lambda, API Gateway for endpoint management, CloudWatch Logs for logging, and a webhook for communication.

### Key features of this project:
*Serverless architecture
*AWS
*Python


### Built With
The project is built with Python, AWS Lambda, AWS API Gateway, AWS CloudWatch Logs, Webhook:

[![Python][Python]][Python-url] [![AWS Lambda][lambda-badge]][lambda-url] [![API Gateway][api-gateway-badge]][api-gateway-url] [![CloudWatch][cloudwatch-badge]][cloudwatch-url]


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

### Usage

1. Run the application:
   ```bash
   python3 app.py
    ```

2. Open your web browser and navigate to http://localhost:5000/ to access the monitoring dashboard. (username: admin ; password: admin)
3. Monitor your system's CPU and memory usage in real-time and view historical data for analysis.

<!-- Docker Section -->
### Docker image
[![Docker][Docker]][Docker-url]
1. Run this command to build a Docker image
```bash
sudo docker built -t <image-name> .
```

2. To start the Flask server run this command
```bash
docker run -p 5000:5000 <image-name>
``` 

This will start the Flask server in a docker conatiner on your localhost. \
Navigate to [http://localhost:5000/](http://localhost:5000/) on your browser to access the application. \
(username: admin ; password: admin)

### Screenshots
![Screenshot](static/images/login-screenshot.png)
![Screenshot](static/images/dashboard-screenshot.png)
![Screenshot](static/images/darkmode-screenshot.png)

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-3C873A?style=for-the-badge&labelColor=black&logo=python&logoColor=3C873A
[Python-url]: https://www.python.org
[AWS Lambda]: https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3AAmazon_Lambda_architecture_logo.svg&psig=AOvVaw1kbJN00kSmmX4HqkFLSts5&ust=1703197207581000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJDGlJqGn4MDFQAAAAAdAAAAABAE
[lambda-url]: https://aws.amazon.com/lambda/?nc2=type_a
[API Gateway]: https://icons8.com/icon/55497/rest-api
[api-gateway-url]: https://aws.amazon.com/api-gateway/?nc2=type_a
[CloudWatch]: ![image](https://github.com/Daniel-Shwartzman/TaskManagementBot/assets/135250441/500830d5-dd61-4dfc-a36a-15cf91492737)
[cloudwatch-url]: https://aws.amazon.com/cloudwatch/?nc2=type_a




