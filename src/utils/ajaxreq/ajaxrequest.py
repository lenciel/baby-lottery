#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json

from django.http import HttpResponse

from ..db.queryutil import get_object_or_none



logger = logging.getLogger('AjaxRequest')

class HttpResponseJson(HttpResponse):
    def __init__(self, result, request=None, **extra):
        content_type = 'application/json; charset=utf-8'
        if request:
            # e.g.
            # Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
            ua = request.META['HTTP_USER_AGENT']
            if ua and (ua.find('MSIE 8') != -1 or ua.find('MSIE 9') != -1):
                content_type = 'text/plain; charset=utf-8'

        super(HttpResponseJson, self).__init__(
            content=json.dumps(result, ensure_ascii=False),
            content_type=content_type, **extra)

