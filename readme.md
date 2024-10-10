# Sistema de Autenticação com SQLAlchemy

Este projeto é um sistema de autenticação em linha de comando desenvolvido em Python, que utiliza o SQLAlchemy como ORM para manipulação de banco de dados SQLite. Ele oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete) para usuários, com autenticação segura utilizando hashing de senhas.

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Possíveis Melhorias](#possíveis-melhorias)

## Sobre o Projeto

Este projeto foi desenvolvido como um exercício de CRUD com SQLAlchemy e possui funcionalidades como cadastro, login, atualização e exclusão de usuários. Ele implementa um sistema simples de autenticação para usuários, com um menu de opções interativo. A segurança básica é garantida pelo hashing das senhas utilizando a biblioteca `hashlib`.

## Funcionalidades

- **Cadastro de Usuário**: Permite o registro de novos usuários com nome, e-mail e senha.
- **Login de Usuário**: Autenticação de usuários com verificação de e-mail e senha hashada.
- **Atualização de Dados**: Usuários logados podem atualizar seu nome, e-mail e senha.
- **Exclusão de Conta**: Usuários logados podem excluir sua conta permanentemente.
- **Menu Interativo**: Navegação através de um menu em linha de comando para simplificar a interação com o sistema.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca SQLAlchemy
- Biblioteca `hashlib` (inclusa no Python por padrão)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/tondevpy/sistema-autenticacao.git
   cd sistema-autenticacao
    ```

## Instale as dependências:
```bash
- pip install sqlalchemy
```

## Configuração do Banco de Dados: 

- O projeto já está configurado para utilizar um banco de dados SQLite chamado dados.db. O arquivo será criado automaticamente na primeira execução.

## Uso

Execute o programa
```bash
python app.py
```

## Menu Principal: No menu principal, você pode escolher:

- [1] - Criar um usuário: Registra um novo usuário no sistema.
- [2] - Fazer login: Realiza o login com um usuário existente.

- Funções no Menu de Login: Após o login, o usuário pode:

- [1] Atualizar conta: Altera o nome, e-mail ou senha do usuário.
- [2] Excluir conta: Remove o usuário do banco de dados.
- [3] Sair: Finaliza a sessão de login.


## Estrutura do Projeto

sistema-autenticacao/
├── app.py           # Arquivo principal com a interface do usuário e menu de opções
├── db.py            # Configuração do banco de dados, modelo de dados e repositório de funções CRUD
├── dados.db         # Arquivo de banco de dados SQLite (gerado automaticamente)
└── README.md        # Documentação do projeto

## Arquivos Principais

- db.py: Define a configuração do banco de dados e o modelo Usuario no SQLAlchemy, além das funções CRUD no repositório.
- app.py: Implementa a interface de usuário e o menu interativo, permitindo cadastro, login e gerenciamento de contas.

## Tecnologias Utilizadas

- Python 3: Linguagem de programação principal.
- SQLAlchemy: ORM (Object-Relational Mapping) para manipulação do banco de dados.
- SQLite: Banco de dados relacional leve e fácil de configurar.
- hashlib: Biblioteca padrão do Python para hashing de senhas, utilizada para segurança básica.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
