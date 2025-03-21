from django.shortcuts import render, redirect  
# Importing 'render' to render templates (HTML pages)  
# Importing 'redirect' to redirect users to a different page  

from django.http import HttpResponse  
# Importing HttpResponse, though it's not used here. It can be used to return plain text responses  

from .models import Task  
# Importing the Task model to interact with the database  


def home(request):
    """
    View function to display the home page with all tasks.
    """
    tasks = Task.objects.all()  
    # Fetching all task records from the database  

    return render(request, 'index.html', {'tasks': tasks})  
    # Rendering 'index.html' and passing the tasks as context data  


def add_task(request):
    """
    View function to handle adding a new task.
    """
    if request.method == 'POST':  
        # Checking if the request method is POST (i.e., form submission)  

        title = request.POST['title']  
        # Retrieving the 'title' input from the form  

        Task.objects.create(title=title)  
        # Creating a new task record in the database  

    return redirect('home')  
    # Redirecting back to the home page after adding the task  


def delete_task(request, task_id):
    """
    View function to delete a task.
    """
    task = Task.objects.get(id=task_id)  
    # Fetching the task object with the given task_id from the database  

    task.delete()  
    # Deleting the task  

    return redirect('home')  
    # Redirecting back to the home page after deletion  


def complete_task(request, task_id):
    """
    View function to mark a task as completed.
    """
    task = Task.objects.get(id=task_id)  
    # Fetching the task object with the given task_id from the database  

    task.completed = True  
    # Updating the 'completed' field to True  

    task.save()  
    # Saving the updated task in the database  

    return redirect('home')  
    # Redirecting back to the home page after updating the task  
