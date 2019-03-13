from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task, Points, Event

# Create your views here.

def index(request):
    template = loader.get_template('panel/index.html')
    context = {
        'tasks': Task.objects.all(),
        'points': Points.objects.get(id=1),
        'events': Event.objects.all()
    }
    return HttpResponse(template.render(context, request))

def add_task(request):
    title = request.POST.get("title")
    text = request.POST.get("text")
    points = request.POST.get("points")

    task = Task(title=title, text=text, completed=False, points=points)
    task.save()

    template = loader.get_template('panel/index.html')
    context = {
        'tasks': Task.objects.all(),
        'points': Points.objects.get(id=1),
        'events': Event.objects.all()
    }

    return HttpResponse(template.render(context, request))

def complete_task(request, id):
    task_id = id
    task = Task.objects.get(id=task_id)

    points = Points.objects.get(id=1)

    points.points += task.points

    points.save()

    task.delete()

    template = loader.get_template('panel/index.html')
    context = {
        'tasks': Task.objects.all(),
        'points': Points.objects.get(id=1),
        'events': Event.objects.all()
    }

    return HttpResponse(template.render(context, request))