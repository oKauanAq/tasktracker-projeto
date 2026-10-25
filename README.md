# TaskTracker

Projeto desenvolvido ao longo das etapas do Bootcamp II: planejamento lógico, implementação em Python e execução em containers Docker.

## Descrição

O TaskTracker é uma aplicação de linha de comando desenvolvida em Python para gerenciamento simples de tarefas.

A aplicação permite cadastrar novas tarefas, visualizar tarefas cadastradas, validar informações de entrada e acompanhar o status inicial de cada tarefa.

## Funcionalidades

- Cadastrar nova tarefa
- Visualizar tarefas cadastradas
- Validar título obrigatório
- Validar prioridade
- Definir status inicial como Pendente

## Tecnologias utilizadas

- Python 3
- Git
- GitHub
- Docker e Docker Compose

## Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py


```

## Como executar

### Com Python instalado (opcional)

```text
py src/main.py
```

### Com Docker

Instale o Docker Desktop e aguarde o Engine iniciar. No Windows, utilize o backend WSL 2 e containers Linux. O Docker Compose já acompanha o Docker Desktop. Não é necessário instalar Python no computador para executar o container.

Verifique o ambiente:

```sh
docker --version
docker compose version
docker info
```

Baixe o projeto e entre na raiz do repositório:

```sh
git clone https://github.com/oKauanAq/tasktracker-projeto.git
cd tasktracker-projeto
```

**1. Construir a imagem:**

```sh
docker build -t tasktracker:latest .
```

**2. Executar o container isolado em modo interativo:**

```sh
docker run --rm -it tasktracker:latest
```

**3. Executar com Docker Compose:**

```sh
docker compose run --build --rm tasktracker
```

Execute uma alternativa de cada vez. No menu, escolha `1` para cadastrar, `2` para listar e `3` para sair. A opção `--rm` remove apenas o container daquela execução ao terminar. A imagem continua disponível.

### Como funciona a configuração

- `FROM python:3.11-slim`: usa uma base oficial com Python e sistema reduzido.
- `WORKDIR /app`: define o diretório de trabalho dentro do container.
- `ENV PYTHONUNBUFFERED=1`: exibe imediatamente as saídas do Python.
- `COPY src/ /app/src/`: inclui o código da aplicação na imagem.
- `CMD`: inicia `src/main.py` quando o container é executado.
- `build: .`: o Compose constrói a imagem usando o Dockerfile da raiz.
- `stdin_open: true`: mantém a entrada de dados aberta para `input()`.
- `tty: true`: disponibiliza um terminal virtual para a interação.
- `.dockerignore`: exclui arquivos desnecessários do contexto de construção.

O programa utiliza somente a biblioteca padrão do Python, portanto não precisa de instalação de pacotes adicionais. É uma aplicação de terminal: não abre página no navegador nem precisa publicar portas. Use `docker compose run` para interagir com o menu.

### Validações e limites

Para conferir o funcionamento, liste antes de cadastrar, tente uma opção de menu inválida, cadastre uma tarefa com título vazio e depois corrija-o, teste uma prioridade inválida e depois informe `Alta`, `Média` (ou `media`) ou `Baixa`. Ao listar, confira os dados e o status `Pendente`.

As tarefas ficam apenas na memória durante a execução. Ao sair, elas são perdidas, inclusive ao executar novamente o mesmo container. A descrição e a data limite são textos livres; não há validação de calendário. Esses comportamentos pertencem à implementação da Etapa Intermediária, preservada nesta etapa.

Se aparecer erro de conexão com o Engine, abra o Docker Desktop e aguarde sua inicialização. Para evitar erros de entrada (`EOFError`), execute em um terminal interativo com `-it` no Docker ou com o comando Compose acima.

## Histórico das etapas

- Etapa Inicial: planejamento em `docs/planejamento_logico.pdf`.
- Etapa Intermediária: aplicação e regras em `src/main.py`.
- Etapa Final: Dockerfile, Compose e instruções de execução em containers.

O histórico Git e o documento de planejamento foram preservados.

## Autor

Kauan Souza de Aquino  
Engenharia de Software  
Bootcamp II
