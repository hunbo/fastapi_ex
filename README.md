# 🚀 FastAPI 연습 프로젝트

이 프로젝트는 **FastAPI**를 사용해 간단한 API를 연습한 것입니다.  
`Hello, FastAPI!` 메시지와 **경로 및 쿼리 매개변수**를 활용해 데이터를 반환합니다.

---

## 🛠️ 설치 및 실행 방법
1. **의존성 설치**:
   pip install fastapi uvicorn

2. **서버 실행**:
   uvicorn main:app --reload

3. **접속**:
   브라우저에서 http://127.0.0.1:8000로 접속


📄 API 엔드포인트
1. 🌐 루트 경로
   - URL: GET /
   - 응답 : { "hello": "fastapi" }
  
2. 📦 아이템 조회 경로
   - URL: GET /items/{item_id}
   - 경로 매개변수:
     item_id (정수형): 조회할 아이템의 ID
   - 쿼리 매개변수 (선택):
     q (문자열): 추가 쿼리 정보
   - 예시 요청:
     http://127.0.0.1:8000/items/123?q=hunbo
   - 응답:
     { "item_id": 123, "q": "hunbo" }

💻 코드 예시

from fastapi import FastAPI

from typing import Union

app = FastAPI()

@app.get("/")

def read_root():

    return {"hello": "fastapi"}

@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}


🎯 목표
- FastAPI 기본 사용법 익히기
- 경로 매개변수와 쿼리 매개변수 연습

📚 참고 자료
- FastAPI 공식 문서
- Uvicorn 공식 문서

