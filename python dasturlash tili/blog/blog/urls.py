from django.contrib import admin
from django.urls import path
from news.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home-page'),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    
]
