from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.urls import reverse
# Create your views here.

# def user_login(request):
#     context = {}
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             if request.GET.get('next', None):
#                 return HttpResponseRedirect(request.GET['next'])
#             return HttpResponseRedirect(reverse('employee_list'))
#         else:
#             context["error"] = "Provide valid credentials !!"
#             return render(request, "auth/login.html", context)


def todoshka(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'main/index.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    
    task.delete()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'main/update.html', context)



def delete(request, pk):
    task = Task.objects.get(id = pk) 

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {
        'task': task
    }
    return render(request, 'main/delete.html', context)