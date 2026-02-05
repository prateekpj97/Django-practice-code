from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


def home(request):
     return render(request, 'myapp/home.html') 

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'myapp/add_student.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')


@permission_required('myapp.add_student')
def add_student(request):
    ...
