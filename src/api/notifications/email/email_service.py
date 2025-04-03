from .sendgrid.mailer import SendgridMailer
from .smtp.mailer import SmtpMailer


class EmailService:
    def __init__(self, payload, channel):
        self.payload = payload
        self.mailer = self._get_mailer_channel(channel)

    def _get_mailer_channel(self, channel):
        if channel == "sendgrid":
            return self._sendgrid()
        elif channel == "smtp":
            return self._smtp()
        else:
            raise ValueError(channel)

    def _sendgrid(self):
        return SendgridMailer(self.payload)

    def _smtp(self):
        return SmtpMailer(self.payload)

    def get_mailer(self):
        return self.mailer
