from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class User(AbstractUser):
    objects = UserManager()
    def __str__(self):
        return self.username

