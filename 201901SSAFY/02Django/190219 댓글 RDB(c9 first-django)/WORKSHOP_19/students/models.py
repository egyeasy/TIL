from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name