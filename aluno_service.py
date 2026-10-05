from aluno import Aluno

class AlunoService:

    def __init__(self, repository):

        self.repository = repository

    def cadastrar(self, nome, idade, plano):

        # Cria primeiro para validar os dados
        aluno = Aluno(
            None,
            nome,
            idade,
            plano
        )

        # Usa os valores já validados e tratados pelo Model
        dados = self.repository.inserir(
            aluno.nome,
            aluno.idade,
            aluno.plano
        )

        aluno.id_aluno = dados[0]

        return aluno

    def listar(self):

        dados = self.repository.listar()

        lista_alunos = []

        for d in dados:

            aluno = Aluno(
                d[0],
                d[1],
                d[2],
                d[3],
                d[4]
            )

            lista_alunos.append(aluno)

        return lista_alunos

    def buscar_por_id(self, id_aluno):

        dados = self.repository.buscar_por_id(id_aluno)

        if dados is None:
            raise ValueError("ID do aluno não encontrado")

        aluno = Aluno(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4]
        )

        return aluno

    def atualizar(self, nome, idade, plano, id_aluno):

        # Valida antes de mandar para o banco
        Aluno(
            id_aluno,
            nome,
            idade,
            plano
        )

        dados = self.repository.atualizar(
            nome.strip(),
            idade,
            plano.strip(),
            id_aluno
        )

        if dados is None:
            raise ValueError("Aluno não encontrado")

        aluno = Aluno(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4]
        )

        return aluno

    def deletar(self, id_aluno):

        dados = self.repository.deletar(id_aluno)

        if dados is None:
            raise ValueError("ID do aluno não encontrado")

        aluno = Aluno(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4]
        )

        return aluno

    def ativar(self, id_aluno):

        dados = self.repository.buscar_por_id(id_aluno)

        if dados is None:
            raise ValueError("ID do aluno não encontrado")

        if dados[4]:
            raise ValueError("Aluno já está ativo")

        dados = self.repository.ativar(id_aluno)

        aluno = Aluno(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4]
        )

        return aluno

    def desativar(self, id_aluno):

        dados = self.repository.buscar_por_id(id_aluno)

        if dados is None:
            raise ValueError("ID do aluno não encontrado")

        if not dados[4]:
            raise ValueError("Aluno já está desativado")

        dados = self.repository.desativar(id_aluno)

        aluno = Aluno(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4]
        )

        return aluno

    def buscar_por_nome(self, nome):

        dados = self.repository.buscar_por_nome(nome)

        if not dados:
            raise ValueError("Nenhum aluno encontrado com esse nome")

        lista_alunos = []

        for d in dados:

            aluno = Aluno(
                d[0],
                d[1],
                d[2],
                d[3],
                d[4]
            )

            lista_alunos.append(aluno)

        return lista_alunos

    def buscar_por_plano(self, plano):

        dados = self.repository.buscar_por_plano(plano)

        if not dados:
            raise ValueError("Nenhum aluno encontrado com esse plano")

        lista_alunos = []

        for d in dados:

            aluno = Aluno(
                d[0],
                d[1],
                d[2],
                d[3],
                d[4]
            )

            lista_alunos.append(aluno)

        return lista_alunos