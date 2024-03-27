from django.shortcuts import render
from .models import Escolas
from .mapa_escolas import mapa
#from .medir import atualizar_status_escolas

def verificar(request):
     if 'mapa' in request.GET:
        mapa()
     txt_nome = request.GET.get('nome')
     if txt_nome:
          escolas = Escolas.objects.filter(nome__icontains = txt_nome)
     else:
          escolas = Escolas.objects.all()

     return render(request, 'medidor.html', {'escolas': escolas})


