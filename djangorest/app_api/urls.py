
from django.urls import path
from . import views


#from .views import pessoa_view

urlpatterns = [
    path('pessoas/', views.PessoaSerializerView)
]