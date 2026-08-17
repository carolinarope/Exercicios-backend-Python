# 🎫 TICKET DEV-PY-001 — Modelagem de Cliente com POO

## 📌 Contexto

Como parte da evolução do projeto de estudos em Python, foi criada uma primeira implementação utilizando Programação Orientada a Objetos (POO).

O objetivo deste exercício é substituir gradualmente estruturas baseadas apenas em dicionários e funções por classes e objetos, preparando a aplicação para uma arquitetura mais organizada.

---

## 🎯 Objetivo

Criar uma classe `Cliente` capaz de representar clientes do sistema, contendo seus dados básicos e um método para exibição das informações.

---

## 📋 Requisitos

- [x] Criar a classe `Cliente`
- [x] Implementar o método construtor `__init__`
- [x] Criar os atributos `id`, `nome`, `email` e `telefone`
- [x] Criar o método `exibir_dados()`
- [x] Instanciar três objetos da classe
- [x] Atribuir dados diferentes para cada cliente
- [x] Executar testes no terminal
- [x] Verificar se cada objeto mantém seus próprios dados

---

## 🛠️ Tecnologias

- Python 3
- Programação Orientada a Objetos
- Classes e objetos
- Construtor `__init__`
- Atributos de instância
- Métodos
- F-strings

---

## 🧠 Conceitos praticados

### Classe

A classe `Cliente` funciona como um modelo para criação de objetos que representam clientes.

### Objeto

Foram criadas três instâncias independentes:

- `c1`
- `c2`
- `c3`

Cada objeto possui seus próprios valores para nome, e-mail, telefone e ID.

### Construtor

O método `__init__` inicializa os atributos de cada novo objeto.

### `self`

O parâmetro `self` representa a própria instância que está utilizando o método.

---

## 🧪 Testes realizados

Foram criados três clientes com dados diferentes e executado o método `exibir_dados()` para verificar o comportamento dos objetos.

### Resultado esperado

```text
ID: 1
Nome: Carolina
Email: carolina@gmail.com
Telefone: 99999999

ID: 2
Nome: Amanda
Email: amanda@gmail.com
Telefone: 88888888

ID: 3
Nome: Bruna
Email: bruna@gmail.com
Telefone: 77777777