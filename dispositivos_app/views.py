from django.shortcuts import render
from django.shortcuts import render
from .models import Dispositivo
from .forms import DispositivoForm, DocumentoForm
from django.shortcuts import render, get_object_or_404, redirect

def visualizar_dispositivos(request):
    txt_nome = request.GET.get('nome')
    if txt_nome:
        dispositivos = Dispositivo.objects.filter(numero_de_serie__icontains=txt_nome)
    else:
        dispositivos = Dispositivo.objects.all()
    return render(request, 'visualizar_dispositivos.html', {'dispositivos': dispositivos})

def editar_dispositivos(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, pk=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST, request.FILES, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('visualizar_dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, 'editar_dispositivos.html', {'form': form})

def adicionar_documento(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, pk=dispositivo_id)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.dispositivo = dispositivo
            documento.save()
            return redirect('visualizar_dispositivos')
    else:
        form = DocumentoForm()
    return render(request, 'adicionar_documento.html', {'form': form})