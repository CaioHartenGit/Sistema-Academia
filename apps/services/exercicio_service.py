from apps.entities.exercicio import Exercicio
from apps.repositories.exercicio_repository import ExercicioRepository

class ExercicioService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, nome, series, repeticoes, id_treino):
        exercicio = Exercicio(
            None,
            nome,
            series,
            repeticoes,
            id_treino
        )

        exer = self.repository.inserir_cadastrar(
            exercicio.nome,
            exercicio.series,
            exercicio.repeticoes,
            exercicio.id_treino
        )

        return exer

    def listar_por_id(self, id_treino):
        exer = self.repository.listar_por_id(id_treino)
        return exer

    def atualizar(self, id_exercicio, nome, series, repeticoes):
        exercicio = self.repository.atualizar(
            id_exercicio,
            nome,
            series,
            repeticoes
        )

        return exercicio

    def deletar(self, id_exercicio):
        exercicio = self.repository.deletar(id_exercicio)
        return exercicio