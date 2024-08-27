from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(null=True,max_length=20)
    age = models.CharField(default=19,max_length=3)
    nationalCode = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=11)

    Man = 1

