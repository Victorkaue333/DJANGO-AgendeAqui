# AgendeAqui

AgendeAqui é um sistema web robusto para agendamento e gerenciamento de salas de aula, projetado para otimizar a utilização dos espaços acadêmicos e facilitar o controle de reservas por professores, coordenadores e administradores. O sistema previne conflitos de horários e promove uma gestão transparente e eficiente.

## 📋 Visão Geral

O AgendeAqui oferece:
- Solicitação, aprovação e gerenciamento centralizado de reservas de salas
- Controle granular de permissões por função (Administrador, Professor, Coordenação)
- Notificações automáticas e geração de relatórios de uso detalhados

## ✨ Funcionalidades

- **Autenticação de usuários**: Login seguro e controle de sessão
- **Gestão de perfis**: Cadastro, edição e atribuição de perfis por função
- **Administração de salas**: Inclusão, edição e exclusão de salas com cadastro de atributos específicos
- **Agendamentos inteligentes**: Solicitações de reserva com fluxo de aprovação e prevenção de conflitos
- **Calendário visual**: Consulta e visualização intuitiva das reservas em um calendário interativo
- **Notificações**: Avisos por e-mail e painel para ações importantes (aprovação, rejeição, lembretes)
- **Relatórios e exportação**: Geração de relatórios customizáveis em PDF/CSV

## 💻 Tecnologias

- **Backend:** Django 5+
- **Banco de Dados:** PostgreSQL
- **Frontend:** Django Templates com Bootstrap 5

## 🖥️ Telas do Sistema

- **Login:** Acesso ao sistema de forma autenticada
- **Dashboard:** Resumo visual dos agendamentos e status geral
- **Salas:** Listagem, cadastro, edição e exclusão de salas
- **Agendamentos:** Solicitação, acompanhamento e aprovação/rejeição de reservas
- **Relatórios:** Filtros avançados, gráficos e exportação de dados
- **Perfil do Usuário:** Visualização e edição de dados pessoais, alteração de senha e histórico de atividades

## 🚀 Como Executar o Projeto

1. **Pré-requisitos:**  
   - Python 3.10+  
   - PostgreSQL

2. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o banco de dados** em `settings.py` (usuário, senha, host, nome do banco).

4. **Execute as migrações:**
    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

6. **(Opcional) Crie um superusuário para acesso administrativo:**
    ```bash
    python manage.py createsuperuser
    ```

## 📃 Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido com 💙 para facilitar a gestão acadêmica.