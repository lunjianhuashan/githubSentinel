import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Notifier:
    def __init__(self, config):
        self.config = config

    def send_notification(self, report):
        if self.config['email']['enabled']:
            self._send_email(report)

    def _send_email(self, report):
        sender = self.config['email']['from']
        receiver = self.config['email']['to']
        smtp_server = self.config['email']['smtp_server']
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "GitHub Repository Update Report"
        
        msg.attach(MIMEText(report, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server)
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()
            print("Notification sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
