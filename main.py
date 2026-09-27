import pandas as pd

import fetch_schedule
import send_email
import write_email

row = fetch_schedule.get_next_session()
email_info = write_email.write_emails(row)

time_till_next_session = row["Date"] - pd.Timestamp.today().normalize()

if time_till_next_session.days < 13:
    
    send_email.send_email(to=email_info[0], subject="Reminder: you will be a speaker at the journal club", html=email_info[1])

    if pd.notna(row["Backup"]) and pd.notna(row["Backup email"]):
        send_email.send_email(to=email_info[2], subject="Reminder: you will be a backup speaker at the journal club", html=email_info[3])