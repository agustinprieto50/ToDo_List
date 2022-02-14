from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from sympy import true


# class Project(models.Model):

#     title = models.CharField(max_length=500)
#     isCompleted = models.BooleanField(default=False)
#     dueDate = models.DateTimeField(auto_now_add=True)


class Task(models.Model):

    name = models.CharField(max_length=500)
    isCompleted = models.BooleanField(default=False)
    dueDate = models.DateTimeField(auto_now_add=True)
#   projectPk = models.ForeignKey(Project, on_delete=CASCADE, null=True)