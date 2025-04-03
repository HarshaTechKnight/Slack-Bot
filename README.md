# Slack Bot with Python using Slack Events API & Django

## Introduction
This repository contains a Slack bot built using Python, Django, and the Slack Events API. The bot listens to Slack events, processes messages, and responds accordingly.

## Features
- Listens for messages in Slack channels
- Responds to specific keywords or commands
- Uses Slack Events API for real-time event handling
- Implements Django as the backend framework

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- Django
- Slack API credentials
- ngrok (for local development)

## Setup

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/slack-bot-django.git
cd slack-bot-django
```

### 2. Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Slack App
1. Go to [Slack API Apps](https://api.slack.com/apps) and create a new app.
2. Enable **Socket Mode** and **Event Subscriptions**.
3. Subscribe to bot events like `message.channels` and `app_mention`.
4. Generate and copy the **Bot User OAuth Token**.
5. Add the bot to your Slack workspace.

### 5. Set Environment Variables
Create a `.env` file in the project root and add:
```
SLACK_BOT_TOKEN='your-slack-bot-token'
SLACK_SIGNING_SECRET='your-slack-signing-secret'
```

### 6. Apply Migrations
```sh
python manage.py migrate
```

### 7. Run the Development Server
```sh
python manage.py runserver
```

### 8. Set Up ngrok (for Local Development)
```sh
ngrok http 8000
```
Copy the **https** URL provided by `ngrok` and update your Slack event subscription request URL to:
```
https://your-ngrok-url/slack/events/
```

## Usage
- Mention the bot in a Slack channel to trigger a response.
- Extend the bot by modifying `views.py` in the Django app.

## Deployment
To deploy on a production server:
1. Use a production-ready database (PostgreSQL, MySQL, etc.)
2. Set `DEBUG=False` in Django settings
3. Use a production-ready web server like Gunicorn

## Contributing
Feel free to fork this repository, open issues, or submit pull requests.

## License
This project is licensed under the MIT License.
