from apps.repositories.aluno_repository import AlunoRepository
from apps.services.aluno_service import AlunoService
from apps.repositories.treino_repository import TreinoRepository
from apps.services.treino_service import TreinoService
from apps.repositories.exercicio_repository import ExercicioRepository
from apps.services.exercicio_service import ExercicioService

# ============================================================

# REPOSITORIES

# ============================================================

aluno_repository = AlunoRepository()
treino_repository = TreinoRepository()
exercicio_repository = ExercicioRepository()

# ============================================================

# SERVICES

# ===========================================================

aluno_service = AlunoService(aluno_repository)
treino_service = TreinoService(treino_repository)
exercicio_service = ExercicioService(exercicio_repository)

# ===========================================================

# FUNÇÕES AUXILIARES

# ============================================================

def pausar():

    input("\n        Pressione ENTER para continuar...")

def titulo(texto):

    print()

    print("╔══════════════════════════════════════════════════════╗")

    print(f"║{texto:^54}║")

    print("╚══════════════════════════════════════════════════════╝")

    print()

def menu_opcoes(opcoes):

    print("╔══════════════════════════════════════════════════════╗")

    for opcao in opcoes:

        print(f"║{opcao:^54}║")

    print("╚══════════════════════════════════════════════════════╝")

    print()

# ============================================================

# MENU ALUNO

# ============================================================

