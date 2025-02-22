
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Vapi configuration
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")

# Google Sheets configuration

GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

# Email (SMTP) configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")

# Flask configuration
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
