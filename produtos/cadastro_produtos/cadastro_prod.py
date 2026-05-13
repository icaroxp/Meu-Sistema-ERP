


def criar_produto():
    cadastro_produtos = {}
    while True:
            nome_produto = input("Digite o nome do produto: ")
            preco_custo = float(input("Digite o valorde custo do produto: "))
            preco_venda = float(input("Digite o valor de venda do produto: "))
            qtde_prod_estoque = int(input("Digite a quantia em estoque: "))

            cadastro_produtos[nome_produto] = {
            "Valor de custo:": preco_custo,
            "Valor de venda:": preco_venda,
            "Quantidade": qtde_prod_estoque,
            }

            sair = input("Deseja continuar o programa? S ou N")
            if sair.upper() == 'N':
                break
    return cadastro_produtos




        


