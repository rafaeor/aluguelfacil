from django.contrib import admin
from .models import Imovel, Aluguel, Pagamento


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'proprietario', 'valor_aluguel', 'created_at')
    list_filter = ('proprietario',)


@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'inquilino', 'data_inicio', 'ativo')
    list_filter = ('ativo',)


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('aluguel', 'mes', 'ano', 'valor', 'status', 'data_pagamento')
    list_filter = ('status', 'mes', 'ano')
