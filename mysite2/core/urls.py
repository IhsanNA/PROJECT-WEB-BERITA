from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('isi/<int:id>',views.isi, name='isi'),
]