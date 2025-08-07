from multiprocessing.managers import BaseManager
from django.shortcuts import render
from .models import Student



def homepage(request):
    Students : BaseManager[Student] = Student.objects.all()

    context_data : dict[str, BaseManager[Student]] = {
        'student_info': Students
    }

    return render(request, 'homepage.html', context_data)