from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chimp, Slingshot
from .forms import ShiftForm

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
    slingshots_chimp_doesnt_carry = Slingshot.objects.exclude(id__in = chimp.slingshots.all().values_list('id'))
    shift_form = ShiftForm()
    return render(request, 'chimps/detail.html', { 'chimp': chimp, 
        'shift_form': shift_form,  'slingshots': slingshots_chimp_doesnt_carry
        })

def add_shift(request, chimp_id):
    form = ShiftForm(request.POST)
    if form.is_valid():
        new_shift = form.save(commit=False)
        new_shift.chimp_id = chimp_id
        new_shift.save()
    return redirect('detail', chimp_id=chimp_id)

def assoc_slingshot(request, chimp_id, slingshot_id):
    Chimp.objects.get(id=chimp_id).slingshots.add(slingshot_id)
    return redirect('detail', chimp_id=chimp_id)

def unassoc_shlingshot(request, chimp_id, slingshot_id):
    Chimp.objects.get(id=chimp_id).slingshots.remove(slingshot_id)
    return redirect('detail', chimp_id=chimp_id)

class SlingshotList(ListView):
    model = Slingshot

class SlingshotDetail(DetailView):
    model = Slingshot

class SlingshotCreate(CreateView):
    model = Slingshot
    fields = '__all__'

class SlingshotUpdate(UpdateView):
    model = Slingshot
    fields = ['name','color','ammo']

class SlingshotDelete(DeleteView):
    model = Slingshot
    success_url = '/slingshots/'
