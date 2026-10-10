from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel, field_validator
from apps.repositories.aluno_repository import AlunoRepository
from apps.services.aluno_service import AlunoService

app = FastAPI()

aluno_repository = AlunoRepository()
aluno_service = AlunoService(aluno_repository)

# Buscar por ID
@app.get("/alunos/{id_aluno}")
def buscar_por_id(id_aluno: int):
    aluno = aluno_service.buscar_por_id(id_aluno)
    if aluno is None:
        raise HTTPException(status_code = 404, detail = "ID aluno não encontrado")
    return aluno

# Listar Alunos no Banco - PostgresSQL
@app.get("/alunos")
def listar_alunos():
    alunos = aluno_service.listar()
    return alunos

# Criando Aluno entrada
class AlunoEntrada(BaseModel):
    nome: str
    idade: int
    plano: str

    @field_validator("nome")
    @classmethod
    def validar_nome(cls,nome):
        nome = nome.lower().strip()
        if nome == "":
            raise ValueError("Nome não pode está vazio!")
        return nome

    @field_validator("idade")
    @classmethod
    def validar_idade(cls,idade):
        if idade <=0:
            raise ValueError("Idade não pode ser negativa e nem zero")
        return idade
    
    @field_validator("plano")
    @classmethod
    def validar_plano(cls,plano):
        plano = plano.lower().strip()
        if plano not in ("básico", "intermediário", "pro"):
            raise ValueError("Plano Inválido!")
        return plano

# Criando aluno
@app.post("/alunos",status_code=status.HTTP_201_CREATED)
def cadastrar_alunos(alunoEntrada: AlunoEntrada):
    cadastro = aluno_service.cadastrar(alunoEntrada.nome,alunoEntrada.idade,alunoEntrada.plano)
    return cadastro

# Atualizando aluno
@app.put("/alunos/{id_aluno}")
def atualizar_aluno(id_aluno: int, alunoEntrada: AlunoEntrada):
    atualizar_aluno = aluno_service.atualizar(alunoEntrada.nome,alunoEntrada.idade,alunoEntrada.plano,id_aluno)
    if atualizar_aluno is None:
        raise HTTPException( status_code = 404 , detail = "Não foi possivel atualizar o Aluno")
    return atualizar_aluno

