from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='WebPOS作成プロトタイプ',
    description='FastAPIでWebPOSシステムを構築',
    version='0.0.1 beta'
)


def index(request: Request):
    return{'Hello': 'world'}

