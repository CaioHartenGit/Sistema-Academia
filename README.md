# 🏋️ Sistema de Academia

Sistema de gerenciamento de academia desenvolvido em **Python** com **PostgreSQL**, utilizando **Programação Orientada a Objetos (POO)** e uma arquitetura organizada em camadas.

O projeto tem como objetivo colocar em prática conceitos de desenvolvimento de software, banco de dados, CRUD, POO, separação de responsabilidades e integração entre aplicação e banco de dados.

---

## 🚀 Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem principal |
| 🐘 PostgreSQL | Banco de dados |
| 🔌 Psycopg | Conexão entre Python e PostgreSQL |
| 🧱 POO | Organização e modelagem das entidades |
| 🗃️ SQL | Operações no banco de dados |
| 🔀 Git | Controle de versão |
| 🌐 GitHub | Hospedagem do projeto |

---

## 📌 Funcionalidades

### 👤 Alunos

- Cadastrar aluno
- Listar alunos
- Buscar aluno por ID
- Buscar aluno por nome
- Buscar alunos por plano
- Atualizar dados do aluno
- Ativar aluno
- Desativar aluno
- Excluir aluno

### 🏋️ Treinos

- Cadastrar treino
- Listar treinos
- Buscar treinos de um aluno
- Alterar dia do treino
- Excluir treinos

### 💪 Exercícios

- Cadastrar exercício
- Listar exercícios de um treino
- Atualizar exercício
- Excluir exercício

---

## 🧠 Arquitetura

O projeto foi organizado utilizando uma separação de responsabilidades entre:

```text
Interface
   ↓
Service
   ↓
Repository
   ↓
PostgreSQL
```

## ▶️ Executando

Na raiz do projeto, inicie o menu com:

```bash
python3 -m apps.main
```
Execute como módulo para que os imports `apps.*` sejam resolvidos corretamente.

## Desenvolvendo com FastAPI

### Iniciar o servidor

Execute o comando abaixo na raiz do projeto `SISTEMA-ACADEMIA`:

```bash
python3 -m fastapi dev apps/routers/alunosAPI.py
```

**Por que executar como módulo?**

Essa forma de inicialização permite executar o FastAPI pelo ambiente Python selecionado e, no nosso projeto, resolveu o problema de importação dos módulos `apps.*`.

### Acessar a documentação

Com o servidor em execução, acesse:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **OpenAPI JSON:** http://127.0.0.1:8000/openapi.json

Para encerrar o servidor, pressione `Ctrl + C` no terminal.
