from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True): # 전체메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
        

    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지않은메일 가져오기
        # print("[{}] {}".format(msg.from_, msg.subject))
        
    # for msg in mailbox.fetch('(FROM dongwuk93@gmail.com)', limit=2, reverse=True): # 특정 발신메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(TEXT "test mail")'): # 특정 글자 포함 가져오기(제목, 본문)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test")'): # 특정 글자 포함 가져오기제목
    #     print("[{}] {}".format(msg.from_, msg.subject))
    #     # UnicodeEncodeError: 'ascii' codec 한글은 힘듦

# 어떤 글자 (한글 가능) 필터
    for msg in mailbox.fetch():
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))