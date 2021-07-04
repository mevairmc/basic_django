""" My first views with django"""
# django
from django.http import HttpResponse

# utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'The time server is {now}')


def hi(request):
    print(request.GET.get('numbers'))
    print(request.GET.getlist('numbers'))
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers_sorted = sorted(numbers)
    response = {
        'status': 'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted successfully!!!'
    }
    return HttpResponse(
        json.dumps(response, indent=4),
        content_type="application/json"
    )


def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, Welcome to Django'
    return HttpResponse(message)
