from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name='pyth'
urlpatterns = [
       path('', views.IndexView.as_view(), name='index'),
    path('index/', views.say_hello),

    path('join/', views.join, name='join'),
      
    





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


