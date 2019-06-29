from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)
    
def detail(request, student_id):
    s = Student.objects.get(pk=student_id)
    context = {
        'student': s,
    }
    return render(request, 'detail.html', context)
    

def new(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    s = Student(name=name, email=email, birthday=birthday, age=age)
    s.save()
    
    return redirect('students:index')
    

def edit(request, student_id):
    s = Student.objects.get(pk=student_id)
    context = {
        'student': s,
    }
    return render(request, 'edit.html', context)
    

def update(request, student_id):
    s = Student.objects.get(pk=student_id)
    
    s.name = request.GET.get('name')
    s.email = request.GET.get('email')
    s.birthday = request.GET.get('birthday')
    s.age = request.GET.get('age')
    
    s.save()
    
    return redirect('students:index')
    
    
def delete(request, student_id):
    s = Student.objects.get(pk=student_id)
    s.delete()
    
    return redirect('students:index')