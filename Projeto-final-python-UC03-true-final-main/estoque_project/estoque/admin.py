from django.contrib import admin
from .models import Categoria, Tag, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "quantidade", "preco", "display_tags")
    list_filter = ("categoria", "tags")
    search_fields = ("nome", "descricao")
    raw_id_fields = ("categoria",)
    filter_horizontal = (
        "tags",
    )

    def display_tags(self, obj):
        return ", ".join([tag.nome for tag in obj.tags.all()])

    display_tags.short_description = "Tags"

