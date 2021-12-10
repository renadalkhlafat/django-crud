from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
)
# Create your views here.


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'details_list.html'
    model = Snack
    context_object_name = 'snack_detail'


class SnackCreateView(CreateView):
    template_name = 'create_snack.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']


class SnackDeleteView(DeleteView):
    template_name = 'delete_snack.html'
    model = Snack
    success_url = reverse_lazy('snacks')

class SnackUpdateView(UpdateView):
    template_name = 'update_snack.html'
    model = Snack
    fields = ['title', 'description']
