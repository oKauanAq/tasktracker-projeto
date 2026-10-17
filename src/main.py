def exibir_menu():
    print("\n=== TASK TRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de nova tarefa.")

        elif opcao == "2":
            print("\nVisualização de tarefas.")

        elif opcao == "3":
            print("\nEncerrando a aplicação. Até logo!")
            break

        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()