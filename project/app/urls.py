from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', UserSignupView.as_view()),
    path('login/', loginview.as_view()),
    path('profile/', Profile_View.as_view()),
    path('hello_geeks/', hello_geeks, name='hello_geeks'),
    path('userlogin', login_page, name="login_page"),  # URL for the login page template
    path('register', register_page, name="register_page"),
]
