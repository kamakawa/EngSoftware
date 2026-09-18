# 🚗 Protótipo de Estacionamento — UTFPR

> **Engenharia de Software — Atividade em Sala: Dos Requisitos ao Protótipo Inicial**

Protótipo desenvolvido para a disciplina de **Engenharia de Software** da **Universidade Tecnológica Federal do Paraná (UTFPR)**, sob orientação do professor **Luiz Rodrigues**.

O projeto representa a transição entre a **especificação de requisitos** e uma primeira implementação executável, utilizando **Python** e interação exclusivamente pelo terminal.

---

## 🎯 Objetivo

Desenvolver um pequeno protótipo de um aplicativo de estacionamento para o campus da UTFPR, permitindo demonstrar em código alguns dos requisitos levantados na primeira etapa do projeto.

O protótipo foi desenvolvido de forma intencionalmente simples, com foco em **demonstrar os requisitos funcionando**, e não em construir uma aplicação completa.

---

## 📋 Requisitos Implementados

### RF01 — Visualização das vagas disponíveis

> Como aluno, quero visualizar as vagas disponíveis no estacionamento em tempo real, para conseguir saber onde há possibilidade de estacionar, principalmente durante o horário de pico da manhã.

O protótipo apresenta no terminal quais vagas estão atualmente disponíveis.

### RF03 — Identificação das vagas reservadas

> Como aluno, quero saber quais vagas são reservadas para funcionários, principalmente próximas à biblioteca, para evitar estacionar em uma vaga que não é destinada aos alunos.

O protótipo identifica e apresenta quais vagas são destinadas a funcionários.

---

## 🏗️ Estrutura do Projeto

```text
Atividade em Sala - Dos Requisitos ao Protótipo Inicial/
│
├── main.py
├── rf01_vagas.py
├── rf03_reservadas.py
├── requisitos.txt
├── README.md
└── GIT.md
```

### 📌 `main.py`

É o **ponto de entrada único** do protótipo. Executa os requisitos implementados e apresenta seus resultados no terminal.

### 📌 `rf01_vagas.py`

Contém a implementação do **RF01 — Visualização das vagas disponíveis**.

### 📌 `rf03_reservadas.py`

Contém a implementação do **RF03 — Identificação das vagas reservadas**.

### 📌 `requisitos.txt`

Apresenta os requisitos implementados pelo protótipo.

### 📌 `GIT.md`

Contém a sequência sugerida de commits utilizada durante o desenvolvimento da atividade.

---

## 🛠️ Tecnologias

* 🐍 **Python**
* 🔀 **Git**
* 🐙 **GitHub**
* 💻 **Terminal / Linha de comando**

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta

```bash
cd "Atividade em Sala - Dos Requisitos ao Protótipo Inicial"
```

### 3. Execute o protótipo

```bash
python main.py
```

---

## 💻 Exemplo de execução

```text
=======================================================
PROTÓTIPO - ESTACIONAMENTO DO CAMPUS
=======================================================

[RF01] Visualização das vagas disponíveis
Vagas disponíveis: A01, A03, A05

[RF03] Identificação das vagas reservadas
Vagas reservadas para funcionários: A02, B01
Essas vagas não devem ser consideradas vagas comuns para alunos.

=======================================================
Protótipo executado com sucesso.
=======================================================
```

Os dados apresentados são **simulados**, exclusivamente para demonstrar o funcionamento dos requisitos no pro
