from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def all(request):
    if 'cari' in request.GET:
        cari = request.GET['cari']
        berita = models.berita.objects.filter(judul__icontains=cari)
    else :
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
    catID = 2

    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/trending.html', context)

def politik(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    catID = 1
    
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/politik.html', context)

def olahraga(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    catID = 3
    
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/olahraga.html', context)

def kesehatan(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    catID = 4
    
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/kesehatan.html', context)

def gayahidup(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    catID = 5
    
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/gayahidup.html', context)

def entertaimen(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.categories.objects.all()
    catID = 4
    
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status='publish')

    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/entertaimen.html', context)

