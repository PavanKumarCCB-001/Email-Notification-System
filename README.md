# Email-Notification-System using MongoDB
This is a Dynamic Email Notification System developed using Python and MongoDB. It sends notifications to the users over emails in case of certain events such as requesting a password reset, logging in from a new device, and so on. The system employs a MongoDB database for capturing user actions and storing email templates.

**Features:**
1) _Dynamic Email Notifications_: Sends personalized emails to users based on the actions they perform.
2) _MongoDB Integration_:         Stores user actions and email templates for flexibility and scalability.
3) _Custom Email Templates_:       Create and manage action-specific email templates.
4) _Secure Email Sending_:       Uses an App Password for secure email authentication.
   
**Tech Stack:**


-> Programming Language: Python

-> Database: MongoDB
Libraries:
pymongo:  For MongoDB integration
smtplib:  For sending emails
email:  for building structured email message
