# 📚 Sistema de Cadastro de Alunos (Python + SQLite)

Este projeto é um sistema simples de cadastro de alunos utilizando **Python** e **SQLite**, ideal para iniciantes praticarem conceitos de banco de dados, lógica de programação e organização de projetos.

---

## 🧩 Funcionalidades

- ✅ Cadastrar novos alunos  
- 📋 Listar todos os alunos cadastrados  
- 🔍 Buscar aluno por ID  
- ✏️ Atualizar informações de um aluno (nome, idade ou curso)  
- ❌ Remover aluno do sistema por ID

---

## 📁 Estrutura do Projeto

```
cadastro_alunos/
├── main.py                   # Menu principal do sistema
├── db/
│   └── conexao.py            # Conexão com o banco SQLite
├── database/
│   └── alunos.db             # Banco de dados SQLite (criado automaticamente)
├── models/
│   └── aluno.py              # Funções de CRUD (Create, Read, Update, Delete)
├── utils/
│   └── helpers.py            # Funções auxiliares e validações
├── README.md                 # Descrição do projeto
```

---

## ⚙️ Requisitos

- Python 3 instalado ✅

---

## 🚀 Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cadastro_alunos.git
cd cadastro_alunos
```

2. Execute o arquivo principal:
```bash
python main.py
```

---

## 🧠 Tecnologias utilizadas

- Python 3
- SQLite (via `sqlite3` do Python)

---

## 📌 Aprendizados envolvidos

- Operações CRUD com banco de dados
- Estruturação de projetos Python
- Separação por responsabilidade (código limpo)
- Manipulação de dados com SQL

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar! 🚀

---

Criado com 💻 por Pedro Augusto

