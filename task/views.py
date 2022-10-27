from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    slack = {
        'slackUsername': 'Ayoleyi',
        'backend': True,
        'age': 22,
        'bio': 'A backend engineer in-training with a mission to build world class solutions for long-standing problems'
    }

    return JsonResponse(slack)
