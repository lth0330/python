from fastapi import FastAPI
import uvicorn

app = FastAPI()

# (3) FsatApi 객체로 uvicorn 서버 실행 
if __name__ == "__main__":
    uvicorn.run( 'app:app' , host='127.0.0.1' 
                , port=8000 , reload=True )

# (4) 라우터 연결 : 다른 .py 에서 정의한 router객체를 합치기
# .include_router( 연결할 라우터 )
import controller
app.include_router( controller.router )