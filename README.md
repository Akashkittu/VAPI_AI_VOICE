Voice AI Receptionist Using Vapi
Overview
This project implements a Voice AI Receptionist using Vapi. It handles incoming calls, logs call data to Google Sheets, and sends appointment confirmation emails. The application uses a Flask web server to expose API endpoints for processing incoming call data from Vapi's webhook, and it integrates with the Google Sheets API and SMTP email service for logging and notifications.

Features
Vapi API Integration: Processes incoming call data and manages voice interactions using Vapi.
Google Sheets Logging: Logs call details (customer number, status, timestamp, transcript, appointment details, email) in real time.
Email Notifications: Sends email confirmations for appointments when an email is provided.
Flask Web Server: Exposes endpoints to handle incoming call data and process requests.
Modular Codebase: Clean, modular, and well-documented Python code following best practices.
Project Structure
graphql
Copy
/voice-ai-receptionist
│-- app.py                     # Main Flask application
│-- vapi_handler.py            # Handles incoming call data from Vapi
│-- sheets_logger.py           # Logs call data into Google Sheets
│-- email_notifier.py          # Sends email notifications
│-- config.py                  # Loads configuration and environment variables
│-- .env                       # Environment variables (DO NOT commit this file)
│-- credentials.json           # Google API credentials (DO NOT commit this file)
│-- token.json                 # OAuth token file for Google Sheets API (generated after first run)
│-- requirements.txt           # Python dependencies
│-- README.md                  # Project documentation
Key Libraries and Tools Used
Flask: A lightweight web framework to build the API.
vapi_python: The Vapi Python SDK used for interacting with Vapi's API.
google-api-python-client: A client library for interacting with Google APIs, including Google Sheets.
google-auth: Provides authentication support for Google APIs.
google-auth-oauthlib: Supports OAuth2 authentication flows.
python-dotenv: Loads environment variables from a .env file.
requests: A simple HTTP library for making API calls.
Standard Libraries:
smtplib and email modules for sending emails (these come with Python and do not require separate installation).
Setup Instructions
Clone the Repository:

bash
Copy
git clone <repository-url>
cd voice-ai-receptionist
Create and Activate a Virtual Environment:

bash
Copy
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the project root with the following content (replace placeholder values with your actual credentials):

ini
Copy
# Vapi Credentials
VAPI_API_KEY=your_vapi_api_key
VAPI_ASSISTANT_ID=your_vapi_assistant_id

# Google Sheets Credentials
GOOGLE_SHEET_ID=1xHMQnVjRCoYFGxLzCFrEjQgPlmL-rhmmqXsIbgZNB4c
GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json

# Email SMTP Credentials (for Gmail, use an App Password if 2FA is enabled)
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465

# Flask Server Port
FLASK_PORT=5000
Secure Sensitive Files: Make sure your .env, credentials.json, and token.json files are added to your .gitignore file:

plaintext
Copy
.env
credentials.json
token.json
Run the Flask Server:

bash
Copy
python app.py
You should see:

csharp
Copy
🚀 Starting Flask server on port 5000
* Running on http://127.0.0.1:5000
Expose Your Local Server (Optional): If you need Vapi to send webhooks to your local server, use a tool like ngrok:

bash
Copy
ngrok http 5000
Then update your Vapi assistant's webhook URL with the generated ngrok URL (e.g., https://<ngrok-id>.ngrok.io/handle_incoming_call).

Usage
Testing the API
1. Test Incoming Call Handling
Simulate an incoming call by sending a POST request. For example, using cURL on Windows:

cmd
Copy
curl -X POST "http://127.0.0.1:5000/handle_incoming_call" ^
     -H "Content-Type: application/json" ^
     -d "{ \"customer\": { \"number\": \"+1234567890\", \"email\": \"nitiburnwal350@gmail.com\" }, \"status\": \"completed\", \"createdAt\": \"2025-02-22T14:30:00Z\", \"appointmentDetails\": \"Your appointment is confirmed for tomorrow at 10 AM.\" }"
Alternatively, use Postman to send a POST request to:

arduino
Copy
http://127.0.0.1:5000/handle_incoming_call
with the following JSON body:

json
Copy
{
  "customer": { "number": "+1234567890", "email": "djjs@gmail.com" },
  "status": "completed",
  "createdAt": "2025-02-22T14:30:00Z",
  "appointmentDetails": "Your appointment is confirmed for tomorrow at 10 AM."
}
2. Expected Response
If everything is configured correctly, you should see a JSON response similar to:

json
Copy
{
  "status": "success",
  "message": "Call from +1234567890 processed successfully.",
  "call_id": "Unknown Call ID",
  "call_status": "completed",
  "email_sent": true
}
Google Sheets: Verify that a new row with call details is added.
Email: Check the recipient’s inbox (djjs@gmail.com) for the confirmation email.