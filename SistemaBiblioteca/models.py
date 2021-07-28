import time
from pymongo import MongoClient
import random
client= MongoClient('mongodb+srv://projeto:projeto@sistemabiblioteca.3o1zg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=client["SistemaBiblioteca"]
col= db["Livros"]
col2=db["ADM's"]
col3=db["Visitantes"]

class Livro:
    def __init__(self,nome,autor,ano,genero,admreference):
        self.nome=nome
        self.autor=autor
        self.ano=ano
        self.genero=genero
        self.admreference=admreference
    def setNome(self,nome):
        self.nome=nome
    def setAutor(self,autor):
        self.autor=autor
    def setAno(self,ano):
        self.ano=ano
    def setGenero(self,genero):
        self.genero=genero
    def setAdmreference(self,admreference):
        self.admreference=admreference
    def getNome(self):
        return self.nome
    def getAutor(self):
        return self.autor
    def getAno(self):
        return self.ano
    def getGenero(self):
        return self.genero
    def getAdmreference(self):
        return self.admreference

class Adm:
    def __init__(self,login,senha):
        self.login=login
        self.senha=senha
    def setLogin(self,login):
        self.login=login
    def setSenha(self,senha):
        self.senha=senha
    def getLogin(self):
        return self.login
    def getSenha(self):
        return self.senha
class Visitante:
    def __init__(self,nome):
        self.nome=nome
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

def addAdm(login, senha):
    adms = {"Login": login, "Senha": senha}
    col2.insert(adms)
    print("Adm Cadastrado com Sucesso!")
def addLivro(nome,autor,ano,genero,admreference):
    conjid = tuple(range(99999, 999998))
    id = str(random.sample(conjid, 1))
    verify = col.find({"_id": id})
    for y in verify:
        while y == id:
            conjid = tuple(range(99999, 999998))
            id = str(random.sample(conjid, 1))
        if y != id:
            break
    livros = {'_id': id, 'Nome do Livro': nome, 'Autor': autor, 'Ano': ano,
              'Gênero': genero, 'Adicionado por':admreference}
    col.insert_one(livros)
    print("Livro Cadastrado com Sucesso!")
def editLivro(pesquisaed, categoria, infonova):
    col.update_one({"Nome do Livro": pesquisaed}, {"$set": {categoria: infonova}})
def excluirLivro(nome):
    col.delete_one({"Nome do Livro": nome})
def pesquisaLivro(categoria, nomepesquisa):
    docpesquisa = col.find({categoria: nomepesquisa})
    for i in docpesquisa:
        print(i)
def addVisit(nome):
    col3.insert_one({"Nome": nome, "Hora e dia de entrada": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})
