from django.shortcuts import render
from django.views.generic import(TemplateView,DetailView,ListView,FormView)
from .models import Standard,Subject,Lesson
# Create your views here.
class StandardListView(ListView):
    context_object_name='standards'
    model=Standard
    template_name='classes/standard_list_view.html'