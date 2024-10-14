from fastapi import FastAPI
from typing import Union
import uvicorn

#fastapi 객체 생성
app = FastAPI()

#localhost:8000/,    get은 http 메소드 중 하나임. (데이터를 조회)
@app.get("/")
def read_root():
    return {"hello":"fastapi"}


#방법1 : python main.py
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)



#방법2
# uvicorn main module name:FastApi instance name -- reload
# --reload : 코드가 수저되면 서버에 자동 로딩
# uvicorn main:app --reload

# 경로매개 변수
#localhost:8000/items/1
#localhost:8000/items/2
#localhost:8000/items/aaa

#쿼리 매개 변수 : q:Union[str, None]=None
#http://127.0.0.1:8000/items/222?q="hunbo"
@app.get("/items/{item_id}")
def read_item(item_id:int, q:Union[str, None]=None):
    return{"item_id":item_id, "q":q}
