import pandas as pd
import httpx   # HTTP 통신
# 6. 서비스 : 비지니스 로직 
class ProductService :
    # 생성자 
    def __init__(self) :
        self.df = pd.DataFrame([
            {'id':1 , 'name' : '콜라', 'price':1200},
             {'id':2 , 'name' : '사이다', 'price':1000}
        ])


# 7. 서비스 함수 
    def products(self):
        return self.df.to_dict(orient='records')
    


# 8. 외부 서버 (API E또는 스프링)와 통신하기
# httpx.AsyncClient() vs axios()
    async def getSpring(self) : 
        async with httpx.AsyncClient() as client :
           response = await client.get("https://localhost:8080/api/product") # 통신할 스프링 주소
           print(response)
           return response.json()


ProductService = ProductService()  # 서비스 객체 생성