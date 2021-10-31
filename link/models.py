from django.db import models
from django.utils import timezone
# Create your models here.
class StoreUrlDate(models.Model):
    link=models.CharField(max_length=1000)
    uuid=models.CharField(max_length=10)
    currentdate=models.DateField(default=timezone.now)

class IpAddress(models.Model):
    user_ip=models.TextField(default=None)
    def __str__(self):
        return self.user_ip