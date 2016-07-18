from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from Feed import *
# Create your views here.
from requestHandler import *


def home(request):
    context={}
    template='base/basePage.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_main_content()
    return render_to_response(template,context,context_instance=RequestContext(request))

def TestParse(request):
    feed=Feed()
    feed.feedParser()
    return HttpResponse(None)


