from django.contrib import admin
from . models import Customuser,berita, categories
# Register your models s

admin.site.register(Customuser)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ['namaKategori']
    search_fields = ['namaKategori']

admin.site.register(categories,categoriesAdmin)

class beritaAdmin(admin.ModelAdmin):
    list_display = ['judul','isi','kategori','gambar','penulis','status','kategoriID']
    search_fields = ['judul','kategori__name']
    autocomplete_fields = ['kategori']

admin.site.register(berita,beritaAdmin)
