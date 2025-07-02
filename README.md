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
  - `sms`: Message text8u

After successful retrieval, the message is deleted from the system.

For repeated requests to the same `sms_id`:
- Returns 404 error with message "Message has already been viewed!"
