from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CollecForm  
from .models import Collec 
from cc.utils import attr_class

def details_collec(request, id):
    collec_filter=Collec.objects.filter(id=id)
    if not collec_filter.exists():
        return render(request, "not_found.html")
    
    collec=collec_filter[0]
    
    return render(request, "collec_detail.html", {"collection":collec})
    
    

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
    
    attr_class(form)
    return render(request, 'new_collection.html', {'form': form})


def collection_list(request):
    collections = Collec.objects.all()
    return render(request, 'collection_list.html', {'collections': collections})