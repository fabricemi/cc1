from django.urls import path
from . import views


urlpatterns = [
    path('collection/<int:id>/', views.details_collec, name='collec_detail'),
    path('new/', views.new_collection, name='new_collection'),
    path('all/', views.collection_list, name='collection_list'),
]