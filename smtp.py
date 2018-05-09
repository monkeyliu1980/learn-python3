#!/usr/bin/env python3

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email import encoders
from email.utils import parseaddr, formataddr

# tested by jiatao 
from_addr = 'monkeyliu1980@163.com'
to_addr = 'itsm@morganstanleyhuaxin.com' 
#1487584702@qq.com, Jiatao.Liu@morganstanleyhuaxin.com, itsm@morganstanleyhuaxin.com

server = smtplib.SMTP('smtp.163.com', 25)
server.set_debuglevel(1)
server.login(from_addr, 'monkeyliu1980')
msg = MIMEText('hello, \nthis is a test email sent by Python3\nfrom smtp.163.com\nat 2018/05/07','plain','utf-8')
msg['From'] = from_addr
msg['Subject'] = Header(u'Sent by Python3', 'utf-8').encode()
msg['To'] = to_addr
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
