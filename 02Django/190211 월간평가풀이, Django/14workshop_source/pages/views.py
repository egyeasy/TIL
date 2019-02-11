from django.shortcuts import render
import random

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
    
def student(request, name):
    age = random.choice(range(24, 30))
    return render(request, 'student.html', {'name': name, 'age': age})