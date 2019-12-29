from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chimp

# Create your views here.
class  ChimpCreate(CreateView):
    model = Chimp
    fields = '__all__'
    

class ChimpUpdate(UpdateView):
    model = Chimp
    fields = ['weight', 'description', 'age']

class ChimpDelete(DeleteView):
    model = Chimp
    success_url = '/chimps/'

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

