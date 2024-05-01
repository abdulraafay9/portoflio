from django.shortcuts import render

from .models import *

# Create your views here.
def home(request):
    jobs=Job.objects.all()
    context={
        'jobs':jobs
    }
    return render(request,"index.html",context)
