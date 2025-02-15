from django.http import HttpResponseRedirect
from django.views import View

from forms_crud.models import Person


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        model = Person.objects.get(pk=pk)
        model.delete()
        return HttpResponseRedirect('/')
