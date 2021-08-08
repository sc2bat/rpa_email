import smtplib
from account import *

# socket.gaierror: [Errno 11001] getaddrinfo failed
# smtplib.SMTP("smtp.gamil.com", 587)

# server = smtplib.SMTP('64.233.184.108')
server = smtplib.SMTP('smtp.gmail.com', 587)

with server as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 모든 이메일은 암호화되어 전송 기본
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"Subject: {subject}\n{body}"
    # 발신자 수신자 메세지 프레임
    smtp.sendmail(EMAIL_ADDRESS, "dongwuk93@gmail.com", msg)

