#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Bb

def index(request):
    s = 'Список оголошень\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s+=bb.title + '\r\n' + bb.content +'\r\n\r\n'
    return HttpResponse(s, content_type = 'text/plain; charset= utf-8')
