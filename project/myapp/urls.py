from django.urls import path
from .views import add_nunmbers, sent_reminder

urlpatterns = [
    path('', add_nunmbers, name='add_nunmbers'),
    path('sent_reminder/', sent_reminder, name='sent_reminder'),
]