from importlib.resources import contents
from fastapi import APIRouter
from app.text_model import Text
from fastapi.encoders import jsonable_encoder
from app.performance.logs_metrics_config import logs, metrics
from fastapi.responses import FileResponse, Response
from starlette.background import BackgroundTask
from app.utils import cleanup
from app.image_ST_model import ImageSTModel
from app.database.redis_manager import RedisManager

router = APIRouter(
    tags=["/stable-diffusion/image"],
    responses={400: {'description': 'Bad Request'}}
)

imageModel =  ImageSTModel()   
redis = RedisManager()

@router.post("/stable-diffusion/image")
async def post_image(request: Text):
    
    metrics.tracing_start()
    message_request = 'POST /stable-diffusion/image'
    logs.set_message(message_request+" "+str((99-len(message_request))*"*"))
    text = request.text
    
    logs.set_message('Input Word: %s', [text])
    metrics.tracing_start()
    
    image_content = redis.get(text)
    
    if not image_content:
        logs.set_message('Word is not in cache')
        
        try:
            filename = imageModel.get_image(text)
            with open(filename, 'rb') as fimage:
                img_bytes = fimage.read()
                redis.store(text,img_bytes)
            
            resp_image = FileResponse(filename, background=BackgroundTask(cleanup, filename))

        except KeyError as error:
            logs.set_message('Error: %s', [error])
            resp_image = jsonable_encoder({"msg": "No image for this word!"})
    
    else:
        resp_image = Response(content=image_content, media_type="image/jpg", status_code=200)
               
    peak, time = metrics.tracing_mem()
    logs.set_message('image.get_image: |Peak: %f (MB) | Time: %f (s)|', [peak, time])

    metrics_values = metrics.calculate_metrics()
    logs.set_message('RESOURCES: |CPU: %f | Memory: %f | Peak (MB): %f | Time (s): %f|', metrics_values)
    
    return resp_image
