import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일" 
msg["From"] = EMAIL_ADDRESS 
msg["To"] = "dongwuk93@gmail.com" 
msg.set_content("다운로드하세요")

# 파일 첨부
# msg.add_attachment()
with open("daum.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

server = smtplib.SMTP('smtp.gmail.com', 587)

with server as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
