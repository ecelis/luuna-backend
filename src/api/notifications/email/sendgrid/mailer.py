import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendgridMailer:
    def __init__(self, payload):
        self.api_key = os.environ.get("SENDGRID_API_KEY")
        self.from_email = os.environ.get("CONTACT_EMAIL")
        self.payload = payload
        self.sendgrid = SendGridAPIClient(self.api_key)

    def send_email(self, subject, content, is_html=False):
        content_type = "text/html" if is_html else "text/plain"
        message = Mail(
            from_email=self.from_email,
            to_emails=self.payload["user_email"],
            subject=subject,
            html_content=content_type,
            plain_text_content=content if not is_html else None,
        )

        try:
            response = self.sendgrid.send(message)
            return response.status_code
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return None
