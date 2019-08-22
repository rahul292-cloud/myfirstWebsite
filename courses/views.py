from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses
# Create your views here.

def index(request):
    #return HttpResponse("Hello World .")
    courses = Courses.objects

    return render(request, 'index.html' , {'courses':courses})

def detail(request, course_id):

    #print(course_id)

    course_detail = get_object_or_404(Courses,pk=course_id)

    return render(request, 'detail.html', {'course':course_detail})
