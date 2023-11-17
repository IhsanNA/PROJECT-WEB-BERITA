from django.contrib import admin
from . models import beritaupdate1

# Register your models here.

class beritaupdate1Admin(admin.ModelAdmin):
    list_display = ['judul','isi','kategori','gambar','penulis','status','kategoriID']
    search_fields = ['judul','kategori__name']
    autocomplete_fields = ['kategori']

admin.site.register(beritaupdate1,beritaupdate1Admin)
