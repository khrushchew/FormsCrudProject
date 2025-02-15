from django import forms

from forms_crud.models import Person

class UserForm(forms.ModelForm):
    name = forms.CharField(label='Name', initial='', help_text='Введите своё имя', min_length=2, max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter the name',}),)
    age = forms.IntegerField(label='Age', initial=18, help_text='Введите свой возраст', min_value=1, max_value=100)

    class Meta:
        model = Person
        fields = ('name', 'age')
