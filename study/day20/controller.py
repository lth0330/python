# 3. 라우터 : 앱(서버)와 연결되는 라우터
from fastapi import APIRouter

router = APIRouter(prefix='/api')


# 서비스 객체 호출
from service import ProductService

# 5. HTTP 매핑 
@router.get("/products")
async def products():
    return ProductService.products()

@router.get("/spring")
async def getspring():
    return await ProductService.getSpring()
