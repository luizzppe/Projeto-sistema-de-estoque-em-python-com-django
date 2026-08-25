from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path("", views.index, name="index"),
    # URLs para Produtos
    path("produtos/", views.produto_list, name="produto_list"),
    path("produtos/novo/", views.produto_create, name="produto_create"),
    path("produtos/<int:pk>/", views.produto_detail, name="produto_detail"),
    path("produtos/<int:pk>/editar/", views.produto_update, name="produto_update"),
    path("produtos/<int:pk>/excluir/", views.produto_delete, name="produto_delete"),

    # URLs para Categorias
    path("categorias/", views.categoria_list, name="categoria_list"),
    path("categorias/novo/", views.categoria_create, name="categoria_create"),
    path("categorias/<int:pk>/editar/", views.categoria_update, name="categoria_update"),
    path("categorias/<int:pk>/excluir/", views.categoria_delete, name="categoria_delete"),

    # URLs para Tags
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/novo/", views.tag_create, name="tag_create"),
    path("tags/<int:pk>/editar/", views.tag_update, name="tag_update"),
    path("tags/<int:pk>/excluir/", views.tag_delete, name="tag_delete"),
]
