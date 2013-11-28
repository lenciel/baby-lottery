#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings

MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_TO = ['lenciel@qq.com']

def send_email(subject, content):
    server = smtplib.SMTP_SSL()
    server.connect(MAIL_SERVER, MAIL_PORT)
    server.login(settings.MAIL_FROM, 'Welcome1')

    mail_subject = subject
    mail_content = content

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = settings.MAIL_FROM
    msg['To'] = ', '.join(MAIL_TO)
    part = MIMEText(mail_content, 'html', 'utf-8')
    msg.attach(part)
    ret = []

    try:
        ret = server.sendmail(settings.MAIL_FROM, MAIL_TO, msg.as_string())
    except:
        pass
    server.quit()
    return ret

def gen_random_string(size=7):
    """
    产生随机的字符串。

    参数
    size: 目标随机字符串的长度，默认7。 62^7 = 3521614606208 足够大。

    该算法虽然简单，但产生的key足够随机，
    在MAC OSX上的测试结果显示100万个key可能有一个冲突的。
    """
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    keys_len = 62
    key = ''
    for random in os.urandom(size):
        key += keys[ord(random) % keys_len]
    return key
