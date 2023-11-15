from django.shortcuts import render, get_object_or_404, catID
from . import models, catID
# Create your views here.

def all(request):
        berita = models.berita.objects.all()
        context = {'beritas' : berita}
        return render(request, 'menu/all.html', context)

def isi(request, id):
        berita = get_object_or_404(models.berita, pk=id)
        context = {'beritas' : berita}
        return render(request, 'menu/isiberita.html', context)

def trending(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/trending.html', context)

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

