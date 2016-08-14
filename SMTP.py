# -*- coding: cp949 -*-

import mimetypes
import smtplib

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from datetime import datetime

#global value

host ="smtp.gmail.com"
port="587"
#htmlFilename=""

senderAddr="bookinpeople@gmail.com"
recipientAddr = "hobbes1520@gmail.com"

msg = MIMEBase("multipart","alternative")
msg = MIMEText("this is auto mailing test.")
msg['subject'] = "now i'm debugging2"
msg['from'] = senderAddr
msg['to'] = recipientAddr

#create MIME document
#htmlFD = open(htmlFileName, 'rb')
#htmlpart = MIMEText(htmlFD,read(),'html'_charset = 'UTF-8')
#htmlFD.close()

#attach to MIMEBase
#msg.attach(HtmlPart)

#sending mail
min=input('please tell me want min:')

RSV=datetime(2016,8,14,23,int(min),0)
CurS=0

s = smtplib.SMTP(host,port)
s.ehlo()
s.starttls()
s.ehlo()
s.login("bookinpeople@gmail.com", "book160218")
while CurS==0:
    if((RSV.day==datetime.now().day)&(RSV.hour==datetime.now().hour)&(RSV.minute==datetime.now().minute)&(RSV.second==datetime.now().second)):
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        print("i'm send the mail. thank you")
        s.close()
        CurS=1
    else:
        pass