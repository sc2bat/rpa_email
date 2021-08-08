import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일" # 제목
msg["From"] = EMAIL_ADDRESS # 발신자
msg["To"] = "dongwuk93@gmail.com" # 수신자
# 다수의 인원에게 발신
#1 # msg["To"] = "ddd@gmail.com", "ccc@gmail.com", "eee@gmail.com"

#2 # to_list = ["ddd@gmail.com", "ccc@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "ddd@gmail.com"
# 비밀참조
# msg["Bcc"] = "ddd@gmail.com"

msg.set_content("TEST_TEST") # 본문

server = smtplib.SMTP('smtp.gmail.com', 587)

with server as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

