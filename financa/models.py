#coding: utf-8

from django.db import models
from django.contrib import admin

PAGAMENTO = [
    ('1',u'cartão de crédito'),
    ('2',u'cheque'),
    ('3',u'dinheiro'),
    ('4',u'visa electron'),
]

TIPO = [
    ('1',u'Conta Corrente'),
    ('2',u'Cartão de Crédito'),
]

BANCO = [
    ('1',u'Santander Banespa'),
    ('2',u'Banco Real'),
]

ADMIN = [
        ('1',u'Amerian Express'),
        ('2',u'Diners'),
        ('3',u'Mastercard'),
        ('4',u'Visa'),
        ]

class Cartao(models.Model):
    referencia = models.CharField(u'referência', max_length=48)
    adm = models.IntegerField(u'Adm. de Cartão', choices = ADMIN)
    banco = models.IntegerField(u'Banco', choices = BANCO)
    limite = models.FloatField(u'Limite')
    fechto = models.IntegerField(u'dia fech. fatura', max_length=2)
    vencto = models.IntegerField(u'dia venc. fatura', max_length=2)
    class Meta:
        verbose_name = u'Cartão'
        verbose_name_plural = u'Cartões'
    def __unicode__(self):
         return u'%s' % self.referencia


class Conta(models.Model):
    nome        = models.CharField(u'nome da conta', max_length=12)
    tp_conta    = models.CharField(u'tipo da conta', max_length=24, choices = TIPO)
    nconta      = models.CharField(u'número da conta', max_length=12)
    banco       = models.CharField(u'bancos', max_length=24, choices = BANCO)
    dt_abertura = models.DateField(u'data de abertura')
    sd_inicial  = models.DecimalField(u'saldo inicial R$', max_digits=10, decimal_places=2)
    def __unicode__(self):
        return u'%s' % (self.nome)
   
class Categoria(models.Model):
    nome    = models.CharField(max_length=32)
    
    def __unicode__(self):
        return u'%s' % (self.nome)

class Lancamento(models.Model):
    dt      = models.DateField(u'data')
    hist    = models.CharField(u'histórico', max_length=64)
    categ   = models.ForeignKey('Categoria',)
    pagto   = models.CharField(u'forma de pagamento',max_length=24, choices = PAGAMENTO)
    valor = models.DecimalField(u'valor R$',max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return '%s - %s - R$ %20.2f' % (self.categ, self.hist, self.valor)

