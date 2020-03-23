from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
servers = {"gmail": "smtp.gmail.com", "hotmail": "smtp.live.com",
           "yahoo": "smtp.mail.yahoo.com"}


class vex:
    def __init__(self, provider, username, password):
        self.provider = servers[provider]
        self.username = username
        self.password = password

    def send(self, to_addr, subject, message):
        msg = MIMEText(message, 'plain')
        msg['Subject'] = subject
        msg['From'] = self.username
        est = SMTP(self.provider)
        est.login(self.username, self.password)
        est.sendmail(self.username, to_addr, msg.as_string())
        est.quit


# infos = vex('gmail', 'johndoe@gmail.com', 'password')
# infos.send('to@gmail.com', 'Subject', 'Message')
