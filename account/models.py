from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
    
# Create your models here.
class User(AbstractUser):
    Is_Author = models.BooleanField(default=False)
    Special_User = models.DateTimeField(default=timezone.now())


    def is_special_user(self):
        if self.Special_User > timezone.now():
            return True
        else:
            return False