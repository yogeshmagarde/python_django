from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', UserSignupView.as_view()),
    path('login/', loginview.as_view()),
    path('profile/', Profile_View.as_view()),
    path('hello_geeks/', hello_geeks, name='hello_geeks'),
]