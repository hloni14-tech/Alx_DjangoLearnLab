from django.db import models

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey('auth.user', related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)
