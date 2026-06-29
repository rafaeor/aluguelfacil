# Aluguel Fácil

Plataforma para simplificar a gestão de aluguéis entre proprietários e inquilinos.

## Funcionalidades

- Proprietário cadastra imóveis e vincula inquilinos
- Inquilino visualiza o imóvel e paga aluguel via PIX
- Painel financeiro com resumo de recebimentos mensais
- Página pública para cada imóvel com fotos e valores
- Histórico de pagamentos e recibos

## Screenshots

![Painel do Proprietário](screenshot/Screenshot%20From%202026-06-29%2018-48-04.webp)

![Login](screenshot/Screenshot%20From%202026-06-29%2018-51-31.webp)

![Cadastro](screenshot/Screenshot%20From%202026-06-29%2018-52-10.webp)

![Painel do Inquilino](screenshot/Screenshot%20From%202026-06-29%2018-52-21.webp)

![Página Pública do Imóvel](screenshot/Screenshot%20From%202026-06-29%2018-52-25.webp)

## Tecnologias

- Python / Django 6.0
- PostgreSQL 17
- Docker / Docker Compose
- Tailwind CSS

## Como rodar

```bash
# 1. Clone o repositório
git clone <repo-url>
cd aluguelfacil

# 2. Configure o .env
cp .env.example .env
# Edite .env com suas configurações

# 3. Suba os containers
docker compose up -d

# 4. Execute as migrações
docker compose run --rm aluguelfacil-web python manage.py migrate

# 5. Crie o superusuário
docker compose run --rm -it aluguelfacil-web python manage.py createsuperuser
```

## Estrutura do Projeto

```
.
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── src/
│   ├── accounts/          # Autenticação e CustomUser
│   ├── core/              # Imovel, Aluguel, Pagamento
│   └── aluguelfacil/      # Configurações do Django
└── screenshot/            # Screenshots do sistema
```
