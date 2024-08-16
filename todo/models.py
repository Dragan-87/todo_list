import datetime
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TodoItems(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
