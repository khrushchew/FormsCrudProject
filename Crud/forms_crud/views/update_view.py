from django.views import View
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms_crud.forms import UserForm
from forms_crud.models import Person

class UpdateView(View):
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        model = Person.objects.get(pk=pk)
        form = self.form_class(model_to_dict(model))
        return render(request, 'retrieve.html', {'form': form, 'pk': pk})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        model = Person.objects.get(pk=pk)
        form = self.form_class(data=request.POST, instance=model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    