from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from requestHandler import *

@never_cache
def home(request):
    template='home.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_main_content()
    return render_to_response(template,context,context_instance=RequestContext(request))

@never_cache
def categoryNews(request,pk):
    template='sections.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_sections(pk)
    return render_to_response(template,context,context_instance=RequestContext(request))

@never_cache
def latestNews(request):
    template='sections.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_latest_news()
    return render_to_response(template,context,context_instance=RequestContext(request))
@never_cache
def details(request,pk):
    template='article.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_article_page(pk)
    return render_to_response(template,context,context_instance=RequestContext(request))

@csrf_exempt
def getMarqueUpdates(request):
     requestHandle=RequestHandler()
     news_object=requestHandle.ListCurrentNews()
     data=serializers.serialize("json",news_object)
     return HttpResponse(data)

@never_cache
def videos_new(request):
    template='videos.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_videos_news()
    return render_to_response(template,context,context_instance=RequestContext(request))
