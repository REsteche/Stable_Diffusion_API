from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest
from app.performance.logs_metrics_config import metrics

router = APIRouter(
    tags=["/stable-diffusion/metrics"],
    responses={400: {'description': 'Bad Request'}}
)

@router.get("/stable-diffusion/metrics", response_class = PlainTextResponse)
async def get_metrics():
    res = set()
    res.add(generate_latest(metrics.couter).decode('UTF-8'))
    res.add(generate_latest(metrics.histogram).decode('UTF-8'))
    res.add(generate_latest(metrics.gauge).decode('UTF-8'))
    response = "".join(res)
    return response