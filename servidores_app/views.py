from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

@has_permission_decorator('ver_usuario')
def visualizar_usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        # Verifica se o formulário de exclusão foi enviado
        if 'excluir_usuario_id' in request.POST:
            usuario_id = request.POST['excluir_usuario_id']
            usuario = get_object_or_404(Usuario, pk=usuario_id)
            usuario.delete()
            return redirect('visualizar_usuarios')

    context = {'usuarios': usuarios}
    return render(request, 'visualizar_usuarios.html', context)


def cadastrar_usuarios(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            isinstance = form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('cadastrar_usuarios')  
    else:
        form = UsuarioForm()
    return render (request,'cadastrar_usuarios.html', {'form': form})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário editado com sucesso.')
            return redirect('editar_usuario', usuario_id=usuario_id)
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form})

def criar_usuario (request):
    user = User.objects.create_user(username="teste",password="1234")
    user.save
    assign_role(user,'gerente')
    return HttpResponse('Usuário cadastrado com sucesso')