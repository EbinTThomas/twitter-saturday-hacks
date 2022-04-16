from django.urls import path
from .views import index, dwnquote

urlpatterns = [
  path('', index, name='index'),
  path('dwnquote/<str:quote>', dwnquote, name='dwnquote'),
]