from fastapi import APIRouter

router = APIRouter(
    tags=["/stable-diffusion/health"],
    responses={400: {'description': 'Bad Request'}}
)

@router.get("/stable-diffusion/health")
async def perfom_healthcheck():
    return {"health":"application OK"}