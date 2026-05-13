from produtos.cadastro_produtos.cadastro_prod import criar_produto
cad_prod = {}
while True:
    opcao_menu = input('Digite o numero do que deseja executar: \n 1- Cadastrar produtos \n 2- Listar produtos \n 3- Procurar produtos \n 0- Sair\n')
    if opcao_menu == '1':
        cad_prod = criar_produto()
    elif opcao_menu == '2':
        print('\n',cad_prod,'\n')
    elif opcao_menu == '3':
        buscar_prod = input("Digite o nome do produto para consulta-lo: ")
        print('\n',cad_prod[buscar_prod],'\n')
    elif opcao_menu == '0':
        break
