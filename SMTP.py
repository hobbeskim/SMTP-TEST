# -*- coding: cp949 -*-

import mimetypes
import smtplib

from email.mime.base import MIMEBase
from email.mime.text import MIMEText


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
#god tham crazy git
#fuckkkkkkkk!!!
#sending mail
s = smtplib.SMTP(host,port)
s.ehlo()
s.starttls()
s.ehlo()
s.login("bookinpeople@gmail.com","book160218")
i = 0

## this is real
#while i<2:
s.sendmail(senderAddr, [recipientAddr], msg.as_string())
#   i=i+1
s.close()
