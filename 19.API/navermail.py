import smtplib
from secret import MY_MAIL_PASSWORD, MY_MAIL_ID

smtp = smtplib.SMTP_SSL('smtp.naver.com', 455)

smtp.ehlo()
smtp.login(MY_MAIL_ID, MY_MAIL_PASSWORD)

from email.message import EmailMessage
msg = EmailMessage()

msg['Subject'] = '메일제목'
msg['FROM'] = MY_MAIL_ID
msg['To'] = MY_MAIL_ID
msg.set_content('메일본문, 멀티라인도 가능, 여기에 각자 쓰고 싶은 메세지 작성')

smtp.send_message(msg)
smtp.quit()