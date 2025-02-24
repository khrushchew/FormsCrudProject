from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from forms_crud.forms import UserForm
from forms_crud.models import Person


class IndexView(View):
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        persons = Person.objects.all()
        return render(request, 'index.html', {'form': form, 'persons': persons})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        persons = Person.objects.all()
        return render(request, 'index.html', {'form': form, 'persons': persons})
    
