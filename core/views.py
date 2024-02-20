from django.shortcuts import render
from django.http import JsonResponse
import json
from .google_bard import get_response


def chatbot(request):
     return render(request,'home.html')


def google_bard_response(request):
    response=get_response(request.GET.get('prompt'))
    return JsonResponse({'message': response})

