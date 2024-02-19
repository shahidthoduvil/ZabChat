from django.shortcuts import render
from django.http import JsonResponse
import json
from .google_bard import get_response


def chatbot(request):
     return render(request,'home.html')


def google_bard_response(request):
    response=get_response(request.GET.get('prompt'))
    return JsonResponse({'message': response})















# from openai import AsyncOpenAI
# import os
# from decouple import config
# from django.conf import settings


# api_key = config(settings.OPENAI_API_KEY)
# async def chatbot(request):
#         if request.method=='POST':
#             user_input=request.POST.get('user_input')
#             prompt=user_input
        
#             async with AsyncOpenAI(api_key=api_key) as client:
#                 response = await client.chat.completions.create(
#                       model="gpt-4-turbo-preview",
#                     messages=[
#                         {"role": "system", "content": "You are a helpful assistant."},
#                         {"role": "user", "content": user_input},
#                     ]
#                     )
#                 answer = response['choices'][0]['message']['content']
#                 print(answer)
#         return render(request,'home.html')