
# TECHFLOW CORE - GERENCIADOR DE DEMANDAS

from utils import (
    validar_texto,
    validar_prioridade,
    formatar_cep
)

demandas = []

STATUS_VALIDOS = ["Pendente", "Em andamento", "Concluída"]


# CADASTRAR DEMANDA
def cadastrar_demanda():
    print("\n--- CADASTRAR DEMANDA ---")

    identificador = input("ID: ").strip()

    if not validar_texto(identificador):
        print("Erro: ID não pode ficar vazio.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Erro: ID já cadastrado.")
            return

    titulo = input("Título: ").strip()
    solicitante = input("Solicitante: ").strip()
    prioridade = input("Prioridade: ").strip().capitalize()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()

    if not all(validar_texto(campo) for campo in [
        titulo, solicitante, prioridade, cep, cidade
    ]):
        print("Erro: todos os campos são obrigatórios.")
        return

    if not validar_prioridade(prioridade):
        print("Erro: prioridade inválida.")
        return

    cep = formatar_cep(cep)

    if cep is None:
        print("Erro: CEP deve conter 8 números.")
        return

    nova_demanda = {
        "id": identificador,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Pendente"
    }

    demandas.append(nova_demanda)
    print("Demanda cadastrada com sucesso!")


# LISTAR DEMANDAS
def listar_demandas():
    print("\n--- LISTA DE DEMANDAS ---")

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        print("-" * 30)

        for campo, valor in demanda.items():
            print(f"{campo.capitalize()}: {valor}")


# BUSCAR DEMANDA
def buscar_demanda():
    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Demanda encontrada:")

            for campo, valor in demanda.items():
                print(f"{campo.capitalize()}: {valor}")

            return

    print("Demanda não encontrada.")


# ATUALIZAR STATUS
def atualizar_status():
    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            novo_status = input(
                "Novo status (Pendente, Em andamento, Concluída): "
            ).strip().capitalize()

            if novo_status not in STATUS_VALIDOS:
                print("Erro: status inválido.")
                return

            demanda["status"] = novo_status
            print("Status atualizado com sucesso!")
            return

    print("Demanda não encontrada.")


# EXCLUIR DEMANDA
def excluir_demanda():
    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            demandas.remove(demanda)
            print("Demanda excluída com sucesso!")
            return

    print("Demanda não encontrada.")


# MENU PRINCIPAL
def menu():
    while True:
        print("\n===== TECHFLOW CORE =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            buscar_demanda()

        elif opcao == "4":
            atualizar_status()

        elif opcao == "5":
            excluir_demanda()

        elif opcao == "0":
            print("Encerrando o TechFlow Core!")
            break

        else:
            print("Opção inválida.")
