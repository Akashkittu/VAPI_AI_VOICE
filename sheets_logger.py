import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load environment variables from .env file
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE")

# Define Google Sheets API Scope (Read & Write Access)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def authenticate_google_sheets():
    """Authenticate and return Google Sheets API service."""
    creds = None

    # Check if token.json exists (stores user credentials)
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no valid credentials, authenticate using OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(GOOGLE_CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)

def log_call_data(call_data):
    """
    Logs Vapi call data into Google Sheets.
    - call_data: Dictionary containing call details.
    """
    try:
        service = authenticate_google_sheets()
        sheet = service.spreadsheets()
        
        # Extract required details from the call data
        caller_number = call_data.get("customer", {}).get("number", "Unknown")
        call_status = call_data.get("status", "Unknown")
        timestamp = call_data.get("createdAt", "N/A")
        appointment_details = call_data.get("appointmentDetails", "No details available")
        customer_email = call_data.get("customer", {}).get("email", "No email provided")

        values = [[caller_number, call_status, timestamp, appointment_details, customer_email]]
        body = {"values": values}

        sheet.values().append(
            spreadsheetId=GOOGLE_SHEET_ID,
            range="A:D",
            valueInputOption="RAW",
            body=body
        ).execute()

        print(f"✅ Call data logged successfully: {values}")

    except HttpError as err:
        print(f"❌ Google Sheets API Error: {err}")

if __name__ == "__main__":
    # Example test data (replace with actual call data)
    sample_call_data = {
        "customer": {
            "number": "+1234567890",
            "email": "nitiburnwal350@gmail.com"
        },
        "status": "completed",
        "createdAt": "2025-02-22T14:30:00Z",
        "appointmentDetails": "Your appointment is confirmed for tomorrow at 10 AM."
    }

    log_call_data(sample_call_data)
