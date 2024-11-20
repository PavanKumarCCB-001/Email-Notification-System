from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Email_Notification_System"]
templates_collection = db["action_template"]
notifications_collection = db["notifications"]

# Email credentials
SENDER_EMAIL = "Give Sender email"
APP_PASSWORD = "Give the App generated Password"


# Function to send an email using MIMEMultipart
def send_email(receiver_email, subject, body):
    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")


# Function to process pending notifications
def process_notifications():
    # Find all pending notifications
    pending_notifications = notifications_collection.find({"status": "pending"})

    for notification in pending_notifications:
        action = notification["action"]
        email = notification["email"]

        # Fetch the template for the action
        template = templates_collection.find_one({"action": action})
        if not template:
            print(f"No template found for action: {action}")
            continue

        # Format the subject and body with placeholders
        subject = template["subject"]
        body = template["body"].format(**notification.get("data", {}))

        # Send the email
        try:
            send_email(email, subject, body)

            # Update notification status to 'sent'
            notifications_collection.update_one(
                {"_id": notification["_id"]},
                {"$set": {"status": "sent"}}
            )
        except Exception as e:
            print(f"Error sending email: {e}")

    print("All pending notifications have been processed.")


# Run the notification processor
process_notifications()
