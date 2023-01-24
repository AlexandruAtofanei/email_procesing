import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your name'
email['to'] = 'example@email.com'
email['subject'] = 'python test'

email.set_content(html.substitute({'name': 'George'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com', '2fa key')
    smtp.send_message(email)
    print('worked')
