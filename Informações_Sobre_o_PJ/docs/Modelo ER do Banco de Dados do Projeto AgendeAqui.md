# Modelo ER — AgendeAqui

Este documento descreve a modelagem conceitual do banco de dados do projeto AgendeAqui: entidades, atributos e relacionamentos.

## Entidades e Atributos

- **Usuário (User)**
	- Atributos: `id` (PK), `nome`, `email`, `senha` (hash), `tipo_perfil` (enum: Admin, Coordenador, Professor)

- **Bloco**
	- Atributos: `id` (PK), `nome` (ex.: "Bloco A")

- **Sala**
	- Atributos: `id` (PK), `nome`/`numero` (ex.: "Lab 3"), `capacidade` (inteiro)
	- Relacionamento: pertence a um `Bloco` (`bloco_id` FK)

- **Recurso**
	- Atributos: `id` (PK), `nome` (ex.: Projetor, Ar-condicionado)
	- Relacionamento: Many-to-Many com `Sala` (tabela intermediária `sala_recursos`)

- **Agendamento**
	- Atributos: `id` (PK), `data` (date), `horario_inicio` (time), `horario_fim` (time), `motivo` (texto), `status` (enum: Pendente, Aprovado, Reprovado), `justificativa_reprovacao` (texto opcional)
	- Relacionamentos: pertence a um `Usuário` (`usuario_id` FK) e a uma `Sala` (`sala_id` FK)

## Relacionamentos e Cardinalidades

- **Usuário (1) — (N) Agendamento**
	- Um usuário pode criar vários agendamentos; cada agendamento tem exatamente um usuário solicitante.

- **Sala (1) — (N) Agendamento**
	- Uma sala pode possuir múltiplos agendamentos (em horários diferentes), cada agendamento refere-se a uma única sala.

- **Bloco (1) — (N) Sala**
	- Um bloco contém várias salas; cada sala pertence a um bloco.

- **Sala (N) — (N) Recurso**
	- Uma sala pode ter vários recursos; um recurso pode estar presente em várias salas. Implementar via tabela de associação (`sala_recursos`).

## Observações para implementação

- Use `ForeignKey` com `on_delete=PROTECT` para `Sala.bloco` para evitar exclusão acidental de blocos com salas associadas.
- Para o relacionamento many-to-many entre `Sala` e `Recurso`, utilize `ManyToManyField` em Django.
- Considere adicionar índices em `Agendamento.data` e `Agendamento.horario_inicio` para otimizar consultas de disponibilidade.

## Arquivos relacionados

- Diagrama visual (PDF/PNG) — anexar ao repositório em `docs/` quando disponível.


