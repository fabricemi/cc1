from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CollecForm  
from .models import Collec 

def attr_class(form):
    """attribut au champ input la casse 'form-control'"""
    for f in form.fields.keys():
        form.fields[f].widget.attrs.update({
            "class":"form-control"
        })

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


def delete_collection(request, id):
    collec_filter = Collec.objects.filter(id=id)
    if not collec_filter.exists():
        return render(request, "not_found.html")
    
    collection = collec_filter[0]
    
    if request.method == 'POST':
        collection.delete()
        return redirect('collection_list')
    
    return render(request, 'collec_confirm_delete.html', {'collection': collection})
