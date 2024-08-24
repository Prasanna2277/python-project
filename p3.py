import smtplib
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
smtp_port = 587  
username = "your-email@gmail.com"
app_password = "your-app-password"


msg = MIMEText("This is the body of the email")
msg["Subject"] = "Subject Line"
msg["From"] = username
msg["To"] = "recipient@example.com"


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(username, app_password)
        server.send_message(msg)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e}")
except Exception as e:
    print(f"Error: {e}")
