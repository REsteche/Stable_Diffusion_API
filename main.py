import uvicorn

from app import app

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)