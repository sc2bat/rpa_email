from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
   
   # 특정 날짜 이후
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # 특정 날짜의 메일
    # for msg in mailbox.fetch('(ON 07-Nov-2020)', reverse=True, limit=5):
    #     print("[{}] {}".format(msg.from_, msg.subject))

# imap_tools
# https://pypi.org/project/imap-tools/

    # 두가지 이상의 조건을 만족하는 필터
    # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test")', reverse=True, limit=5):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 둘 중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test")', reverse=True, limit=5):
        print("[{}] {}".format(msg.from_, msg.subject))