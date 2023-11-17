from django.db import models
from news import models as mdl

# Create your models here.

class beritaupdate1(models.Model):
    STATUS = ('publish', 'publish'),('draft', 'draft') 

    judul = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255, null=True)
    isi = models.CharField(max_length=9999)
    kategori = models.ForeignKey(mdl.categories,on_delete=models.CASCADE)
    kategoriID = models.IntegerField(max_length=255, null=True)
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    penulis = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=200, null=True)