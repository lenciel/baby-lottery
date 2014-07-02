#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Greeting(models.Model):
    gender = models.PositiveIntegerField(verbose_name=u'投注项')
    name = models.CharField(verbose_name=u'姓名', max_length=32)
    email = models.CharField(verbose_name=u'email', max_length=32)
    message = models.CharField(verbose_name=u'祝福消息', max_length=2000)
    lottery_code = models.CharField(verbose_name=u'幸运码', max_length=32)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u"创建日期")

    class Meta:
        verbose_name = u'祝福'

    def __unicode__(self):
        return "%s-%s" % (self.email, self.message)