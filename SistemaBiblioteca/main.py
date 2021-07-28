import pymongo
import time
from pymongo import MongoClient
from models import *
import random
client= MongoClient('mongodb+srv://projeto:projeto@sistemabiblioteca.3o1zg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=client["SistemaBiblioteca"]
col= db["Livros"]
col2=db["ADM's"]
col3=db["Visitantes"]
x=0 #variavel pra iniciar o looping principal
y=0 #variavel pra iniciar o looping de cadastro adm
z=0
livro= Livro(x,x,x,x,x)
keyadm= '050703' #senha para cadastro de adm
adm= Adm('x','x')
visit= Visitante('x')

while x==0:
    login = input("Entrar como Administrador(digite 'adm') \n"
                  "Entrar como Visitante(digite 'visitante')\n"
                  "Cadastrar Administrador(digite'cadastro adm')\n"
                  "Sair(digite 'sair')\n")
    if login== 'cadastro adm':
        verifykey= input("Digite a senha de cadastro de adm:\n")
        while y==0:
            if keyadm==verifykey:
                adm.setLogin(input('Digite o Login para cadastrar:\n'))
                adm.setSenha(input('Digite a senha para cadastrar:\n'))
                addAdm(adm.getLogin(),adm.getSenha())
                print("Cadastrado com sucesso!!")
                y=1
            else:
                print("Senha incorreta")
                verifykey = input("Digite a senha de cadastro de adm:\n")
    if login == "adm":
        loginadm = input("Digite o login de ADM:\n")
        senhaadm = input("Digite o senha de ADM:\n")
        while z==0:
            if col2.find_one({"Login": loginadm,"Senha": senhaadm}):
                acao= input("Cadastrar livro(digite 'cadastrar')\n"
                        "Editar informações do livro(digite 'editar')\n"
                        "Excluir livro(digite 'exlcuir')\n"
                        "Ver lista de livros(digite 'lista')\n"
                        "Pesquisar livro por categoria(digite 'pesquisar')\n"
                        "Voltar para tela inicial(digite 'voltar')\n"
                        "Sair(digite 'sair')\n"
                        "O que você quer fazer?\n")
                if acao== 'cadastrar':
                    livro.setAdmreference(loginadm)  #usei o login de adm para fazer referencia
                    livro.setNome(input('Digite o nome do Livro:\n'))
                    livro.setAutor(input('Digite o nome do Autor:\n'))
                    livro.setAno(input('Digite o ano do Livro:\n'))
                    livro.setGenero(input('Digite o gênero do Livro:\n'))
                    addLivro(livro.getNome(),livro.getAutor(),livro.getAno(),livro.getGenero(), livro.getAdmreference())
                elif acao== 'editar':
                    documents=col.find()
                    for i in documents:
                        print(i)
                    pesquisaed= input('Digite o Nome do livro que deseja editar:\n')
                    edit= input('Nome do Livro(digite "livro)\n"'
                                'Autor(digite "autor")\n'
                                'Ano(digite"ano")\n'
                                'Gênero(digite "genero")\n'
                                'O que deseja editar?\n')
                    if edit== 'livro':
                        livro.setNome(input('Digite o novo nome do Livro:\n'))
                        categoria= "Nome do Livro"
                        editLivro(pesquisaed,categoria, livro.getNome())
                    elif edit=='autor':
                        livro.setAutor(input('Digite o novo nome do Autor:\n'))
                        categoria= "Autor"
                        editLivro(pesquisaed,categoria, livro.getAutor())
                    elif edit== 'ano':
                        livro.setAno(input('Digite o novo ano do Livro:\n'))
                        categoria= "Ano"
                        editLivro(pesquisaed,categoria, livro.getAno())
                    elif edit== 'genero':
                        livro.setGenero(input('Digite o novo gênero do Livro:\n'))
                        categoria= "Gênero"
                        editLivro(pesquisaed,categoria, livro.getGenero())
                elif acao== 'excluir':
                    documents = col.find()
                    for i in documents:
                        print(i)
                    exc=(input('Digite o nome do livro que quer deletar:\n'))
                    excluirLivro(exc)
                elif acao== 'lista':
                    documents = col.find()
                    for i in documents:
                        print(i)
                elif acao== 'pesquisar':
                    pesquisa=input('Nome do Autor(digite "autor")\n'
                                    'Ano(digite "ano")\n'
                                    'Gênero(digite "genero")\n'
                                    'Quer pesquisar por qual categoria?\n')
                    if pesquisa== 'autor':
                        nomepesquisa=input('Digite o nome do Autor(com iniciais maiúsculas):\n')
                        categoria= "Autor"
                        pesquisaLivro(categoria,nomepesquisa)
                    if pesquisa== 'ano':
                        nomepesquisa=input('Digite o ano(com iniciais maiúsculas):\n')
                        docpesquisa=col.find({"Ano": nomepesquisa})
                        categoria="Ano"
                        pesquisaLivro(categoria,nomepesquisa)
                    if pesquisa== 'genero':
                        nomepesquisa=input('Digite o gênero(com iniciais maiúsculas):\n')
                        categoria= "Gênero"
                        pesquisaLivro(categoria,nomepesquisa)
                elif acao=="sair":
                    x = 1
                    break
                elif acao=="voltar":
                    break
            else:
                print("Login ou Senha incorretas")
                loginadm = input("Digite o login de ADM:\n")
                senhaadm = input("Digite o senha de ADM:\n")

    if login== "visitante":
        nomevisit=input('Digite seu nome COMPLETO:\n')
        addVisit(nomevisit)
        visit=input("Ver lista de livros(digite 'lista')\n"
                    "Pesquisar livro por categoria(digite 'pesquisar')\n"
                    "Sair(digite 'sair')\n"
                    "O que você quer fazer?\n")
        if visit=="lista":
            documents = col.find()
            for i in documents:
                print(i)
        if visit=="pesquisar":
            pesquisa = input('Nome do Autor(digite "autor")\n'
                             'Ano(digite "ano")\n'
                             'Gênero(digite "genero")\n'
                             'Quer pesquisar por qual categoria?\n')
            if pesquisa == 'autor':
                nomepesquisa = input('Digite o nome do Autor(com iniciais maiúsculas):\n')
                categoria = "Autor"
                pesquisaLivro(categoria, nomepesquisa)
            if pesquisa == 'ano':
                nomepesquisa = input('Digite o ano(com iniciais maiúsculas):\n')
                docpesquisa = col.find({"Ano": nomepesquisa})
                categoria = "Ano"
                pesquisaLivro(categoria, nomepesquisa)
            if pesquisa == 'genero':
                nomepesquisa = input('Digite o gênero(com iniciais maiúsculas):\n')
                categoria = "Gênero"
                pesquisaLivro(categoria, nomepesquisa)
        if visit=="sair":
            break
        else:
            print("Não compreendi.Comece de novo.")
            break

    if login=="sair":
        x=1
