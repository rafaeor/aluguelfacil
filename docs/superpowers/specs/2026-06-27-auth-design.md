# Authentication System Design

## Overview
Two-role authentication for AluguelFácil: **proprietário** (owner/landlord) and **inquilino** (tenant).

## User Model
- `accounts.CustomUser` extending Django's `AbstractUser`
- Fields: `user_type` (`proprietario` | `inquilino`)

## Registration Flows
- **Proprietário**: Created by admin via Django admin interface
- **Inquilino**: Self-registers via `/auth/cadastro/` (name, email, password)

## Auth Views
| URL | View | Purpose |
|-----|------|---------|
| `/auth/login/` | `LoginView` | Single login, redirects by `user_type` |
| `/auth/cadastro/` | `SignUpView` | Inquilino self-registration |
| `/auth/logout/` | `LogoutView` | Logout |

## App Structure
- **accounts/** — auth logic (CustomUser, login, signup, templates)
- **core/** — domain models (Imovel, Aluguel, Pagamento)

## Post-Login Redirect
- `proprietario` → `/painel/` (owner dashboard)
- `inquilino` → `/minha-casa/` (tenant dashboard)
