import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

GMAIL_ADDRESS = "jonasfrugte@gmail.com"
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
 
def send_email(to: str, subject: str, html: str) -> None:
    msg = EmailMessage()
    msg["From"] = f"Jonas Frugte <{GMAIL_ADDRESS}>"
    msg["To"] = to
    msg["Reply-To"] = "j.s.a.frugte@uu.nl"
    msg["Subject"] = subject
    msg.set_content(html, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)

