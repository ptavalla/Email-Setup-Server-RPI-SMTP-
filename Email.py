import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS port

# Replace with your Gmail address and app-specific password
SENDER_EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # Use an app password if 2FA is enabled

# Recipient email
RECIPIENT_EMAIL = "recipient@example.com"

# Email content
subject = "Test Email from Raspberry Pi using Gmail"
body = "This is a test email sent from my Raspberry Pi using Gmail with authentication."

# Create the email message
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

server = None  # Initialize server to None
try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Log in to your Gmail account
    server.login(SENDER_EMAIL, PASSWORD)
    # Send the email
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if server is not None:
        server.quit()
