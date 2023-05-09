from Produto import Produto
from Usuario import Usuario

#for produto in listaDeCompras:
#   print(produto.getNome())

def addProduto(produto:object,estoque):
  nome=produto.getNome()
  preco=produto.getPreco()
  codigo=produto.getCodigo()
  estoque.append({'Nome':nome,'Preço':preco,'Código':codigo})

  return 'Produto foi adicionado ao estoque'

op=0
produtos=[]
while op!= 3:
  print('\nMERCADINHO\n')
  print('1 - Caixa')
  print('2 - Admin')
  print('3 - Sair')
  op = int(input('\nEscolha a opção:'))
  print('\n')

  if op == 1:
    usuario=Usuario('Thiago',1,'senha',1)
    
  if op == 2:
    usuario=Usuario('Eduarda',2,'senha',2)
    
    op2=0
    while op2 !=4:
      print('\nOPÇÕES\n')
      print('1 - Adicionar produto')
      print('2 - Remover produto')
      print('3 - Visualizar o estoque')
      print('4 - Voltar')
      print('5 - Sair')

      op2= int(input('\nEscolha a opção:'))
      
      if op2 == 1:
        nomeProduto=input("Digite o nome do produto:\n")
        print('\n')
        codigoProduto=input("Digite o código do produto:\n")
        print('\n')
        precoProduto=input("Digite o preço do produto:\n")
        produto=Produto(nomeProduto,codigoProduto,precoProduto)
        addProduto(produto,produtos)

      if op2 == 3:
        print(produtos)
      
      if op2 == 5:
        print('Saindo...')
        exit(0)
      
  if op<1 or op>3:
    print('Digite uma opção válida!')