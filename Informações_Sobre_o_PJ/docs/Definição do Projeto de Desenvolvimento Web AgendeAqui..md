# Definição do Projeto — AgendeAqui

Resumo: documento que descreve o escopo, objetivos e a organização em apps do projeto "AgendeAqui" — um sistema para gerenciamento e agendamento de salas e recursos em instituições de ensino.

## 1. Informações Gerais

- **Nome do projeto:** AgendeAqui
- **Tipo de sistema:** Gerenciamento e Agendamento de Recursos (salas de aula e laboratórios).

## 2. Objetivos

- Permitir agendamento de salas por diferentes perfis de usuários;
- Oferecer calendário interativo para consulta de disponibilidade;
- Fornecer ferramentas de aprovação/reprovação de solicitações;
- Disponibilizar funcionalidades administrativas (cadastro de salas, blocos, recursos);
- Gerar relatórios e exportações sobre ocupação e histórico de uso.

## 3. Principais Funcionalidades

- **Autenticação:** login, logout, alteração de senha;
- **Visualização:** calendário com disponibilidade de salas;
- **Solicitação:** professores solicitam reservas com data, horário e motivo;
- **Gestão de Reservas:** coordenadores aprovam/reprovam solicitações (com justificativa);
- **Administração:** CRUD de salas, blocos e recursos;
- **Relatórios:** filtros, gráficos e exportação (CSV).

## 4. Organização em Apps (Django)

O projeto é dividido em apps para separar responsabilidades:

- `administracao` (config do projeto)
	- Contém `settings.py`, `urls.py`, `wsgi/asgi` e templates globais;
	- Templates principais: `base.html`, `login.html`, `cadastro.html`.

- `agendamentos` (app central)
	- Lida com regras de negócio de reservas e calendário;
	- Templates: `home.html`, `agendamentos.html`, `perfil_do_usuario.html`, `relatorios.html`.

- `salas` (app de ambiente físico)
	- Modelos: `Bloco`, `Sala`, `Recurso`;
	- CRUD de salas, listagem e filtros.

- `dashboard` (visão geral)
	- Página inicial com métricas e gráficos (resumo dos agendamentos e status).

- `relatorios` (análises e exportação)
	- Filtros avançados, visualizações gráficas e exportação CSV/Excel.

## 5. Próximos passos (curto prazo)

- Implementar modelos e migrações para `salas` e `agendamentos`;
- Criar views e templates para CRUD de salas e fluxo de solicitações;
- Implementar dashboard com gráficos (Chart.js) e relatórios com export CSV.


