from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,field_validator
from apps.repositories.exercicio_repository import ExercicioRepository
from apps.services.exercicio_service import ExercicioService

app = FastAPI()

exercicio_repositorio = ExercicioRepository()
exercicio_service = ExercicioService(exercicio_repositorio)


# Buscar exercicio por ID
@app.get("/exercicios/{id_exercicio}")
def buscar_por_id(id_exercicio: int):
    exercicio = exercicio_service.listar_por_id(id_exercicio)
    if exercicio is None:
        raise HTTPException(
            status_code = 404,
            detail= "ID do exercicio não encontrado"
        )
    return exercicio

# Criar exercicios
class ExercicioEntrada(BaseModel):
    nome:  str
    serie: int
    repeticoes: int



