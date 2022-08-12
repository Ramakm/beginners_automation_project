#import modules 

from http import server
import smtplib
import ssl
from email.message import EmailMessage

Subject = " Email from Python"
Body = "This is a test email from python!"

sender_email = "XXXXXXXXXXXXXXXXXX@gmail.com" #give a proper email as i removed mine
receiver_email = "XXXXXXXXXXXXXXXXX@gmail.com" #Give a proper email as i removed mine

password = input("Enter a Password: ")

#Build email by using EmailMessage

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = Subject

message.set_content(Body)

context = ssl.create_default_context()  #we need this becuz when we connect to gmail we need a secure connection. ssl will provide that

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())  #We are doing as_string becuz we are converting the message into a string and send it to the receiver

print("Success")
