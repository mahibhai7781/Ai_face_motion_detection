from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detect', views.detection, name='detection'),
    path('Register', views.Register, name="Register"),
    path('About', views.About, name='About'),
    path('faceDet', views.faceDet, name="faceDet"),
    path('imotionDetection', views.imotionDetection, name="imotionDetection"),
    path('VideoImotionDetect', views.VideoImotionDetect, name="VideoImotionDetect"),
    path('input',views.input),
    path('sign_up',views.SignUp),
    path('picAdd',views.addPicture),
]