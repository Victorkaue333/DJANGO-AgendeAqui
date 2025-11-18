Atividade: Definição do Projeto de Desenvolvimento Web

1. Nome do projeto: AgendeAqui

2. Tipo de sistema que será criado: Sistema de Gerenciamento e Agendamento de Recursos (Focado em Salas de Aula e Laboratórios para Instituições de Ensino).

3. Funções do sistema: O sistema permitirá que diferentes perfis de usuários realizem as seguintes ações:
Autenticação: Fazer login, logout e alterar senha.
Visualização: Consultar a disponibilidade de salas através de um calendário interativo.
Solicitação: Professores podem solicitar a reserva de uma sala para uma data e horário específicos.
Gerenciamento de Reservas: Coordenadores podem visualizar solicitações pendentes e aprová-las ou reprová-las (com justificativa).
Administração: O administrador pode cadastrar, editar e excluir salas, blocos e recursos (ex: projetores).
Relatórios: Geração de relatórios sobre a ocupação das salas e histórico de uso.
4. Divisão das funções do sistema em aplicativos (Apps): Para organizar o projeto dentro do Framework Django, as funcionalidades foram estruturadas da seguinte forma:
administracao (Pasta do Projeto/Config): Além das configurações principais (settings.py, urls.py), esta pasta gerencia os templates globais e de entrada do sistema.
Responsável pelo layout base (base.html).
Responsável pelas telas de autenticação e registro (login.html, cadastro.html).
agendamentos (App Principal): Este é o aplicativo central que contém toda a lógica de negócio do sistema. Ele agrupa as funcionalidades de:
Dashboard: Página inicial do sistema (home.html).
Gestão de Usuários: Visualização e edição do perfil (perfil_do_usuario.html).
Salas: Cadastro e listagem dos espaços físicos (salas.html).
Reservas: Lógica de solicitação e calendário de agendamentos (agendamentos.html).
Relatórios: Visualização dos dados de uso (relatorios.html).

