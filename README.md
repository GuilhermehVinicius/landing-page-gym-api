# API para Landing Page

## Descrição
Esta é uma API desenvolvida para a landing page [http://54.197.20.170/](http://54.197.20.170/). A API foi criada utilizando **Python** com o framework **FastAPI** e **SQLModel** para manipulação do banco de dados. O banco de dados está hospedado no **Render**, enquanto a API está hospedada na **AWS** com um proxy reverso configurado em **NGINX**.

## Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: FastAPI
- **ORM**: SQLModel
- **Hospedagem da API**: AWS
- **Banco de Dados**: Render
- **Proxy Reverso**: NGINX

# API para Landing Page

## Descrição
Esta é uma API desenvolvida para a landing page [http://54.197.20.170/](http://54.197.20.170/). A API foi criada utilizando **Python** com o framework **FastAPI** e **SQLModel** para manipulação do banco de dados. O banco de dados está hospedado no **Render**, enquanto a API está hospedada na **AWS** com um proxy reverso configurado em **NGINX**.

## Configuração do Ambiente

### Requisitos
- Python 3.13.0
- Pipenv
- Pipx
- Poetry

### Instalação
1. Clone o repositório:
   ```bash
   git clone landing-page-gym-api
   cd landing-page-gym-api
   ```

2. Instale o Pyenv, Pipx e Poetry:
    [Pyenv](https://github.com/pyenv/pyenv)
    [Pipx](https://github.com/pypa/pipx)
    [Poetry](https://python-poetry.org/docs/)

3. Configure o Pyenv para a versão 3.13.0 do Python:
   ```bash
   pyenv install 3.13.0
   pyenv local 3.13.0
   ```

4. Configurar variavel de ambiente do Banco de Dados:
   ```bash
   export DATABASE_URL = =<URL_DO_BANCO_DE_DADOS>
   ```

4. Baixar as dependências com Poetry:
   ```bash
   poetry shell
   poetry install
   fastapi dev api_form/app.py
   ```

### Estrutura do Projeto
```.
├── api_form
│   ├── app.py          # Ponto de entrada da aplicação
│   ├── database.py     # Conexão com Banco de Dados
│   ├── schemas.py      # Modelos
│   ├── settings.py     # Carregar variáveis de ambiente do projeto
├── Dockerfile          # Configuração para containerização
└── README.md           # Documentação do projeto
```
