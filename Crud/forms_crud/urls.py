from django.urls import path

from forms_crud.views.index_view import IndexView
from forms_crud.views.update_view import UpdateView
from forms_crud.views.delete_view import DeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("update/<int:pk>/", UpdateView.as_view()),
    path("delete/<int:pk>/", DeleteView.as_view())
]
