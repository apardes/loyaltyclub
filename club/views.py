from django.shortcuts import render
from django.shortcuts import render_to_response, render
from django.template import RequestContext
#import requests
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
	return render_to_response('club/index.html', context_instance = RequestContext(request))

def issueCredit(request):
	pass

def chargeCredit(request):
	pass

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
 
@twilio_view
def sms(request):
    r = Response()
    r.message('Hello from your Django app!')
    return r

