from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.



class Collections(models.Model):
    title = models.CharField(max_length = 100, null = False)
    description = models.TextField()
    uuid = models.UUIDField(default = uuid4(), editable = False, primary_key = True)
    movies = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
