from django import views
from django.urls import path, include
from .views import app_view, saveBook

app_name = 'app'

urlpatterns = [
  path('', app_view, name='app-view'),
  path('save_book/', saveBook, name='save-book'),
]
