class Treino:
    def __init__(self,id_treino,nome,dia_semana,id_aluno):
        self.id_treino = id_treino
        self.nome = nome 
        self.dia_semana = dia_semana # DIA
        self.id_aluno = id_aluno # ID 


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        if not isinstance(novoNome, str):
            raise ValueError("Nome inválido")
        novoNome = novoNome.strip().lower()
        if novoNome == "":
            raise ValueError("Campo nome não pode ser vazio")
        if len(novoNome) > 50:
            raise ValueError("Quantidade de caracteres excedida")
        self._nome = novoNome

    @property 
    def id_aluno(self):
        return self._id_aluno

    @id_aluno.setter
    def id_aluno(self,NovoID):
        if not isinstance(NovoID, int):
            raise ValueError("ID aluno precisa ser válido")
        if NovoID <= 0:
            raise ValueError("O ID aluno não pode ser negativo")
        self._id_aluno = NovoID

    @property
    def dia_semana(self):
        return self._dia_semana
    
   
    @dia_semana.setter
    def dia_semana(self, novoDiaSemana):
        if not isinstance(novoDiaSemana, str):
            raise ValueError("Dia da semana inválido")
        novoDiaSemana = novoDiaSemana.strip().lower()
        if novoDiaSemana.endswith("-feira"):
            novoDiaSemana = novoDiaSemana.replace("-feira", "")
        if novoDiaSemana == "":
            raise ValueError("Dia da semana não pode ser vazio")
        if len(novoDiaSemana) > 20:
            raise ValueError("Quantidade de caracteres excedida")
        self._dia_semana = novoDiaSemana
        
