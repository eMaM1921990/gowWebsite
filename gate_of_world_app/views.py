from django.http.response import HttpResponse
from django.shortcuts import render
from Feed import *
# Create your views here.

def TestParse(request):
    feed=Feed()
    feed.feedParser()
    return HttpResponse(None)
