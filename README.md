# Keylogger with Email Notification
This Python script serves as a basic keylogger that monitors keyboard input. It records the keys pressed and periodically sends them via email to a specified recipient. Please use this code responsibly and ethically.


## Prerequisites
**pynput:** A Python library for monitoring keyboard input.<br>
**smtplib:** A Python library for sending emails.<br>
**sched:** A Python library for scheduling tasks.<br>
**time:** A Python library for working with time.<br>
**threading:** A Python library for managing threads.<br>


## Usage
1. Install the required libraries using 'pip':
   
    pip install pynput<br>
    pip install smtplib
  
2. Replace the placeholder email addresses (senderEmail and receiver_email) with your own.
   
3. Update the password in the server.login() call with the actual password. Be cautious not to expose sensitive information in your code.


## How it Works
1. The script imports the necessary libraries for keyboard monitoring, email sending, scheduling, time management, and threading.

2. It sets an interval (seconds) for sending emails.

3. The sendMail function takes a key argument and sends an email with the pressed keys to the specified recipient.

4. The schedule_mail_send function is responsible for periodically checking the log file (keyLogs.txt), sending its content via email, and then clearing the log file.

5. When a key is pressed, the keyPressed function prints the pressed key and writes it to the log file.

6. In the main part of the program, it starts a listener to monitor keyboard input. It sets up a scheduler to periodically call the schedule_mail_send function, and starts a separate thread for the scheduler to run independently.

7. The program waits for an input, ensuring it continues to run until manually stopped.


**Note:** Be cautious while using this script and ensure you have proper authorization to monitor and record keyboard input. Unauthorized use of this script may violate privacy and legal standards. Always use it responsibly and in compliance with applicable laws and regulations.
