from django.urls import path
from .views import index

# Define your URL patterns here.
urlpatterns = [
    path('', index, name='index'),
]