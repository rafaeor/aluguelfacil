from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date


class Imovel(models.Model):
    proprietario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='imoveis',
        limit_choices_to={'user_type': 'proprietario'},
    )
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    valor_condominio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.TextField(blank=True)
    quartos = models.IntegerField(null=True, blank=True)
    vagas = models.IntegerField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    wifi_ssid = models.CharField(max_length=100, blank=True)
    wifi_senha = models.CharField(max_length=100, blank=True)
    foto_url = models.URLField(blank=True, help_text='Link para foto do imóvel')
    foto_url = models.URLField(blank=True, help_text="Link para foto do imóvel")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    inquilino = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='alugueis',
        limit_choices_to={'user_type': 'inquilino'},
    )
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='alugueis')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.imovel.nome} - {self.inquilino.username}'


class Pagamento(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        PAGO = 'pago', 'Pago'

    aluguel = models.ForeignKey(Aluguel, on_delete=models.CASCADE, related_name='pagamentos')
    mes = models.IntegerField()
    ano = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)

    class Meta:
        unique_together = ('aluguel', 'mes', 'ano')

    def __str__(self):
        return f'{self.aluguel.imovel.nome} - {self.mes}/{self.ano}'
