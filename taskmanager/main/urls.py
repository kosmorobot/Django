from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('ksushon', views.ksushon, name='ksushon'),
    path('lexa', views.lexa, name='lexa'),
    path('mashka', views.mashka, name='mashka'),
    path('jun', views.jun, name='jun'),

]
