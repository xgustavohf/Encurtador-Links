from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
import hashlib

def index(request):
    link_anterior = request.session.get('link_anterior', None)
    return render(request, 'shortener/index.html', {'link_anterior': link_anterior})

def encurtar(request):
    if request.method == 'POST':
        url_original = request.POST.get('url', '')
        codigo_hash = hashlib.sha256(url_original.encode()).hexdigest()[:8]

       
        request.session['link_anterior'] = url_original

        Link.objects.create(original_url=url_original, short_code=codigo_hash)

        return render(request, 'shortener/index.html', {'link_anterior': url_original, 'link_encurtado': codigo_hash})
    else:
        return redirect('index')

def redirecionar(request, codigo_hash):
    try:
        link = Link.objects.filter(short_code=codigo_hash).first()
        if link:
            return redirect(link.original_url)
        else:
            return render(request, 'shortener/link_nao_encontrado.html')
    except MultipleObjectsReturned:

        link = Link.objects.filter(short_code=codigo_hash).first()
        return redirect(link.original_url)
    except Link.DoesNotExist:
        return render(request, 'shortener/link_nao_encontrado.html')
