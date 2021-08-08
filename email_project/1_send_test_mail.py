# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#         ex) ㅇㅇㅇ/1234

# 메일 발송 테스트

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

server = smtplib.SMTP('smtp.gmail.com', 587)

with server as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "dongwuk93@gmail.com"

        content = "/".join([nickname, str(randint(1000,9999))])
        msg.set_content(content)

        smtp.send_message(msg)
        print(nickname +"메일 발송 완료")
    