from django.db.models.fields.related import ForeignKey, ForeignObject
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.forms import EmpresaForm
from app.forms import ProdutoForm
from app.models import Empresa
from app.models import Produto
from django.core.paginator import Paginator


# Create your views here.
# Empresa Produto
'''
  Funções para renderização do meu template
'''
def home(request):
  # data = {'db': Carros.objects.all()}
  data = {}

  search = request.GET.get('search')
  if search:
    data['db'] = Empresa.objects.filter(nome__icontains = search)
  else:
    data['db'] = Empresa.objects.all()

  # all = Carros.objects.all()
  # paginator = Paginator(all, 5)
  # pages = request.GET.get('page')
  # data['db'] = paginator.get_page(pages)

  return render(request, 'index.html', data)

def form(request):
  data = {'form': EmpresaForm()}
  return render(request, 'form.html', data)

def create(request):
  form = EmpresaForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")
  # return render(request, 'form.html')

def view(request, pk):
  data = {'db': Empresa.objects.get(pk=pk)}
  return render(request, 'view.html', data)

def edit(request, pk):
  data = {}
  data['db'] = Empresa.objects.get(pk=pk)
  data['form'] = EmpresaForm(instance=data['db'])
  return render(request, 'form.html', data)

def update(request, pk):
  data = {}
  data['db'] = Empresa.objects.get(pk=pk)
  form = EmpresaForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")

def delete(request, pk):
  db = Empresa.objects.get(pk=pk)
  db.delete()
  return HttpResponseRedirect("/")

##
def homeProduto(request):
      # data = {'db': Carros.objects.all()}
  data = {}

  search = request.GET.get('search')
  if search:
    data['db'] = Produto.objects.filter(nomep__icontains = search)
  else:
    data['db'] = Produto.objects.all()
  
  return render(request, 'indexProduto.html', data)

def formProduto(request):
  data = {'formProduto': ProdutoForm()}
  return render(request, 'formProduto.html', data)

def createProduto(request):
  form = ProdutoForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/formProduto")
    #return render(request, 'formeProduto.html')

def viewProduto(request, pk):
  data = {'db': Produto.objects.get(pk=pk)}
  return render(request, 'viewProduto.html', data)


def filtroProduto(request, pk):
   data = {'db': Produto.objects.get(pk=pk)}
   return render(request, 'filtroProduto.html', data)


def editProduto(request, pk):
  data = {}
  data['db'] = Produto.objects.get(pk=pk)
  data['formProduto'] = ProdutoForm(instance=data['db']) ##MEXI AQUI
  return render(request, 'formProduto.html', data) ## MEXI AQUI

def updateProduto(request, pk):
  data = {}
  data['db'] = Produto.objects.get(pk=pk)
  form = ProdutoForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/indexProduto")

def deleteProduto(request, pk):
  db = Produto.objects.get(pk=pk)
  db.delete()
  return HttpResponseRedirect("/indexProduto")