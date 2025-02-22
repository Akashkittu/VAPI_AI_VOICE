# Voice AI Receptionist Using Vapi


## Overview
This project implements a Voice AI Receptionist using Vapi. It handles incoming calls, logs call data to Google Sheets, and sends appointment confirmation emails. The application uses a Flask web server to expose API endpoints for processing incoming call data from Vapi's webhook, and it integrates with the Google Sheets API and SMTP email service for logging and notifications.

## Features
Vapi API Integration: Processes incoming call data and manages voice interactions using Vapi.
Google Sheets Logging: Logs call details (customer number, status, timestamp, transcript, appointment details, email) in real time.
Email Notifications: Sends email confirmations for appointments when an email is provided.
Flask Web Server: Exposes endpoints to handle incoming call data and process requests.
Modular Codebase: Clean, modular, and well-documented Python code following best practices.

## Project Structure


**│-- app.py**                     # Main Flask application

**│-- vapi_handler.py**            # Handles incoming call data from Vapi

**│-- sheets_logger.py**           # Logs call data into Google Sheets

**│-- email_notifier.py**          # Sends email notifications

**│-- config.py**                  # Loads configuration and environment variables

**│-- .env**                       # Environment variables (DO NOT commit this file)

**│-- credentials.json**           # Google API credentials (DO NOT commit this file)

**│-- requirements.txt**           # Python dependencies

**│-- README.md**                  # Project documentation

## Key Libraries and Tools Used
**Flask:** A lightweight web framework to build the API.

**vapi_python:** The Vapi Python SDK used for interacting with Vapi's API.

**google-api-python-client:** A client library for interacting with Google APIs, including Google Sheets.

**google-auth:** Provides authentication support for Google APIs.

**google-auth-oauthlib:** Supports OAuth2 authentication flows.

**python-dotenv:** Loads environment variables from a .env file.

**requests:** A simple HTTP library for making API calls.

**Standard Libraries:**
  smtplib and email modules for sending emails (these come with Python and do not require separate installation).


### pip install -r requirements.txt

## Set Up Environment Variables: Create a .env file in the project root with the following content (replace placeholder values with your actual credentials):
  ##### Vapi Credentials
  VAPI_API_KEY=your_vapi_api_key
  
  VAPI_ASSISTANT_ID=your_vapi_assistant_id
  
  ##### Google Sheets Credentials
  GOOGLE_SHEET_ID=1xHMQnVjRCoYFGxLzCFrEjQgPlmL-rhmmqXsIbgZNB4c
  
  GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
  
  ##### Email SMTP Credentials (for Gmail, use an App Password if 2FA is enabled)
  EMAIL_USERNAME=your-email@gmail.com
  
  EMAIL_PASSWORD=your-app-password
  
  SMTP_SERVER=smtp.gmail.com
  
  SMTP_PORT=465
