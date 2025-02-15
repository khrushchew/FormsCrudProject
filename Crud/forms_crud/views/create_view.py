from django.http import HttpResponseRedirect
from django.views import View

from forms_crud.forms import UserForm


class CreateView(View):
    form_class = UserForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')
