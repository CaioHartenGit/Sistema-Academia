from apps.entities.treino import Treino
from apps.repositories.treino_repository import TreinoRepository


class TreinoService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, nome, dia_semana, id_aluno):
        treino = Treino(None, nome, dia_semana, id_aluno)

        user = self.repository.inserir_Cadastrar(
            treino.nome,
            treino.dia_semana,
            treino.id_aluno
        )

        return user

    def listar(self):
        treinos = self.repository.listar()
        return treinos

    def buscar_por_id(self, id_aluno):
        treinos = self.repository.buscar_por_id(id_aluno)
        return treinos

    def alterar(self, id_aluno, dia_semana, NOVODIADASEMANA):
        treinos = self.repository.alterar_treino(
            id_aluno,
            dia_semana,
            NOVODIADASEMANA
        )

        return treinos

    def deletar(self, id_aluno):
        treinos = self.repository.delete_treino(id_aluno)
        return treinos