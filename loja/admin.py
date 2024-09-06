from django.contrib import admin

from .models import * 

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Fabricante', 'criado_em', 'alterado_em',)
    empty_value_display = 'Vazio'
    search_fields = ('Fabricante',)

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao',
    'preco', 'categoria',)
    empty_value_display = 'Vazio'   
    fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
    

admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)
