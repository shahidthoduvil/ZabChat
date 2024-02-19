from django.urls import path
from .views import *


urlpatterns = [
    path('',chatbot,name='name'),
    path('google_bard_response/',google_bard_response),

]
