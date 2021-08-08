# pip install imap-tools

from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

for msg in mailbox.fetch(limit=1, reverse=True):
    # limit 최대 메일 갯수 reverse= True 최근부터, False 오래된것부터
    print("title", msg.subject)
    print("who", msg.from_)
    print("To", msg.to)
    # print("참조", msg.cc)
    # print("비밀참조", msg.bcc)
    print("date", msg.date)
    print("text", msg.text)
    print("MTML msg", msg.html)
    print("=" *100)

    # 첨부파일
    for att in msg.attachments:
        print("첨부파일이름", att.filename)
        print("type", att.content_type)
        print("size", att.size)
    # 첨부파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))

mailbox.logout()