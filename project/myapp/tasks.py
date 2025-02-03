from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def send_reminder():
    for i in range(10):
        print(i)
    return f"Reminder sent!"


