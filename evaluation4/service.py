import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt 
import koreanfont # 그래프 한글 꺠짐 방지
#book_list=[]
#for page in range(1 , 10) :
# url = f' https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=120'
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text , "html.parser")
# books = soup.select('#yesBestList > li')
#
# for book in books : 
#    gd_name = book.select_one('.gd_name').get_text().strip()
#    yes_b = book.select_one('.yes_b').get_text().strip()
#    saleNum = book.select_one('.saleNum').get_text().strip()
#    info_date = book.select_one('.info_date').get_text().strip()
# 
#    book_list.append({"제목": gd_name, "가격" : yes_b , "판매지수" :saleNum ,"출판년월" : info_date})
#
# time.sleep(2)
#
# df = pd.DataFrame(book_list)

# df.to_csv("evaluation4/data/book.csv",
#         header=True)


df = pd.read_csv('evaluation4/data/book.csv',
                 header=0,                
                 encoding='utf-8',          
                                   )   

df['가격'] = df['가격'].str.replace( ',' , '' )
df['가격'] = df['가격'].astype(int)


df['출판년'] = df['출판년월'].str.split('년').str[0]
df['출판월'] = df['출판년월'].str.slice(start=5)
df['출판년'] = df['출판년'].astype(int)

print(df['가격'].mean())
print(df['가격'].max())
print(df['가격'].min())

print(df['출판년'].value_counts().sort_index())


# 나. 가격대별 도서 개수 출력
# 0~1만원, 1~2만원처럼 가격을 구간으로 나눕니다.
bins = [0, 10000, 20000, 30000, 40000, 50000, float('inf')]
labels = ['0~1만원', '1~2만원', '2~3만원', '3~4만원', '4~5만원', '5만원 이상']

df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels)
개수 = df['가격대'].value_counts().sort_index()


plt.bar(개수.index, 개수.values)
plt.xlabel('가격대')
plt.ylabel('도서 개수')
plt.title('가격대별 도서 개수')
plt.show()


df['년도별'] = pd.cut(df['출판년'],bins=[1990,2000,2010,2020,2030],labels=["~2000 ","2000~2010","2010~2020","2020 ~"])
년도 = df['년도별'].value_counts().sort_index()


plt.bar(년도.index, 년도.values)
plt.xlabel('년도별')
plt.ylabel('도서 개수')
plt.title('년도별 도서 개수')
plt.show()


