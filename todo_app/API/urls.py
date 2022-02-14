
from django.urls import path
from . import views

urlpatterns = [
    path('tasklist/', views.taskList, name='tasklist'),
    path('createtask/', views.createTask, name='createtask'),
    # path('projectlist/', views.projectList, name='projectlist'),
    # path('createproject/', views.createProject, name='createproject'),
    # path('editproject/<pk>/', views.editProject, name='editproject'),
    path('edittask/<pk>/', views.editTask, name='edittask'),
    path('deletetask/<pk>/', views.deleteTask, name='deletetask'),
    # path('deleteproject/<pk>/', views.deleteProject, name='deleteproject'),
    path('completedlist/', views.completedTaskList, name='completedlist'),

]

