
# app.py : FastAPI 실행하는 파일
from fastapi import FastAPI
import uvicorn

# 1. FastApi 객체 생성
app = FastAPI() 

# 2. uvicorn.run('파일명:app') 서버 실행
if __name__ == '__main__' :
    uvicorn.run('app:app', host = '127.0.0.1',
            port=8000, reload=True )
    
# 3. 라우터 : 여러개 controller 파일들을 하나의 앱(서버) 연결하는 방법 
import controller
app.include_router(controller.router)


