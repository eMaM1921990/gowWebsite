from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from django.template import RequestContext
from requestHandler import *


def home(request):
    context={}
    template='base/basePage.html'
    requestHandle=RequestHandler()
    context=requestHandle.get_main_content()
    return render_to_response(template,context,context_instance=RequestContext(request))

