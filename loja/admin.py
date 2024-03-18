from django.contrib import admin

from .models import * 
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)