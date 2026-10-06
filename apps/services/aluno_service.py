from apps.entities.aluno import Aluno
from apps.repositories.aluno_repository import AlunoRepository

class AlunoService:

    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def _converter_aluno(dados):
        if dados is None:
            return None

        return Aluno(*dados)

    def cadastrar(self, nome, idade, plano):
        aluno = Aluno(None, nome, idade, plano)

        dados = self.repository.inserir(
            aluno.nome,
            aluno.idade,
            aluno.plano
        )

        return self._converter_aluno(dados)

    def listar(self):
        return [
            self._converter_aluno(dados)
            for dados in self.repository.listar()
        ]

    def buscar_por_id(self, id_aluno):
        dados = self.repository.buscar_por_id(id_aluno)
        return self._converter_aluno(dados)

    def buscar_por_nome(self, nome):
        return [
            self._converter_aluno(dados)
            for dados in self.repository.buscar_por_nome(nome)
        ]

    def buscar_por_plano(self, plano):
        return [
            self._converter_aluno(dados)
            for dados in self.repository.buscar_por_plano(plano)
        ]

    def atualizar(self, nome, idade, plano, id_aluno):
        dados = self.repository.atualizar(
            nome,
            idade,
            plano,
            id_aluno
        )

        return self._converter_aluno(dados)

    def deletar(self, id_aluno):
        dados = self.repository.deletar(id_aluno)
        return self._converter_aluno(dados)

    def ativar(self, id_aluno):
        dados = self.repository.ativar(id_aluno)
        return self._converter_aluno(dados)

    def desativar(self, id_aluno):
        dados = self.repository.desativar(id_aluno)
        return self._converter_aluno(dados)