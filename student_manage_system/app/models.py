from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no=models.IntegerField()
    # name=models.CharField(max_length=(25))
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    phn=models.IntegerField()

    def __str__(self):
        return self.name