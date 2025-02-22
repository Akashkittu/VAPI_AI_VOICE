from config import VAPI_API_KEY
from email_notifier import send_email  # Import email function
import json

def handle_vapi_call(call_data):
    """
    Handles incoming calls from Vapi.

    - Extracts relevant call details.
    - Logs the call information.
    - Sends email confirmation if email is available.
    - Returns a structured response.

    Parameters:
    call_data (dict): JSON data from Vapi webhook.

    Returns:
    dict: Response confirming the call was processed.
    """

    # Extracting relevant information from the call data
    call_id = call_data.get("call", {}).get("id", "Unknown Call ID")
    customer_number = call_data.get("customer", {}).get("number", "Unknown Number")
    status = call_data.get("status", "Unknown Status")
    transcript = call_data.get("transcript", "No transcript available")
    email = call_data.get("customer", {}).get("email")  # Extract email
    appointment_details = call_data.get("appointmentDetails", "No details available")

    print(f"📞 Incoming Call ID: {call_id}")
    print(f"📌 Customer Number: {customer_number}")
    print(f"✅ Call Status: {status}")
    print(f"📝 Transcript: {transcript}")

    # Send Email Confirmation (If Email Exists)
    email_sent = False
    if email:
        print(f"📧 Sending appointment confirmation to {email}...")
        send_email(email, appointment_details)
        email_sent = True

    # Response JSON
    response = {
        "status": "success",
        "message": f"Call from {customer_number} processed successfully.",
        "call_id": call_id,
        "call_status": status,
        "email_sent": email_sent  # Indicate if email was sent
    }
    
    return response
