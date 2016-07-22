from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from django.template import RequestContext
from requestHandler import *


def home(request):
    context={}
    template='home.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_main_content()
    return render_to_response(template,context,context_instance=RequestContext(request))

def categoryNews(request,slug):
    context={}
    template='list_news.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_news_pages(slug)
    return render_to_response(template,context,context_instance=RequestContext(request))

def latestNews(request):
    return None

def details(request,rss_id):
    return None