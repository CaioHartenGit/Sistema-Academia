from aluno_repository import AlunoRepository
from aluno_service import AlunoService


repository = AlunoRepository()
aluno_service = AlunoService(repository)


while True:

    print("\n=========== Sistema de Alunos ==========")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Buscar por ID")
    print("4 - Atualizar Aluno")
    print("5 - Deletar Aluno")
    print("6 - Ativar Aluno")
    print("7 - Desativar Aluno")
    print("8 - Buscar por Nome")
    print("9 - Buscar por Plano")
    print("10 - Sair do Sistema")
    print("=========================================")

    try:
        opcao = int(input("Digite uma opção: "))

    except ValueError:
        print("Digite somente números.")
        continue

    match opcao:

        case 1:

            try:

                print("\nSistema de Cadastro")

                nome = input("Insira seu nome: ")
                idade = int(input("Insira sua idade: "))
                plano = input("Insira seu plano: ")

                aluno = aluno_service.cadastrar(
                    nome,
                    idade,
                    plano
                )

                print("\nAluno cadastrado com sucesso!")
                print(f"ID: {aluno.id_aluno}")
                print(f"Nome: {aluno.nome}")
                print(f"Plano: {aluno.plano}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 2:

            try:

                print("\nListando Alunos")

                alunos = aluno_service.listar()

                if not alunos:
                    print("Nenhum aluno cadastrado no sistema.")
                    continue

                for aluno in alunos:

                    print("------------------------")
                    print(f"ID: {aluno.id_aluno}")
                    print(f"Nome: {aluno.nome}")
                    print(f"Idade: {aluno.idade}")
                    print(f"Plano: {aluno.plano}")
                    print(f"Ativo: {aluno.ativo}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 3:

            try:

                id_aluno = int(input("Digite o ID: "))

                aluno = aluno_service.buscar_por_id(id_aluno)

                print("------------------------")
                print(f"ID: {aluno.id_aluno}")
                print(f"Nome: {aluno.nome}")
                print(f"Idade: {aluno.idade}")
                print(f"Plano: {aluno.plano}")
                print(f"Ativo: {aluno.ativo}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 4:

            try:

                print("\nSistema de Atualização")

                id_aluno = int(input("Digite seu ID: "))
                nome = input("Qual o novo nome: ")
                idade = int(input("Qual a nova idade: "))
                plano = input("Qual o novo plano: ")

                aluno = aluno_service.atualizar(
                    nome,
                    idade,
                    plano,
                    id_aluno
                )

                print("\nDados atualizados!")
                print(f"ID: {aluno.id_aluno}")
                print(f"Nome: {aluno.nome}")
                print(f"Idade: {aluno.idade}")
                print(f"Plano: {aluno.plano}")
                print(f"Ativo: {aluno.ativo}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 5:

            try:

                id_aluno = int(
                    input("Digite o ID que você quer deletar: ")
                )

                aluno = aluno_service.deletar(id_aluno)

                print(
                    f"Aluno {aluno.nome} deletado com sucesso!"
                )

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 6:

            try:

                id_aluno = int(
                    input("Informe o ID para ativação: ")
                )

                aluno = aluno_service.ativar(id_aluno)

                print(
                    f"Aluno {aluno.nome} ativado com sucesso!"
                )

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 7:

            try:

                id_aluno = int(
                    input("Informe o ID para desativação: ")
                )

                aluno = aluno_service.desativar(id_aluno)

                print(
                    f"Aluno {aluno.nome} desativado com sucesso!"
                )

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 8:

            try:

                nome = input("Informe o nome para buscar: ")

                alunos = aluno_service.buscar_por_nome(nome)

                for aluno in alunos:

                    print("------------------------")
                    print(f"ID: {aluno.id_aluno}")
                    print(f"Nome: {aluno.nome}")
                    print(f"Idade: {aluno.idade}")
                    print(f"Plano: {aluno.plano}")
                    print(f"Ativo: {aluno.ativo}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 9:

            try:

                plano = input("Informe o plano para buscar: ")

                alunos = aluno_service.buscar_por_plano(plano)

                for aluno in alunos:

                    print("------------------------")
                    print(f"ID: {aluno.id_aluno}")
                    print(f"Nome: {aluno.nome}")
                    print(f"Idade: {aluno.idade}")
                    print(f"Plano: {aluno.plano}")
                    print(f"Ativo: {aluno.ativo}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case 10:

            print("Encerrando Sistema...")
            break

        case _:

            print("Opção inválida.")