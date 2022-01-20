# ToDo Application using django

-Installation: <br>
pip install django <br>
pip install psycopg2  <br>
<br>

-Usage: <br>
from django.shortcuts import render, redirect <br>
from .models import * <br>
from django.http import HttpResponseRedirect <br>
from django.contrib.auth import authenticate, login <br>
from .forms import * <br>
from django.urls import reverse <br>
<br>

-Example: <br>
You just have to enter the name of the task, and below type the status of the task. <br>
It can be "Later", "Doing" or "Done". <br>
And after that when you already entered the task, you can change the status later, and also delete it. <br>
