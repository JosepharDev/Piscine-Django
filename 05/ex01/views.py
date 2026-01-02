from django.shortcuts import render
from django.http import HttpResponse
from . import models

from datetime import datetime
# Create your views here.
def  init(request):
    test = models.Movies(title='title', opening_crawl="opening_crawl", director='director', producer='producer', release_date=datetime.now())
    test.save()
    return HttpResponse("ok ex01")