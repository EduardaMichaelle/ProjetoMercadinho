class Usuario:
  def __init__(self,nome:str,CPF:int,senha:str,permissao:int):
    self.nome = nome
    self.CPF = CPF
    self.senha = senha
    self.permissao = permissao
    print('Bem-vindx,', self.nome, '('+self.getPermissao()+')')

  def getNome(self):
    return self.nome

  def getCPF(self):
    return self.CPF

  def getSenha(self):
    return self.senha

  def getPermissao(self):
    if self.permissao==1:
      return 'Caixa'

    else:
      return 'Admin'