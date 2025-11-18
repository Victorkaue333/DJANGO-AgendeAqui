Modelo ER do Banco de Dados do Projeto AgendeAqui
Abaixo, apresento a Modelagem Conceitual completa do AgendeAqui, pronta para ser entregue. Incluí a definição das entidades, atributos e relacionamentos, além de um diagrama visual e o arquivo PDF para entrega.
1. Definição das Entidades e Atributos
Aqui definimos os "objetos" do mundo real que seu sistema vai gerenciar.
Usuário (User): Representa todas as pessoas que acessam o sistema.
Atributos: ID, Nome, Email, Senha, Tipo de Perfil (Admin, Coordenador, Professor).
Sala: O espaço físico que será reservado.
Atributos: ID, Nome/Número (ex: "Lab 3", "Sala 101"), Capacidade (ex: 40 alunos).
Bloco: A localização macro onde a sala está. É importante separar da "Sala" para normalização e relatórios (ex: "Bloco A", "Bloco de Medicina").
Atributos: ID, Nome/Letra.
Recurso: Equipamentos disponíveis nas salas (ex: Projetor, Ar-condicionado, Computadores).
Atributos: ID, Nome do Recurso.
Agendamento: A entidade central que liga "quem" reservou "onde" e "quando".
Atributos: ID, Data, Horário de Início, Horário de Fim, Motivo da Reserva, Status (Pendente, Aprovado, Reprovado), Justificativa de Reprovação.
2. Relacionamentos e Cardinalidades
Aqui definimos as regras de negócio de como essas entidades interagem:
Usuário (Solicita) Agendamento:
1:N (Um para Muitos): Um usuário pode fazer vários agendamentos, mas um agendamento pertence a apenas um usuário.
Sala (Recebe) Agendamento:
1:N (Um para Muitos): Uma sala pode ter vários agendamentos (em horários diferentes), mas um agendamento específico refere-se a apenas uma sala.
Bloco (Contém) Sala:
1:N (Um para Muitos): Um bloco possui várias salas, mas uma sala pertence a apenas um bloco.
Sala (Possui) Recurso:
N:N (Muitos para Muitos): Uma sala pode ter vários recursos (ex: tem Projetor E Ar-condicionado), e um tipo de recurso (ex: Projetor) pode estar presente em várias salas.

