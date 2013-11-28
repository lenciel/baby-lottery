#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
#from .models import LeaveMessage

#from utils import send_email

#FIXME: use ajax json response, also do proper validate on html form

#
#def send_message(request):
#    name = request.POST.get('name', None)
#    phone = request.POST.get('phone', None)
#    message = request.POST.get('message', None)
#    interests = u'感兴趣领域:'
#    if request.POST.get('is_interest_enterprise', 'false') == 'true':
#        interests+=u' 企业业务'
#    if request.POST.get('is_interest_agent', 'false') == 'true':
#        interests+=u' 代理商业务'
#    if request.POST.get('is_interest_provider', 'false') == 'true':
#        interests+=u' 服务商业务'
#
#    mail_subject = u'应用工厂客户联系'
#    mail_content = u'有客户提交了联系方式:<br>姓名：%s <br> 联系方式: %s <br> 留言:%s <br> %s <br> 请速联系!' % (name, phone, message, interests);
#
#    send_email(mail_subject, mail_content)
#
#    #leave_message = LeaveMessage.objects.create(name=name, phone=phone, message=message, interests=','.join(interests))
#    #leave_message.save()
#    return HttpResponse()