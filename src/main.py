tarefas = []


def exibir_menu():
    print("\n=== TASK TRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def ler_titulo():
    while True:
        titulo = input("Digite o título da tarefa: ").strip()

        if titulo:
            return titulo

        print("Erro: o título não pode ficar vazio.")


def ler_prioridade():
    while True:
        prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().lower()

        if prioridade == "alta":
            return "Alta"

        elif prioridade == "média" or prioridade == "media":
            return "Média"

        elif prioridade == "baixa":
            return "Baixa"

        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa():
    print("\n=== CADASTRO DE NOVA TAREFA ===")

    titulo = ler_titulo()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Digite a data limite: ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n=== TAREFAS CADASTRADAS ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()

        elif opcao == "2":
            visualizar_tarefas()

        elif opcao == "3":
            print("\nEncerrando a aplicação. Até logo!")
            break

        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()