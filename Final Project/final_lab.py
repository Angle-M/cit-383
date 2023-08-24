#!/usr/bin/env python

# imports os
import os

#imports argparse
import argparse

#imports datetime
import datetime

#imports smtplib
import smtplib

#imports getpass
import getpass

#imports MIME libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Function to get user input
def get_user_input():
    
    #sets parser to argparse
    parser = argparse.ArgumentParser()
    
    #parser.add_argument for ip
    parser.add_argument("-ip", required=True, help="IP address of a target computer")
    
    #parser.add_argument for username
    parser.add_argument("-u", required=True, help="Username for an account on the target computer")
    
    #parser.add_argument for password
    parser.add_argument("-p", required=True, help="Password for an account on the target computer")
    
    #parser.add_argument for email
    parser.add_argument("-e", required=True, help="Email address of the sender")
    
    #parser.add_argument for cto
    parser.add_argument("-cto", required=True, help="Email address of the CTO")
    
    #parser.add_argument for directory
    parser.add_argument("-d", required=False, help="Directory to which the affected files should be downloaded")
    
    #sets args to parser.parse_args()
    args = parser.parse_args()
    
    #returns args
    return args

#function to identify compromised files
def identify_compromised_files(ip, username, password):
    
    #os.system to ssh into the target computer
    os.system("sshpass -p '{}' ssh {..}@{}".format(password, username, ip))
    
    #sets a_files to os.listdir
    a_files = os.listdir(os.path.expanduser('~'))
    
    #sets t_w_ago to datetime.datetime.now() - datetime.timedelta(weeks=2)
    t_w_ago = datetime.datetime.now() - datetime.timedelta(weeks=2)
    
    #sets compromised_files to []
    compromised_files = []
    
    #for loop to check for modified files
    for file in a_files:
        
        #sets last_modified to datetime.datetime.fromtimestamp(os.path.getmtime(file))
        l_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        
        #checks if last_modified is greater two_weeks_ago
        if l_modified > t_w_ago:
            
            #appends file to compromised_files
            compromised_files.append(file)
            
    #prints compromised files
    print("Compromised Files:")
    
    #loops through compromised_files
    for file in compromised_files:
        
        #prints file, os.path.getsize(file), datetime.datetime.fromtimestamp(os.path.getmtime(file))
        print("\t{}: {}, last modified {}".format(file, os.path.getsize(file), datetime.datetime.fromtimestamp(os.path.getmtime(file))))
        
    #returns compromised_files
    return compromised_files

#function to send email
def send_email(s_email, s_password, cto_email, compromised_files):
    
    #sets message to MIMEMultipart()
    msg = MIMEMultipart()
    
    #sets message["From"] to sender_email
    msg["From"] = s_email
    
    #sets message["To"] to cto_email
    msg["To"] = cto_email
    
    #sets message["Subject"] to "Compromised Files"
    msg["Subject"] = "Compromised Files"
    
    #sets message_body to message
    msg_body = "The following files have been identified as having been modified in the past two weeks:"
    
    #loops through compromised_files
    for file in compromised_files:
        
        #adds to message_body
        msg_body += "\n\t{}: {}, last modified {}".format(file, os.path.getsize(file), datetime.datetime.fromtimestamp(os.path.getmtime(file)))
        
    #attaches message_body to message
    msg.attach(MIMEText(msg_body, "plain"))
    
    #sets file_to_attach to open compromised_files[0]
    file_to_attach = open(compromised_files[0], "rb")
    
    #sets attachment to MIMEBase("application", "octet-stream")
    attachment = MIMEBase("application", "octet-stream")
    
    #sets attachment.set_payload to file_to_attach.read()
    attachment.set_payload(file_to_attach.read())
    
    #sets encoders.encode_base64(attachment)
    encoders.encode_base64(attachment)
    
    #sets attachment.add_header("Content-Disposition", "attachment; filename= {}".format(compromised_files[0]))
    attachment.add_header("Content-Disposition", "attachment; filename= {}".format(compromised_files[0]))
    
    #sets message.attach(attachment)
    msg.attach(attachment)
    
    #trys statement
    try:
        
        #sets server to smtplib.SMTP("email ID", 587)
        server = smtplib.SMTP("email ID", 587)
        
        #starts server
        server.starttls()
        
        #server login
        server.login(s_email, s_password)
        
        #sends email
        server.sendmail(s_email, cto_email, msg.as_string())
        
        #quits server
        server.quit()
        
        #prints "Email sent to CTO"
        print("Email sent to CTO")
    
    #except statement
    except:
        
        #prints "Error sending email"
        print("Error sending email")
        
#function to download files
def download_files(ip, uname, passw, compromised_files, dest_dir):
    
    #checks for dest_dir
    if dest_dir:
        
        #uses os.chdir to change to dest_dir
        os.chdir(dest_dir)
        
    #else statement
    else:
        
        #sets dest_dir to os.path.expanduser('~')
        dest_dir = os.path.expanduser('~')
        
    #loops through compromised_files
    for file in compromised_files:
        
        #system call to scp
        os.system("scp {}@{}:{} {}".format(uname, ip, file, dest_dir))
        
#function main
def main():
    
    # sets args to get_user_input()
    args = get_user_input()
    
    #gets ip
    ip = args.ip
    
    #gets username
    uname = args.u
    
    #gets password
    passw = args.p
    
    #gets sender email
    s_email = args.e
    
    #gets cto email
    cto_email = args.cto
    
    #gets dest_dir
    d_dir = args.d
    
    # sets compromised_files to identify_compromised_files(ip, uname, passw)
    compromised_files = identify_compromised_files(ip, uname, passw)
    
    #gets user input for sender password
    s_password = getpass.getpass(prompt="Enter sender's email password: ")
    
    #sends the email
    send_email(s_email, s_password, cto_email, compromised_files)
    
    # Download files
    download_files(ip, uname, passw, compromised_files, d_dir)
    
# Execute main function
if __name__ == "__main__":
    main()
    print("Done")
    exit()