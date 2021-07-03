""" My first views with django"""
# django
from django.http import HttpResponse

# utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'The time server is {now}')

