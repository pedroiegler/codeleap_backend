from django.urls import path
from .views import CareerListCreateView, CareerRetrieveUpdateDestroyView

urlpatterns = [
    path('careers/', CareerListCreateView.as_view(), name='career-list-create'),
    path('careers/<int:pk>/', CareerRetrieveUpdateDestroyView.as_view(), name='careers_detail'),
]
