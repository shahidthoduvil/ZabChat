import google.generativeai as gemini
from django.conf import settings
from decouple import AutoConfig
import os


gemini.configure(api_key=settings.BARD_API_KEY)

def get_response(prompt):
    response=gemini.chat(messages=prompt)
    print(response)
    return response.last