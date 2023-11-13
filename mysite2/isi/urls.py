from django.urls import path
from . import views

app_name = 'isi'

urlpatterns = [
    path('isiberita',views.isi, name='isi berita'),
]