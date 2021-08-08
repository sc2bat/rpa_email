# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#         ex) ㅇㅇㅇ/1234

# 메일 가져오기
from account import *
from imap_tools import MailBox

# 가져온 정보를 리스트화
applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 25-Dec-2020)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            # 리스트
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# 리스트 정보 확인
# for applicant in applicant_list:
    # print(applicant)