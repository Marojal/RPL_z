
from django.contrib import admin
from .models import Formulir, UploadFile, Pendafatar

class PendafatarAdmin(admin.ModelAdmin):
    list_display = ['user', 'nama']
    list_filter = ['nama']

class FormulirAdmin(admin.ModelAdmin):
    list_display = ['pendaftar', 'nama', 'email', 'tempat_lahir', 'tanggal_lahir', 'nik', 'jenis_kelamin', 'no_hp', 'no_hp_ortu', 'alamat', 'kelurahan', 'kecamatan', 'kabupaten', 'prodi1', 'prodi2', 'prodi3','status', 'foto']
    list_filter = ["nama"]

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ['author', 'ijazah', 'kk', 'ktp', 'raport10_1', 'raport10_2', 'raport11_1', 'raport11_2', 'raport12_1']
    list_filter = ["author"]

admin.site.register(Formulir, FormulirAdmin)
admin.site.register(UploadFile, UploadFileAdmin)
admin.site.register(Pendafatar, PendafatarAdmin)