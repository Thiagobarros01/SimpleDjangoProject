from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Produto
def cadastrar(request):
    if request.method == "GET":
     return render(request,'cadastrar.html')
    elif request.method == "POST":
     produto = request.POST.get('produto')
     preco = request.POST.get('preco')

     prod = Produto(produto = produto, preco = preco)
     
     
     prod.save()
         
     return redirect('/produtos/cadastrar?status=1')
     
    