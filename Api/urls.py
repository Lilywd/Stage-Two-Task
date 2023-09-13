from django.urls import path

from .views import PersonViewSet

urlpatterns = [
    path('api/', PersonViewSet.as_view({'get': 'list', 'post': 'create'}), name='person_list'),
    path('api/<int:pk>/', PersonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='person_detail'),
]