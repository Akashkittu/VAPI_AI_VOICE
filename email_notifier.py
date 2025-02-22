import smtplib  # Standard library for sending emails
from email.mime.text import MIMEText  # For email text formatting
from email.mime.multipart import MIMEMultipart  # For handling attachments
import ssl  # For secure connection
from config import SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD


def send_email(to_email, appointment_details):
    """
    Sends an appointment confirmation email to the specified address.
    Uses SMTP_SSL for a secure email connection.
    """
    
    try:
        # Email subject and content
        subject = "Appointment Confirmation"
        body = f"Hello,\n\nYour appointment is confirmed.\n\n📅 Details:\n{appointment_details}\n\nBest regards,\nVoice AI Receptionist"
        
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Secure email sending
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            print(EMAIL_PASSWORD, EMAIL_USERNAME)
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, to_email, msg.as_string())

        print(f"✅ Email sent successfully to {to_email}")

    except smtplib.SMTPAuthenticationError:
        print("❌ SMTP Authentication Error: Check your email username/password.")
    except smtplib.SMTPConnectError:
        print("❌ Connection Error: Unable to connect to the email server.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP Error: {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected Error Sending Email: {str(e)}")


