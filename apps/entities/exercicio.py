class Exercicio:
    def __init__(self,id_exercicio,nome,series,repeticoes,id_treino):
        self.id_exercicio = id_exercicio
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes
        self.id_treino = id_treino


    @property 
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,Novonome):
        if not isinstance(Novonome, str):
            raise ValueError("Nome do exercicio precisa ser válido")
        Novonome = Novonome.strip().lower()
        if Novonome == "":
            raise ValueError("Nome do exercicio não pode ser vazio")
        if len(Novonome) > 100:
            raise ValueError("Limite máximo de caracter atingido")
        self._nome = Novonome

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self,NovaSerie):
        if not isinstance(NovaSerie, int):
            raise ValueError("Erro! digite um valor válido para serie")
        if NovaSerie <= 0:
            raise ValueError("Serie não pode ser negativa")
        self._series = NovaSerie

    @property
    def repeticoes(self):
        return self._repeticoes 

    @repeticoes.setter
    def repeticoes(self,repeticoes):
        if not isinstance(repeticoes, int):
            raise ValueError("Repetições precisam ser números inteiros")
        if repeticoes <=0:
            raise ValueError("Repetições precisam não podem ser negativas ou zero")
        self._repeticoes = repeticoes

    @property
    def id_treino(self):
        return self._id_treino

    @id_treino.setter
    def id_treino(self,id_treino):
        if not isinstance(id_treino, int):
            raise ValueError("ID treino preciso ser um número inteiro")
        if id_treino <= 0:
            raise ValueError("ID treino não pode ser negativo")
        self._id_treino = id_treino

  