from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Confirmcode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.user
