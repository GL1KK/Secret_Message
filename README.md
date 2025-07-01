# SMS Message Sharing Service

A simple FastAPI application for temporary storage and sharing of SMS messages. Messages can only be read once.

## Features

- Send SMS messages with sender name
- Retrieve SMS messages via unique URL (message is deleted after first read)
- Automatic generation of unique URLs for each message

## API Endpoints

### Send SMS Message

**POST** `/post_sms`

Parameters:
- `name`: Sender name (string)
- `sms`: Message text (string)

Response:
- Access URL in format: `http://127.0.0.1:8000/sms/{sms_id}`

### Retrieve SMS Message

**GET** `/sms/{sms_id}`

Parameters:
- `sms_id`: Unique message identifier (from URL)

Response:
- JSON object with fields:
  - `name`: Sender name
  - `sms`: Message text

After successful retrieval, the message is deleted from the system.

For repeated requests to the same `sms_id`:
- Returns 404 error with message "Message has already been viewed!"

## Installation and Setup

1. Ensure you have Python 3.7+ and Poetry installed
2. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/GL1KK/Secret_Message.git
   cd Secret_Message
   pip install poetry
   poetry shell
   poetry install
   cd app
   uvicorn main:app --reload
   ```
