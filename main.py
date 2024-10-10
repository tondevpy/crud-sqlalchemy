from db import Repositorio
from hashlib import sha256
import os

def validar_input(mensagem):
    while True:
        variavel = input(f"{mensagem}: ").lower().strip()
        if variavel:
            return variavel
        else:
            print('ERRO: esse campo deve ser preenchido')

def cadastrar():
    nome = validar_input('Informe seu nome')
    email = validar_input('Informe seu email')

    validar_email = Repositorio.localizar_usuario(email=email)
    if not validar_email:
        senha = validar_input('Informe sua senha')
        try:
            Repositorio.criar_usuario(nome=nome, email=email, senha=senha)
            print('Usuário cadastrado com sucesso!')
        except Exception as e:
            print(f'Erro: {e}')
    else:
        print('Esse usuário já possui cadastro, faça o login...')
    
    
def fazer_login():
    email = validar_input('Informe seu email')
    senha = validar_input('Informe sua senha')

    senha_hash = sha256(senha.encode('utf-8')).hexdigest()

    return Repositorio.login_usuario(email, senha_hash)

def atualizar_usuario(email):
    nome = validar_input('Informe o novo nome: ')
    novo_email = validar_input('Informe o novo email')
    senha = validar_input('Informe a nova senha')
    
    Repositorio.editar_usuario(email=email, novo_nome=nome, nova_senha=senha, novo_email=novo_email)

def deletar_usuario(email):
    try:
        Repositorio.excluir_usuario(email=email)
        print('Usuário excluido com sucesso...')
    except Exception as e:
        print(f"ERRO: ocorreu um erro {e}")

def logar():

    email = fazer_login()
    if email:
        while True:
            os.system('cls')
            
            print('[1] Atualizar conta\n[2] Excluir conta\n[3] - Sair')
            opcao = validar_input('Digite o numero da opção desejada')
            if opcao == '1':
                atualizar_usuario(email)
            elif opcao == '2':
                deletar_usuario(email)
                print('Deslogado...')
                break
            elif opcao == '3':
                print('Deslogado com sucesso...')
                break
            else:
                print('Informou uma opção inválida...')

            input('Aperte enter para voltar ao painel!')
    else:
        print('Email ou senha inválido...')


def menu():
    print('Seja bem vindo ao sistema de login\n\n[1] - Criar um usuário\n[2] - Fazer login\n\nInforme o numero da opção desejada...')
    escolha = validar_input('Opção')
    if escolha == '1':
        cadastrar()
    elif escolha == '2':
        logar()
    else:
        print('escolheu uma opção inválida...')


menu()

