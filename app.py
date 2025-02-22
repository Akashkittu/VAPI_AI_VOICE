import json
import time
from flask import Flask, request, jsonify
from vapi_handler import handle_vapi_call
from sheets_logger import log_call_data
from email_notifier import send_email
from config import FLASK_PORT

app = Flask(__name__)

@app.route('/handle_incoming_call', methods=['POST'])
def handle_incoming_call():
    """
    Endpoint to process incoming calls from Vapi.
    Extracts caller information, logs data, and sends confirmation emails.
    """
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    customer_number = data.get("customer", {}).get("number")
    email = data.get("customer", {}).get("email")
    appointment_details = data.get("appointmentDetails", "No details available")
    if not customer_number:
        return jsonify({"error": "Customer number is missing"}), 400

    print(f"📞 Incoming call from: {customer_number}")

    try:
        # Process the call data
        response = handle_vapi_call(data)

        # Log call data to Google Sheets
        log_call_data(data)

        # If email is provided, send confirmation email
        if email:
            send_email(email, appointment_details)
            response["email_sent"] = True
            print(f"📧 Email sent to: {email}")
        else:
            response["email_sent"] = False
            print("⚠️ No email provided. Skipping email notification.")


        return jsonify(response), 200
    
    except Exception as e:
        print(f"❌ Error handling incoming call: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    port = FLASK_PORT or 5000  # Default to port 5000 
    print(f"🚀 Starting Flask server on port {port}")
    app.run(debug=True, port=port)
