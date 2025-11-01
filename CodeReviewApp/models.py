from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, null=False, unique=True)
    password = models.CharField(max_length=40, null=False, unique=True)

class CodeReview(models.Model):
    language = models.CharField(max_length=40, null=False, unique=False)
    description = models.CharField(max_length=200, null=True, unique=False)
    code = models.TextField(null=False, unique=False)