# Email Notification System using MongoDB
This is a Dynamic Email Notification System developed using Python and MongoDB. It sends notifications to the users over emails in case of certain events such as requesting a password reset, logging in from a new device, and so on. The system employs a MongoDB database for capturing user actions and storing email templates.

## Features

- _Dynamic Email Notifications:_ Sends personalized emails to users based on the actions they perform.

- _MongoDB Integration:_ Stores user actions and email templates for flexibility and scalability.

- _Custom Email Templates:_ Create and manage action-specific email templates.

- _Secure Email Sending:_ Uses an App Password for secure email authentication.

## Tech Stack

**Programming Language :** Python

**Database:** MongoDB

**Libraries Used:**

pymongo for MongoDB integration

smtplib for sending emails

email for building structured email messages
## Prerequisites
1) Install the MongoDB 
2) Install Python 3.x 
3) Configure your Gmail account to allow App Passwords.
    

## Installation

1) Inorder to execute this code Let's Install pymongo

```bash
  pip3 install pymongo
```
2) Create a database and collections in MongoDB:
  - Database: Email_Notification_System
  - **Collections:**
  - action_template
  - notifications: Stores triggered actions for sending emails.

3) Populate MongoDB collections:
        
   You can Insert the Follwing Documents in action_template Collection:


    {
    
        "action": "password_reset",
        "subject": "Reset Your Password",
        "body": "Hello {name},\nYou requested to reset your password. If this was not you,please contact support."
    }

    {
    
        "action": "Log-from-other-dev",
        "subject": "Logging in from Another Device",
        "body": "Hello {name},\nYou are trying to Login from Another Device."
    }
    
    Now Insert the following document in the Notifications collection:


    {
        
        "email" : "receiver's Email",
        "action" : "password_reset",
        "data": { "name": "Receiver's name" },
        "status":"pending"
    }

## Screenshots


Upon successful execution of the Python script, the status of the notifications in MongoDB will be updated to **"Sent"**.

![image](https://github.com/user-attachments/assets/9fd23c66-ee11-4d2c-af2b-f4b734d89ffb)

