from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('all/',views.all, name='all'),
    path('trending/',views.trending, name='trending'),
    path('politik/',views.politik, name='politik'),
    path('olahraga/',views.olahraga, name='olahraga'),
    path('kesehatan/',views.kesehatan, name='kesehatan'),
    path('gayahidup/',views.gayahidup, name='gayahidup'),
    path('entertaimen/',views.entertaimen, name='entertaimen'),
    path('isi/<int:id>',views.isi, name='isi'),
]