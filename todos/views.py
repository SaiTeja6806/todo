from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')