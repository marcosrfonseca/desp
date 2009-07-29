#!/usr/bin/env python
#coding: utf-8

from django.contrib import admin
from desp.financa.models import Categoria, Lancamento, Conta, Cartao

class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('categ','dt','hist','valor')
    list_display_links = list_display
    ordering = ('categ',)


admin.site.register(Categoria)
admin.site.register(Cartao)
admin.site.register(Lancamento, LancamentoAdmin)
admin.site.register(Conta)
