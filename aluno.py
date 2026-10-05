class Aluno:

    def __init__(self, id_aluno, nome, idade, plano, ativo=True):

        self.id_aluno = id_aluno
        self.nome = nome
        self.idade = idade
        self.plano = plano
        self.ativo = ativo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):

        if not isinstance(novoNome, str):
            raise ValueError("Escreva corretamente seu nome")

        novoNome = novoNome.strip()

        if novoNome == "":
            raise ValueError("Nome não pode ser vazio")

        self._nome = novoNome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, novaIdade):

        if not isinstance(novaIdade, int):
            raise ValueError("Escreva corretamente sua idade")

        if novaIdade <= 0:
            raise ValueError("Idade não pode ser menor ou igual a zero")

        self._idade = novaIdade

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, novoPlano):

        if not isinstance(novoPlano, str):
            raise ValueError("Escreva corretamente seu plano")

        novoPlano = novoPlano.strip()

        if novoPlano.lower() not in ("Básico", "Intermediário", "Pro"):
            raise ValueError("Plano inválido! Verifique e tente novamente")

        self._plano = novoPlano

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, novoAtivo):

        if not isinstance(novoAtivo, bool):
            raise ValueError("Ativo deve ser True ou False")

        self._ativo = novoAtivo