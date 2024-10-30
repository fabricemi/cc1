from django.urls import path
from collec_management import views
from .views import CollecDetailView

urlpatterns = [
    path('collection/<int:pk>/', CollecDetailView.as_view(), name='collec_detail'),
    path('new/', views.new_collection, name='new_collection')
]