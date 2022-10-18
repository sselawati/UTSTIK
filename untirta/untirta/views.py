from django.shortcuts import render
from django.db import models
from . models import Materi


# Create your views here.
def index(request):
    return render(request, 'index.html')
