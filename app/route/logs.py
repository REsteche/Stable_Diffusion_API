from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(
    tags=["/stable-diffusion/logs"],
    responses={400: {'description': 'Bad Request'}}
)

@router.get("/stable-diffusion/logs", response_class = PlainTextResponse)
async def get_logs():
   
    response = open("app/performance/logfile_ster.log", "r", encoding = "utf-8").read()
    
    return response