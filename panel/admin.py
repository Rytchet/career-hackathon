from django.contrib import admin
from .models import Task, Event, Points

# Register your models here.
admin.site.register(Task)
admin.site.register(Event)
admin.site.register(Points)