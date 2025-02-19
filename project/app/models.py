from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/blog.png', upload_to='profile_pics')
 
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_by = models.ManyToManyField(User, related_name="read_messages", blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
    