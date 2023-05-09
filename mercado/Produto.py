class Produto:
    def __init__(self,nome:str,codigo:int,preco:float):
        self.codigo = codigo
        self.preco = preco
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def getCodigo(self):
        return self.codigo
    
    def getPreco(self):
        return self.preco