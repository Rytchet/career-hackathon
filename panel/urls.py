from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name="add-task"),
    path('complete_task/<int:id>', views.complete_task, name="complete-task")
]