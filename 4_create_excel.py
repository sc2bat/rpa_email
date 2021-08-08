# 선정된 3명의 명단을 엑셀 파일로 저장하는 자동화 프로그램

import smtplib
from openpyxl import Workbook
from account import *
from imap_tools import MailBox
from email.message import EmailMessage

max_val = 3 # 선정 수
applicant_list = []

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 
    for msg in mailbox.fetch('(SENTSINCE 25-Dec-2020)'):
        if "파이썬 특강 신청" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. 선정 / 탈락 메일 발송]")
server = smtplib.SMTP('smtp.gmail.com', 587)

with server as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_ 
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = "{}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선착순 {}번)".format(nickname, index)
        else:
            title = "파이썬 특강 안내[탈락]"
            content = "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {}번)".format(nickname, index-max_val)

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)

        print(nickname, "님에게 메일 발송 완료")

print("[3. 선정자 명단 파일 생성]")

wb = Workbook()
ws = wb.active
ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_val]: # 0:3 = 0, 1, 2
    ws.append(applicant[1:])
    # index = applicant[1]
    # nickname = applicant[2]
    # phone = applicant[3] 
    # ws.append([index, nickname, phone])

wb.save("result.xlsx")

print("모든 작업이 완료되었습니다.")