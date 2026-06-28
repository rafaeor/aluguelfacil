# Panels Design — Proprietário & Inquilino Dashboards

## Models (core app)

### Imovel
| Field | Type | Notes |
|-------|------|-------|
| proprietario | FK → CustomUser | user_type = proprietario |
| nome | CharField | e.g. "Apto 402 - R. das Flores" |
| endereco | TextField | |
| valor_aluguel | DecimalField | |
| valor_condominio | DecimalField | nullable |
| descricao | TextField | nullable |
| quartos | IntegerField | nullable |
| vagas | IntegerField | nullable |
| area | IntegerField | nullable |
| wifi_ssid | CharField | nullable |
| wifi_senha | CharField | nullable |
| created_at | DateTimeField | auto_now_add |

### Aluguel (links inquilino to imovel)
| Field | Type | Notes |
|-------|------|-------|
| inquilino | FK → CustomUser | user_type = inquilino |
| imovel | FK → Imovel | |
| data_inicio | DateField | |
| data_fim | DateField | nullable |
| ativo | BooleanField | default=True |

### Pagamento
| Field | Type | Notes |
|-------|------|-------|
| aluguel | FK → Aluguel | |
| mes | IntegerField | 1-12 |
| ano | IntegerField | |
| valor | DecimalField | |
| data_vencimento | DateField | |
| data_pagamento | DateTimeField | nullable |
| status | CharField | choices: pendente / pago |

Auto-generated each month per active Aluguel.

## Panels

### Proprietário `/painel/`
- Card: total recebido no mês + progresso (ex: R$ 2.500 de R$ 4.300)
- Lista de imóveis com status do inquilino (pago / pendente)
- Cada item: nome do imóvel, inquilino, valor, badge de status, botão "Cobrar" se pendente

### Inquilino `/minha-casa/`
- Card: valor do aluguel do mês, data de vencimento
- Botão "Pagar via PIX" → marca pagamento como pago com data atual
- Informações do imóvel (wifi, regras)
- Histórico de pagamentos anteriores

## Admin
- Imovel, Aluguel, Pagamento registrados no Django admin