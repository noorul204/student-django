from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)  # 0 to 100

    def __str__(self):
        return self.name
