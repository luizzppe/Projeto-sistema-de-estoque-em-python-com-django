from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Tag
from .forms import ProdutoForm, CategoriaForm, TagForm

def index(request):
    return render(request, "estoque/index.html")

# Views para Produtos
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, "estoque/produto_list.html", {"produtos": produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, "estoque/produto_detail.html", {"produto": produto})

def produto_create(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("estoque:produto_list")
    else:
        form = ProdutoForm()
    return render(request, "estoque/produto_form.html", {"form": form, "action": "Criar"})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("estoque:produto_list")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "estoque/produto_form.html", {"form": form, "action": "Editar"})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect("estoque:produto_list")
    return render(request, "estoque/produto_confirm_delete.html", {"produto": produto})

# Views para Categorias
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, "estoque/categoria_list.html", {"categorias": categorias})

def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estoque:categoria_list")
    else:
        form = CategoriaForm()
    return render(request, "estoque/categoria_form.html", {"form": form, "action": "Criar"})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("estoque:categoria_list")
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, "estoque/categoria_form.html", {"form": form, "action": "Editar"})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("estoque:categoria_list")
    return render(request, "estoque/categoria_confirm_delete.html", {"categoria": categoria})

# Views para Tags
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "estoque/tag_list.html", {"tags": tags})

def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estoque:tag_list")
    else:
        form = TagForm()
    return render(request, "estoque/tag_form.html", {"form": form, "action": "Criar"})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("estoque:tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "estoque/tag_form.html", {"form": form, "action": "Editar"})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("estoque:tag_list")
    return render(request, "estoque/tag_confirm_delete.html", {"tag": tag})

