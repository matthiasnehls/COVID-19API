"""Run the api"""
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import root

app = FastAPI(
    title="DGC-API-BREACHES ",
    description="## DGC-API-BREACHES \n\n ### Project Repo: [Github]("
                "https://github.com/dgc-ag)",
    debug=False
)

if __name__ == "__main__":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=root, prefix="/api")
    uvicorn.run(app, host="127.0.0.1", port=8899)
