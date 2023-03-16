from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name='pyth'
urlpatterns = [
  
    path('', views.say_hello, name='home'),

    path('join/', views.join, name='join'),
    
   
    path('join/', views.join, name='second'),
      
    





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


