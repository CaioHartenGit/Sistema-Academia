from fastapi import APIRouter, status
from apps.schemas.alunos_schemas import AlunoCreate, AlunoResponse
from apps.repositories.aluno_repository import AlunoRepository
from apps.services.aluno_service import AlunoService


aluno_repository = AlunoRepository()
aluno_service = AlunoService(aluno_repository)

router = APIRouter(prefix = "/alunos", tags = ["Alunos"])

# Criar aluno 
@router.post("/",status_code = status.HTTP_201_CREATED, response_model = AlunoResponse)
def cadastrar_alunos(alunoCreate: AlunoCreate):
    cadastro_aluno = aluno_service.cadastrar(alunoCreate.nome,alunoCreate.idade,alunoCreate.plano)
    return cadastro_aluno

# Listar Alunos no Banco - PostgtesSQL
@router.get("/", response_model = list [AlunoResponse])
def listar_alunos():
    listar_aluno = aluno_service.listar()
    return listar_aluno

# Buscar por ID
@router.get("/{id_aluno}", response_model = AlunoResponse)
def buscar_por_id(id_aluno: int):
    aluno = aluno_service.buscar_por_id(id_aluno)
    return aluno






























'''
from fastapi import FastAPI,HTTPException,status
from apps.repositories.aluno_repository import AlunoRepository
from apps.services.aluno_service import AlunoService
from apps.schemas.alunos_schemas import AlunoCreate

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

# Criando aluno
@app.post("/alunos",status_code=status.HTTP_201_CREATED)
def cadastrar_alunos(alunoEntrada: AlunoCreate):
    cadastro = aluno_service.cadastrar(alunoEntrada.nome,alunoEntrada.idade,alunoEntrada.plano)
    return cadastro

# Atualizando aluno
@app.put("/alunos/{id_aluno}")
def atualizar_aluno(id_aluno: int, alunoEntrada: AlunoCreate):
    atualizar_aluno = aluno_service.atualizar(alunoEntrada.nome,alunoEntrada.idade,alunoEntrada.plano,id_aluno)
    if atualizar_aluno is None:
        raise HTTPException( status_code = 404 , detail = "Não foi possivel atualizar o Aluno")
    return atualizar_aluno

# Deletando aluno no Sistema
@app.delete("/alunos/{id_aluno}")
def deletar_aluno(id_aluno: int):
    deleta = aluno_service.deletar(id_aluno)
    if deleta is not None:
        return{
            "Mensagem": "Aluno deletado com sucesso",
        }
    else:
       raise HTTPException(
           status_code = 404,
           detail = "Aluno não foi encontrado!"
       )

# Ativando aluno no Sistema
@app.patch("/alunos/{id_aluno}/ativar")
def ativar_aluno(id_aluno: int):
    ativar = aluno_service.ativar(id_aluno)
    if ativar is not None:
        return{
            "Mensagem": "Aluno ativado com sucesso"
        }
    else:
        return{
            "Mensagem": "Aluno não encontrado"
        }

# Desativando aluno no Sistema
@app.patch("/alunos/{id_aluno}/desativar")
def desativar_aluno(id_aluno: int):
    desativar = aluno_service.desativar(id_aluno)
    if desativar is not None:
        return{
            "Mensagem": "Aluno desativado com sucesso"
        }
    else:
        return{
            "Mensagem": "Aluno não encontrado"
        }
'''