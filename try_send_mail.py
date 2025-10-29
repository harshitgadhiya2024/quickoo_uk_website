import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from email.mime.base import MIMEBase
from email import encoders
import os

html_body = """
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <h2 style="color: #2c3e50;">Quickoo Website: Contact Form Submission</h2>

    <table style="width: 100%; max-width: 600px; border-collapse: collapse;">
        <tr>
            <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold; width: 100px;">Name:</td>
            <td style="padding: 10px; background-color: #ffffff;">{name}</td>
        </tr>
        <tr>
            <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold;">Email:</td>
            <td style="padding: 10px; background-color: #ffffff;"><a href="mailto:{email}">{email}</a></td>
        </tr>
        <tr>
            <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold;">Phone:</td>
            <td style="padding: 10px; background-color: #ffffff;">{phone}</td>
        </tr>
    </table>

    <div style="margin-top: 20px; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #2c3e50;">
        <h3 style="margin-top: 0;">Message:</h3>
        <p style="white-space: pre-wrap;">{message}</p>
    </div>

    <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;">
    <p style="font-size: 12px; color: #666;">This email was sent from the Quickoo UK website contact form.</p>
</body>
</html>
            """

# Create Email Message
msg = MIMEMultipart()
msg["From"] = "info@quickoo.co.uk"
msg["To"] = "guest.quickoo@gmail.com"
msg["Subject"] = "Quickoo Website: Contact Form Submission"
msg.attach(MIMEText(html_body, "html"))  # Set as HTML

# Connect to SMTP Server
server = smtplib.SMTP("smtp.hostinger.com", 587)
server.starttls()  # Secure the connection
server.login("info@quickoo.co.uk", "Quickoo@#2025")
server.send_message(msg)
server.quit()