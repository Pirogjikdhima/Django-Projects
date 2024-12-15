from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('elements/',views.elements,name='elements'),
    path('generic/',views.generic,name='generic'),
]