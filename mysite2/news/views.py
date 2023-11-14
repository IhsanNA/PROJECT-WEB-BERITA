from django.shortcuts import render
from . import models
# Create your views here.

def all(request):
        berita = models.berita.objects.all()
        context = {'beritas' : berita}
        return render(request, 'menu/all.html',context)

def trending(request):
    return render(request, 'menu/trending.html')

def politik(request):
    return render(request, 'menu/politik.html')

def olahraga(request):
    return render(request, 'menu/olahraga.html')

def kesehatan(request):
    return render(request, 'menu/kesehatan.html')

def gayahidup(request):
    return render(request, 'menu/gayahidup.html')

def entertaimen(request):
    return render(request, 'menu/entertaimen.html')

