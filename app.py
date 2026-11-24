clientes = []


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ").strip()
    if nome == "":
        print("Nome inválido. Digite um nome antes de salvar.")
        input("Pressione Enter para voltar ao menu...")
        return

    clientes.append(nome)
    print("Cliente cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")


def listar_clientes():
    print("\n=== CLIENTES CADASTRADOS ===")
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        input("Pressione Enter para voltar ao menu...")
        return

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente}")

    input("Pressione Enter para voltar ao menu...")


def exibir_menu():
    print("\n=== SISTEMA DE CADASTRO DE CLIENTES ===")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Sair")


while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
        input("Pressione Enter para voltar ao menu...")