from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='undefined', help_text='Введите своё имя', min_length=2, max_length=10)
    age = forms.IntegerField(label='Ваш возраст?', initial=18, help_text='Введите свой возраст', min_value=1, max_value=100)
