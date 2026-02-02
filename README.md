# Organizador de Arquivos em Python

Este projeto nasceu de uma necessidade real: automatizar a organização de arquivos dispersos no meu computador. O objetivo foi transformar uma tarefa manual e repetitiva em um processo eficiente, utilizando este cenário como laboratório para aprofundar conhecimentos em automação, manipulação do sistema de arquivos
e boas práticas de código.

---

## 📌 Funcionalidades

- Organização automática de arquivos por categoria:
  - Imagens
  - PDFs
  - Planilhas
  - Vídeos
  - Documentos
  - Slides
  - Outros (arquivos não mapeados)
- Criação automática de pastas
- Sobrescrita segura de arquivos já existentes
- Ignora subpastas e processa apenas arquivos

---

## 🧠 Decisões de Projeto

- O script utiliza `os.rename` para mover arquivos, aproveitando o comportamento
  nativo do sistema operacional.
- Foi adotada uma categoria `outros` para arquivos que não se encaixam em padrões
  conhecidos, evitando falhas ou perdas.
- O projeto prioriza simplicidade e clareza, sem dependências externas desnecessárias.

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/IannyCorreia/organizador-de-arquivos.git
