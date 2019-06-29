from django.db import models
from faker import Faker

fake = Faker('ko_kr')

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=40)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student.name}가 {self.lecture.name}을(를) 수강 중입니다."


# 리조트 예약
class Client(models.Model):
    name = models.CharField(max_length=746)
    
    @classmethod
    def dummy(cls, n): # 자기 자신(클래스, not 인스턴스)과 인자
        for i in range(n):
            cls.objects.create(name=fake.name()) # Client.objects.create()와 같다
            
    def __str__(self):
        return self.name
        
    
class Resort(models.Model):
    name = models.CharField(max_length=746)
    clients = models.ManyToManyField(Client, related_name="resorts") # M:N
    
    def __str__(self):
        return self.name

