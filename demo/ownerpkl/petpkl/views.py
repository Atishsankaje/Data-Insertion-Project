from django.shortcuts import render
from .models import Student
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def insert_student(request):
    student = Student(
        roll_number= 1,
        name = 'ass',
        dept = 'cs',
        email = 'atish@gmail.com',
        phone = '1234567891',
    )
    student.save()
    return HttpResponse("student inserted successfully")
