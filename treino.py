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
    def nome(self,NOVOnome):
        if not isinstance(NOVOnome, str):
            raise ValueError("Nome inválido")
        if NOVOnome.strip() == "":
            raise ValueError("Campo nome não pode ser vazio")
        if len(NOVOnome) > 50:
            raise ValueError("Quantidade de caracter excedida ")
        self._nome = NOVOnome

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
    def dia_semana(self,NovoDIASEMANA):
        if not isinstance(NovoDIASEMANA, str):
            raise ValueError("Nome inválido")
        if NovoDIASEMANA.strip() == "":
            raise ValueError("Campo nome não pode ser vazio")
        if len(NovoDIASEMANA) > 20:
            raise ValueError("Quantidade de caracter excedida")
        self._dia_semana = NovoDIASEMANA
        
