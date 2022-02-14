from asyncio import tasks
from re import S
from django.shortcuts import render
from .serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def completedTaskList(request):
    tasks = Task.objects.filter(isCompleted=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def editTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()    
    return Response("Task succesfully deleted!")



# @api_view(['DELETE'])
# def deleteProject(request, pk):
#     project = Project.objects.get(pk=pk)
#     project.delete()
#     return Response("Project succesfully deleted!")

# @api_view(['GET'])
# def projectList(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def editProject(request, pk):
#     task = Project.objects.get(id=pk)
#     serializer = ProjectSerializer(instance=task ,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def createProject(request):
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def createProject(request):
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)