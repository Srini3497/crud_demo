from django.shortcuts import HttpResponse
from .models import Student
# Create your views here.
def add_ram(request):
    n = 'ram'
    e = 'ram@gmail.com'
    Student.objects.create(name=n, email=e)
    return HttpResponse('Ram Added to the Database')

def add_student(request, name, eid):
    Student.objects.create(name=name, email=eid)
    return HttpResponse(f'{name} Added to the Database')

def remove_student(request, eid):
    stud = Student.objects.get(email=eid)
    stud.delete()
    return HttpResponse('Deleted the student from Database')

