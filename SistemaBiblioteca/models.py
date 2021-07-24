class Livro:
    def __init__(self,nome,autor,ano,genero):
        self.nome=nome
        self.autor=autor
        self.ano=ano
        self.genero=genero
    def setNome(self,nome):
        self.nome=nome
    def setAutor(self,autor):
        self.autor=autor
    def setAno(self,ano):
        self.ano=ano
    def setGenero(self,genero):
        self.genero=genero
    def getNome(self):
        return self.nome
    def getAutor(self):
        return self.autor
    def getAno(self):
        return self.ano
    def getGenero(self):
        return self.genero

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