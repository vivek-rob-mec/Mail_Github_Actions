import smtplib
from email.mime.text import MIMEText ## MIMEtext is a class that represent the text of email
from email.mime.multipart import MIMEMultipart ## It's a class that represent the email message itself
import os

def send_email(workflow_name, repo_name, workflow_run_id): ## these are name we will be getting in our mail
    # Email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv("RECEIVER_EMAIL")

    # Email message
    subject = f"workflow {workflow_name} failed for repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed for the repo {repo_name}. Please check the logs for more details.\nMore details: \nRun_id: {workflow_run_id} "

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Make a connection with teh server
    try:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login(sender_email,sender_password)
       text = msg.as_string()
       server.sendmail(sender_email,receiver_email,text)
       server.quit()

       print("Email sent successfully")
    
    except Exception as e:
        print(f"Error: {e}")


send_email(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))    