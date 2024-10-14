# fastapi_ex
fastapi practice

from fastapi import FastAPI

#fastapi 객체 생성
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"fastapi"}

# uvicorn main module name:FastApi instance name -- reload
# --reload : 코드가 수저되면 서버에 자동 로딩

# 실행방법
# uvicorn main:app --reload
