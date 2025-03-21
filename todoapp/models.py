from django.db import models  # Importing Django's built-in models module to create database models

class Task(models.Model):  # Defining a model class 'Task' that represents a database table
    title = models.CharField(max_length=255)  # A text field to store the task title (max 255 characters)
    completed = models.BooleanField(default=False)  # A boolean field to track if the task is completed (default: False)

    def __str__(self):  # Special method to return a string representation of the model instance
        return self.title  # Returns the title of the task when printed or displayed