def menu_aluno():

    while True:

        titulo("👤 GERENCIAMENTO DE ALUNOS")

        menu_opcoes([

            "[ 1 ] Cadastrar aluno",

            "[ 2 ] Listar alunos",

            "[ 3 ] Buscar aluno por ID",

            "[ 4 ] Buscar aluno por nome",

            "[ 5 ] Buscar aluno por plano",

            "[ 6 ] Atualizar aluno",

            "[ 7 ] Deletar aluno",

            "[ 8 ] Ativar aluno",

            "[ 9 ] Desativar aluno",

            "[ 0 ] Voltar"

        ])

        opcao = input("  ➜ Escolha uma opção: ")

        match opcao:

            # ------------------------------------------------

            # CADASTRAR

            # ------------------------------------------------

            case "1":

                titulo("CADASTRAR ALUNO")

                nome = input("        Nome: ")

                idade = int(input("        Idade: "))

                plano = input("        Plano: ")

                aluno = aluno_service.cadastrar(

                    nome,

                    idade,

                    plano

                )

                print("\n        ✓ ALUNO CADASTRADO COM SUCESSO!")

                print(f"        ID:    {aluno.id_aluno}")

                print(f"        Nome:  {aluno.nome}")

                print(f"        Idade: {aluno.idade}")

                print(f"        Plano: {aluno.plano}")

                pausar()

            # ------------------------------------------------

            # LISTAR

            # ------------------------------------------------

            case "2":

                titulo("LISTA DE ALUNOS")

                alunos = aluno_service.listar()

                if not alunos:

                    print("        Nenhum aluno cadastrado.")

                else:

                    for aluno in alunos:

                        print(

                            f"        ID: {aluno.id_aluno} | "

                            f"Nome: {aluno.nome} | "

                            f"Idade: {aluno.idade} | "

                            f"Plano: {aluno.plano} | "

                            f"Ativo: {aluno.ativo}"

                        )

                pausar()

            # ------------------------------------------------

            # BUSCAR POR ID

            # ------------------------------------------------

            case "3":

                titulo("BUSCAR ALUNO POR ID")

                id_aluno = int(input("        ID do aluno: "))

                aluno = aluno_service.buscar_por_id(id_aluno)

                print("\n        ALUNO ENCONTRADO!")

                print(f"        ID:    {aluno.id_aluno}")

                print(f"        Nome:  {aluno.nome}")

                print(f"        Idade: {aluno.idade}")

                print(f"        Plano: {aluno.plano}")

                print(f"        Ativo: {aluno.ativo}")

                pausar()

            # ------------------------------------------------

            # BUSCAR POR NOME

            # ------------------------------------------------

            case "4":

                titulo("BUSCAR ALUNO POR NOME")

                nome = input("        Nome: ")

                alunos = aluno_service.buscar_por_nome(nome)

                for aluno in alunos:

                    print(

                        f"        ID: {aluno.id_aluno} | "

                        f"Nome: {aluno.nome} | "

                        f"Idade: {aluno.idade} | "

                        f"Plano: {aluno.plano}"

                    )

                pausar()

            # ------------------------------------------------

            # BUSCAR POR PLANO

            # ------------------------------------------------

            case "5":

                titulo("BUSCAR ALUNO POR PLANO")

                plano = input("        Plano: ")

                alunos = aluno_service.buscar_por_plano(plano)

                for aluno in alunos:

                    print(

                        f"        ID: {aluno.id_aluno} | "

                        f"Nome: {aluno.nome} | "

                        f"Plano: {aluno.plano}"

                    )

                pausar()

            # ------------------------------------------------

            # ATUALIZAR

            # ------------------------------------------------

            case "6":

                titulo("ATUALIZAR ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                nome = input("        Novo nome: ")

                idade = int(input("        Nova idade: "))

                plano = input("        Novo plano: ")

                aluno = aluno_service.atualizar(

                    nome,

                    idade,

                    plano,

                    id_aluno

                )

                print("\n        ✓ ALUNO ATUALIZADO COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # DELETAR

            # ------------------------------------------------

            case "7":

                titulo("DELETAR ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                aluno = aluno_service.deletar(id_aluno)

                print("\n        ✓ ALUNO DELETADO COM SUCESSO!")

                print(f"        ID:   {aluno.id_aluno}")

                print(f"        Nome: {aluno.nome}")

                pausar()

            # ------------------------------------------------

            # ATIVAR

            # ------------------------------------------------

            case "8":

                titulo("ATIVAR ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                aluno = aluno_service.ativar(id_aluno)

                print(f"\n        ✓ ALUNO {aluno.nome} FOI ATIVADO!")

                pausar()

            # ------------------------------------------------

            # DESATIVAR

            # ------------------------------------------------

            case "9":

                titulo("DESATIVAR ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                aluno = aluno_service.desativar(id_aluno)

                print(f"\n        ✓ ALUNO {aluno.nome} FOI DESATIVADO!")

                pausar()

            # ------------------------------------------------

            # VOLTAR

            # ------------------------------------------------

            case "0":

                break

            case _:

                print("\n        ✗ OPÇÃO INVÁLIDA!")

                pausar()

# ============================================================

# MENU TREINO

# ============================================================

def menu_treino():

    while True:

        titulo("🏋️ GERENCIAMENTO DE TREINOS")

        menu_opcoes([

            "[ 1 ] Cadastrar treino",

            "[ 2 ] Listar treinos",

            "[ 3 ] Buscar treinos do aluno",

            "[ 4 ] Alterar dia do treino",

            "[ 5 ] Deletar treinos do aluno",

            "[ 0 ] Voltar"

        ])

        opcao = input("        ➜ Escolha uma opção: ")

        match opcao:

            # ------------------------------------------------

            # CADASTRAR

            # ------------------------------------------------

            case "1":

                titulo("CADASTRAR TREINO")

                nome = input("        Nome do treino: ")

                dia_semana = input("        Dia da semana: ")

                id_aluno = int(input("        ID do aluno: "))

                treino_service.cadastrar(

                    nome,

                    dia_semana,

                    id_aluno

                )

                print("\n        ✓ TREINO CADASTRADO COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # LISTAR

            # ------------------------------------------------

            case "2":

                titulo("LISTA DE TREINOS")

                treinos = treino_service.listar()

                if not treinos:

                    print("        Nenhum treino cadastrado.")

                else:

                    for treino in treinos:

                        print(

                            f"        ID: {treino[0]} | "

                            f"Nome: {treino[1]} | "

                            f"Dia: {treino[2]} | "

                            f"Aluno: {treino[3]}"

                        )

                pausar()

            # ------------------------------------------------

            # BUSCAR POR ALUNO

            # ------------------------------------------------

            case "3":

                titulo("TREINOS DO ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                treinos = treino_service.buscar_por_id(id_aluno)

                if not treinos:

                    print("        Nenhum treino encontrado.")

                else:

                    for treino in treinos:

                        print(

                            f"        ID: {treino[0]} | "

                            f"Nome: {treino[1]} | "

                            f"Dia: {treino[2]}"

                        )

                pausar()

            # ------------------------------------------------

            # ALTERAR DIA

            # ------------------------------------------------

            case "4":

                titulo("ALTERAR DIA DO TREINO")

                id_aluno = int(input("        ID do aluno: "))

                dia_atual = input("        Dia atual: ")

                novo_dia = input("        Novo dia: ")

                treino = treino_service.alterar(

                    id_aluno,

                    dia_atual,

                    novo_dia

                )

                print("\n        ✓ DIA DO TREINO ALTERADO COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # DELETAR

            # ------------------------------------------------

            case "5":

                titulo("DELETAR TREINOS DO ALUNO")

                id_aluno = int(input("        ID do aluno: "))

                treino_service.deletar(id_aluno)

                print("\n        ✓ TREINOS DELETADOS COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # VOLTAR

            # ------------------------------------------------

            case "0":

                break

            case _:

                print("\n        ✗ OPÇÃO INVÁLIDA!")

                pausar()

# ============================================================

# MENU EXERCÍCIO

# ============================================================

def menu_exercicio():

    while True:

        titulo("💪 GERENCIAMENTO DE EXERCÍCIOS")

        menu_opcoes([

            "[ 1 ] Cadastrar exercício",

            "[ 2 ] Listar exercícios do treino",

            "[ 3 ] Atualizar exercício",

            "[ 4 ] Deletar exercício",

            "[ 0 ] Voltar"

        ])

        opcao = input("  ➜ Escolha uma opção: ")

        match opcao:

            # ------------------------------------------------

            # CADASTRAR

            # ------------------------------------------------

            case "1":

                titulo("CADASTRAR EXERCÍCIO")

                nome = input("        Nome do exercício: ")

                series = int(input("        Número de séries: "))

                repeticoes = int(input("        Número de repetições: "))

                id_treino = int(input("        ID do treino: "))

                exercicio_service.cadastrar(

                    nome,

                    series,

                    repeticoes,

                    id_treino

                )

                print("\n        ✓ EXERCÍCIO CADASTRADO COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # LISTAR

            # ------------------------------------------------

            case "2":

                titulo("EXERCÍCIOS DO TREINO")

                id_treino = int(input("        ID do treino: "))

                exercicios = exercicio_service.listar_por_id(

                    id_treino

                )

                if not exercicios:

                    print("        Nenhum exercício encontrado.")

                else:

                    for exercicio in exercicios:

                        print(

                            f"        ID: {exercicio[0]} | "

                            f"{exercicio[1]} | "

                            f"{exercicio[2]} séries x "

                            f"{exercicio[3]} repetições"

                        )

                pausar()

            # ------------------------------------------------

            # ATUALIZAR

            # ------------------------------------------------

            case "3":

                titulo("ATUALIZAR EXERCÍCIO")

                id_exercicio = int(

                    input("        ID do exercício: ")

                )

                nome = input("        Novo nome: ")

                series = int(

                    input("        Novas séries: ")

                )

                repeticoes = int(

                    input("        Novas repetições: ")

                )

                exercicio_service.atualizar(

                    id_exercicio,

                    nome,

                    series,

                    repeticoes

                )

                print("\n        ✓ EXERCÍCIO ATUALIZADO COM SUCESSO!")

                pausar()

            # ------------------------------------------------

            # DELETAR

            # ------------------------------------------------

            case "4":

                titulo("DELETAR EXERCÍCIO")

                id_exercicio = int(

                    input("        ID do exercício: ")

                )

                exercicio = exercicio_service.deletar(

                    id_exercicio

                )

                print("\n        ✓ EXERCÍCIO DELETADO COM SUCESSO!")

                print(f"        ID:   {exercicio[0]}")

                print(f"        Nome: {exercicio[1]}")

                pausar()

            # ------------------------------------------------

            # VOLTAR

            # ------------------------------------------------

            case "0":

                break

            case _:

                print("\n        ✗ OPÇÃO INVÁLIDA!")

                pausar()

# ============================================================

# MENU PRINCIPAL

# ============================================================

def menu_principal():

    while True:

        titulo("🏆 SISTEMA DE ACADEMIA")

        menu_opcoes([

            "[ 1 ] 👤 ALUNOS",

            "[ 2 ] 🏋️ TREINOS",

            "[ 3 ] 💪 EXERCÍCIOS",

            "[ 0 ] 🚪 SAIR"

        ])

        opcao = input(" ➜ Escolha uma opção: ")

        match opcao:

            case "1":

                menu_aluno()

            case "2":

                menu_treino()

            case "3":

                menu_exercicio()

            case "0":

                titulo("ENCERRANDO SISTEMA")

                print("        Obrigado por utilizar o sistema! 👋")

                break

            case _:

                print("\n        ✗ OPÇÃO INVÁLIDA!")

                pausar()

# ============================================================

# INICIAR SISTEMA

# ============================================================

if __name__ == "__main__":

    menu_principal()