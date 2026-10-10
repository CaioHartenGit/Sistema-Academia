from fastapi import FastAPI,HTTPException
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