#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from django.conf import settings
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response
#from utils import get_latest_cases, get_latest_articles


def home(request):
    ga_property_id = settings.GOOGLE_ANALYTICS_PROPERTY_ID
    return render_to_response('index.html',
                              locals(),
                              context_instance=RequestContext(request))
