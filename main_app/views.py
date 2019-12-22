from django.shortcuts import render

# Create your views here.

class Chimp:
    def __init__(self, name, weight, description, age):
        self.name = name
        self.weight = weight
        self.description = description
        self.age = age

chimps = [
    Chimp('Lolo', 250, 'foul little demon', 3),
    Chimp('Sachi', 210, 'One eyed sniper', 9),
    Chimp('Raven', 217, 'Vicious hand to tusk combat specialist', 3)
]

def home(request):
    return render(request, 'home.html/')

def about(request):
    return render(request, 'about.html')

def chimps_index(request):
    return render(request, 'chimps/index.html', { 'chimps': chimps })