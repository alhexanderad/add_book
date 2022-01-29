from django.urls import path, include
from .views import app_view 

app_name = 'app'

urlpatterns = [
    path('', app_view, name='app-view'),
]
