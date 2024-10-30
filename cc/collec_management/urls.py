from django.urls import path
from collec_management import views

urlpatterns = [
    path('new/', views.new_collection, name='new_collection'),
]