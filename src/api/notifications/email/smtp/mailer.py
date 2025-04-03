import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from jinja2 import Environment, FileSystemLoader


class SmtpMailer:
    def __init__(self, payload):
        self.smtp_host = os.environ.get("EMAIL_HOST")
        self.smtp_port = os.environ.get("EMAIL_PORT", 25)
        self.smtp_user = os.environ.get("EMAIL_HOST_USER")
        self.smtp_password = os.environ.get("EMAIL_HOST_PASSWORD")
        self.from_email = os.environ.get("CONTACT_EMAIL")
        self.payload = payload
        self.env = Environment(
            loader=FileSystemLoader("%s/templates/" % os.path.dirname(__file__))
        )

    def send_email(self, subject, content, is_html=False):
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = self.from_email
        message["To"] = self.payload["user_email"]

        message.attach(MIMEText(content, "html"))
        msgBody = message.as_string()

        with SMTP(self.smtp_host, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.from_email, self.payload["user_email"], msgBody)
