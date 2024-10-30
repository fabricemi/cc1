from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CollecForm  
from .models import Collec 
from django.views.generic import DetailView

class CollecDetailView(DetailView):
    model = Collec
    template_name = 'collec_detail.html'
    context_object_name = 'collection'

def about(request):
    return render(request, "about.html")


def new_collection(request):
    if request.method == 'POST':
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date_creation = timezone.now()  
            collection.save()
    else:
        form = CollecForm()
    return render(request, 'new_collection.html', {'form': form})