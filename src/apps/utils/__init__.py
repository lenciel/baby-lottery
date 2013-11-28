#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#import requests

from django.conf import settings

MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_FROM = 'service@189works.com'

#def get_latest_cases():
#    app2b_platform_case_endpoint = 'cms/samplecases/'
#    headers = {"content-type": "application/json"}
#    payload = json.dumps({"limit": 8, "include_valid_only": True})
#    cases = []
#    try:
#        url = settings.APP2B_RESTFUL_API_ROOT + app2b_platform_case_endpoint
#
#        response = requests.post(url, headers=headers, data=payload)
#        # FIXME: to prevent app2b website homepage crush.
#        if not response.ok:
#            return cases
#        raw_cases = response.json()['objects']
#        for raw_case in raw_cases:
#            case = dict()
#            case['title_image'] = raw_case['title_image']
#            case['title'] = raw_case['title']
#            case['sections'] = raw_case['sections']
#            cases.append(case)
#    except:
#        pass
#    return cases
#
#
#def send_email(subject, content):
#    server = smtplib.SMTP_SSL()
#    server.connect(MAIL_SERVER, MAIL_PORT)
#    server.login(MAIL_FROM, '189worksCOM')
#
#    mail_subject = subject
#    mail_content = content
#
#    msg = MIMEMultipart('alternative')
#    msg['Subject'] = mail_subject
#    msg['From'] = MAIL_FROM
#    msg['To'] = ', '.join(settings.MAIL_TO)
#    part = MIMEText(mail_content, 'html', 'utf-8')
#    msg.attach(part)
#
#    ret = server.sendmail(MAIL_FROM, settings.MAIL_TO, msg.as_string())
#    server.quit()
#
#    return ret
#
#
#def get_latest_articles(limit=10, scn=None):
#    app2b_platform_articles_endpoint = 'cms/articles/'
#    headers = {"content-type": "application/json"}
#    payload_dict = {"limit": limit, "include_valid_only": True}
#    if scn:
#        payload_dict['from_scn'] = scn
#    payload = json.dumps(payload_dict)
#    url = settings.APP2B_RESTFUL_API_ROOT + app2b_platform_articles_endpoint
#    cases = []
#    try:
#        response = requests.post(url, headers=headers, data=payload)
#        raw_cases = response.json()['objects']
#        for raw_case in raw_cases:
#            case = dict()
#            case['title'] = raw_case['title']
#            case['title_image'] = settings.APP2B_PLATFORM_HOST + raw_case['title_image']
#            case['summary'] = raw_case['summary']
#            article_content_url = settings.APP2B_PLATFORM_HOST + raw_case['content_url']
#            case['content'] = raw_case['content']
#            response = requests.get(article_content_url)
#            if response.ok:
#                case['html_content'] = response.text
#            case['source'] = raw_case['source']
#            for img in raw_case['images']:
#                img['url'] = settings.APP2B_PLATFORM_HOST + img['url']
#            case['images'] = raw_case['images']
#            case['published_at'] = datetime.fromtimestamp(raw_case['published_at']).strftime('%Y-%m-%d %H:%M');
#            case['scn'] = raw_case['scn']
#            cases.append(case)
#    except:
#        pass
#    return cases

