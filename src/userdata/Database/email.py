import smtplib
import sqlite3
import database_def as db
con = sqlite3.connect("guid.db")
cur = con.cursor()


# Here are the email package modules we'll need.
from email.message import EmailMessage

# Create the container email message.
msg = EmailMessage()
msg['Subject'] = 'Velkommen til safaritur'
#Lag en ekte email kanskje?
msg['From'] = "Admin-mail"
#DETTE SKAL FUNGERE I TEORIEN MEN MÅ HA VARIABLET FRA TKINTER NÅR HAN LOGGER INN
msg['To'] = db.email_henter("brukernavn")
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

# Open the files in binary mode.  You can also omit the subtype
# if you want MIMEImage to guess it.

# Send the email via our own SMTP server.
with smtplib.SMTP('localhost') as s:
    s.send_message(msg)