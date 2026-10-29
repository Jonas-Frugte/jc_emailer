import pandas as pd

SCHEDULE_URL = "https://docs.google.com/spreadsheets/d/1jsMeb0MDqyzUjYp_A6jo_vScGJpHpBcJsnMQF2ELCB0/edit?usp=sharing"
ORGANIZER_EMAIL = "j.s.a.frugte@uu.nl"

def _format_date(date: pd.Timestamp) -> str:
    # e.g. "Wednesday 7 October 2026"
    return f"{date:%A} {date.day} {date:%B %Y}"

def _footer() -> str:
    return f"""
<p>If you won't be available, please email me at
<a href="mailto:{ORGANIZER_EMAIL}">{ORGANIZER_EMAIL}</a> as soon as possible.</p>
<p>You can find the full schedule here: <a href="{SCHEDULE_URL}">journal club schedule</a>.</p>
<p>Best,<br>Jonas Frugte<br>Journal club organizer</p>
"""


def reminder_email(name: str, date: pd.Timestamp) -> str:
    return f"""<html><body>
<p>Hi {name},</p>
<p>This is a reminder that you are scheduled as the <b>speaker</b> at journal club on
<b>{_format_date(date)} at 10:00</b> in room <b>BB 7.12</b> (Buys Ballot building).</p>
<p>Please upload the paper you will be presenting to the journal club Teams channel before the session.</p>
{_footer()}
</body></html>"""


def reminder_email_backup(name: str, date: pd.Timestamp) -> str:
    return f"""<html><body>
<p>Hi {name},</p>
<p>This is a reminder that you are scheduled as the <b>backup speaker</b> at journal club on
<b>{_format_date(date)} at 10:00</b> in room <b>BB 7.12</b> (Buys Ballot building).</p>
<p>The backup speaker is always the person presenting at the session after, so you will already
be preparing a paper anyway. If the scheduled speaker can't make it, you would simply present
your paper one session early.</p>
<p>Please upload the paper you will be presenting to the journal club Teams channel.</p>
{_footer()}
</body></html>"""

def write_emails(row: pd.Series) -> tuple[str, str, str, str]:
    email_speaker = row["Speaker email"]
    name_speaker = row["Speaker"]
    email_backup = row["Backup email"]
    name_backup = row["Backup"]
    date = row["Date"]

    email = reminder_email(name=name_speaker, date=date)
    backup_email = reminder_email_backup(name=name_backup, date=date)

    return email_speaker, email, email_backup, backup_email

    