from django.db import models

class project_user(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()

class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
