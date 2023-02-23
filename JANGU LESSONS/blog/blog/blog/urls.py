from django.contrib import admin
from django.urls import path
from news.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home-page'),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    path('category/',category_page,name='category_page'),
    path('category_detail/<int:cat_id>/',category_detail,name='category_detail'),
    path('register/',register_page,name='register_page'),
    path('check_username/',check_username,name='check_username'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    
]+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
