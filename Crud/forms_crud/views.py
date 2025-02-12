from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Person

from .forms import UserForm


# Create your views here.
def index(request):
    form = UserForm()
    persons = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'persons': persons})

def create(request):
    if request.method == 'POST':
        Person.objects.create(name=request.POST.get('name'), age=request.POST.get('age'))
        return HttpResponseRedirect('/')
