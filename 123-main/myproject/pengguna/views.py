from django.shortcuts import render,redirect,get_object_or_404 # type: ignore

from pengguna.models import Formulir
from pengguna.forms import FormulirForm
from pengguna.forms import UploadForm
import logging

# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)

    
def formulir_detail(request, pk):
    formulir = get_object_or_404(Formulir, pk=pk)
    context = {
        'formulir': formulir,
        'title': 'Detail Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_detail.html', context)


logger = logging.getLogger(__name__)

def create_formulir(request):
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            formulir=form.save()
            logger.info("Formulir berhasil disimpan")
            return redirect('formulir_detail',pk=formulir.pk)
        else:
            logger.error("Formulir tidak valid: %s", form.errors)
    else:
        form = FormulirForm()
    return render(request, 'dashboard/snippets/formulir.html', {'form': form, 'title': 'Create Formulir'})

def add_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            add_form = form.save()
            return redirect('/upload/file', pk=add_form.pk) 
    else:
        form = UploadForm()

    context = {
        'form': form,  # Mengirimkan form dengan nama 'form'
        'title': 'Upload Berkas'
    }

    return render(request, 'dashboard/snippets/upload-file.html', context)


def formulir_list(request):
    formulirs = Formulir.objects.all()
    context = {
        'formulirs': formulirs,
        'title': 'Daftar Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_list.html', context)

def upload_file_view(request):
    form = UploadForm()
    is_operator = request.user.groups.filter(name='operator').exists()
    return render(request, 'dashboard/snippets/formulir.html', {'form': form, 'is_operator': is_operator})

def file_detail(request, pk):
    file = get_object_or_404(Formulir, pk=pk)
    context = {
        'formulir': file,
        'title': 'Detail Formulir',
    }
    return render(request, 'dashboard/snippets/up_file.html', context)

def file_list(request):
    files = Formulir.objects.all()
    context = {
        'files': files,
        'title': 'Daftar Berkas',
    }
    return render(request, 'dashboard/snippets/file_list.html', context)