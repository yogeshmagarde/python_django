from django.shortcuts import HttpResponse
from myapp.tasks import add, send_reminder

def add_nunmbers(request):
    result = add.delay(2, 13)
    result_apply_async = add.apply_async((2, 3), countdown=5)
    return HttpResponse(f"{result} done {result_apply_async}")


def sent_reminder(request):
    result = send_reminder.delay()  # Call Celery task asynchronously
    return HttpResponse(f"Reminder task started! Task ID: {result.id}")