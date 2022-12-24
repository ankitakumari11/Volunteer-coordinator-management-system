from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class IsCoord(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default="")
    cname = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=30, default="")
    gender = models.CharField(max_length=10, default="")
    activity = models.CharField(max_length=30, default="")
    dept = models.CharField(max_length=20, default="")
    academic_year = models.CharField(max_length=10, default="")
    module = models.CharField(max_length=20, default="")
    div = models.CharField(max_length=10, default="")
    current_add = models.CharField(max_length=100, default="")
    prn = models.BigIntegerField(default=000000)
    roll = models.BigIntegerField(default=0)
    contact_num = models.FloatField(default=0000000000)

    def __str__(self):
        return self.cname


class RequestFrom(models.Model):
    vname = models.CharField(max_length=20)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class vdata(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default="")
    Name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=10)
    activity = models.CharField(max_length=30)
    dept = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=10)
    module = models.CharField(max_length=20)
    div = models.CharField(max_length=10)
    current_add = models.CharField(max_length=100)
    prn = models.BigIntegerField()
    roll = models.BigIntegerField()
    contact_num = models.FloatField()
    verified = models.BooleanField(default=False)
    submitted = models.BooleanField(default=False)
    Objective_of_the_Activity = models.CharField(max_length=200, default="")
    Description_of_the_Activity = models.CharField(max_length=200, default="")
    Benefits_to_Society = models.CharField(max_length=200, default="")
    Benefits_to_Self = models.CharField(max_length=200, default="")
    Learning_Experiences_challenges = models.CharField(
        max_length=200, default="")
    How_did_it_help_you_to_shape_your_Empathy = models.CharField(
        max_length=200, default="")
    url = models.URLField(
        max_length=200, default="")
    Cordinator = models.CharField(max_length=40, default="")

    def _str_(self):
        return self.Name
