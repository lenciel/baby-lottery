#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class LeaveMessage(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=255)
    phone = models.CharField(verbose_name=u'电话', max_length=255)
    message = models.CharField(verbose_name=u'留言', max_length=2000, null=True, blank=True)
    interests = models.CharField(verbose_name=u'兴趣', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = u'合同节点'

    def __unicode__(self):
        return "%s-%s" % (self.name, self.phone)