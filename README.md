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