import uvicorn
from fastapi import FastAPI
from routers import include_routers


app = FastAPI()

include_routers(app)



if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)