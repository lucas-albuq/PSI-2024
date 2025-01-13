from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def create_carrinhoitem_view(request, produto_id=None):
    print ('create_carrinhoitem_view')
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto:
        print('produto: ' + str(produto.id))

    carrinho_id = request.session.get('carrinho_id')
    print ('carrinho: ' + str(carrinho_id))
    carrinho = None

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print (carrinho)
        print ('carrinho1: ' + str(carrinho.id))
        hoje = datetime.today().date()
        if carrinho.criado_em.date() != hoje:
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
            print ('novo carrinho: ' + str(carrinho.id))
    else:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id
        print ('carrinho2: ' + str(carrinho.id))

    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()

    if carrinho_item:
        carrinho_item.quantidade += 1
        print ('item de carrinho: Acrescentou 1 item do produto ' +
        str(carrinho_item.id))
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print ('item de carrinho: Acrescentou o produto ' + str(carrinho_item.id))

    carrinho_item.save()
    print ('item de carrinho salvo: ' + str(carrinho_item.id))
    return redirect('/carrinho')

def list_carrinho_view(request):
    print ('list_carrinho_view')
    carrinho = None
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id:
        print ('carrinho: ' + str(carrinho_id))
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print ('Data do carrinho' + str(carrinho.criado_em) )
        carrinho_item = None
        carrinho_item = CarrinhoItem.objects.filter(carrinho_id=carrinho_id)
        if carrinho_item:
            print ('itens de carrinho encontrado: ' + str(carrinho_item))

    context = {
        'carrinho': carrinho,
        'itens': carrinho_item
    }

    return render(request, 'carrinho/carrinho-listar.html', context=context)

def confirmar_carrinho_view(request):
    print ('confirmar_carrinho_view')
    carrinho = None
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id:
        print ('carrinho: ' + str(carrinho_id))
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        usuario = get_object_or_404(Usuario, user=request.user)
        print ('Usuario: ' + str(usuario))

        if usuario:
            carrinho.user_id = usuario.id
            carrinho.situacao = 1
            carrinho.confirmado_em = timezone.make_aware(datetime.today())
            carrinho.save()
            print ('carrinho salvo')

    context = {
        'carrinho': carrinho
    }
    return render(request, 'carrinho/carrinho-confirmado.html', context=context)

def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id == item.carrinho.id:
        item.delete()
        
    return redirect('/carrinho')