#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from utils import send_email, gen_random_string
from utils.db.queryutil import get_object_or_none
from utils.ajaxreq.ajaxrequest import HttpResponseJson
from utils.ajaxreq.response_codes import get_response_code


def send_greeting(request):
    email = request.POST.get('email', None)
    from .models import Greeting
    greeting = get_object_or_none(Greeting, email=email)
    if greeting:
        return HttpResponseJson(get_response_code('email_already_used'), request)

    else:
        name = request.POST.get('name', None)
        gender = request.POST.get('gender', None)
        message = request.POST.get('message', None)
        lottery_code = gen_random_string()

        mail_subject = u'Lenceel&Lenciel代表我们的宝宝向您表示感谢!'
        mail_content =  u'Hi, %s, <br/><br/> 感谢您的参与。<br/> 您的联系方式: %s <br/> 您的幸运码:%s <br/> 如果中奖的是您，我们会尽快和您联系!<br/><br/>Thanks for participate.<br/> Your email: %s <br/> Your lucky code:%s <br/> We will get back to you if you are the lucky one, thanks again.<br/><br/>' % (name, email, lottery_code, email, lottery_code);

        send_email(mail_subject, mail_content, email)

        Greeting = Greeting.objects.create(name=name, gender=gender, email=email, message=message, lottery_code=lottery_code)
        Greeting.save()

    return HttpResponseJson(get_response_code('success'), request)


def result(request):
    return render_to_response('greeting/result.html',
                              locals(),
                              context_instance=RequestContext(request))