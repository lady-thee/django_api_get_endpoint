from django.urls import path 
from .views import loadAPIView

urlpatterns = [
    path("", loadAPIView, name='api')
]