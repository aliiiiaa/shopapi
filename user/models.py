from django.db import models
from rest_framework.authtoken.admin import User

# Create your models here.


class ConfirmCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
