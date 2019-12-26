from django.shortcuts import render
from .models import Chimp

# Create your views here.


def home(request):
    return render(request, 'home.html/')

def about(request):
    return render(request, 'about.html')

def chimps_index(request):
    chimps = Chimp.objects.all()
    return render(request, 'chimps/index.html', { 'chimps': chimps })

def chimps_detail(request, chimp_id):
    chimp = Chimp.objects.get(id=chimp_id)
    return render(request, 'chimps/detail.html', { 'chimp': chimp })