# 동적페이지 크롤링
# - 웹페이지 자료가 대기 상태 / 이벤트가 있는 경우

# [1] 설치
# pip install playwright  # 파이썬 라이브러리
# playwright install

# [2] 라이브러리
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 동적웹피이지 크롤링 라이브러리 
import pandas as pd

# [3] 크롤링 주소  "https://search.naver.com/search.naver?where=image&query=%EC%A7%B1%EA%B5%AC"
#  박스 : tile_item  , 이미지 : _fe_image_tab_content_thumbnail_image , 제목  : info_title

# [4] 비동기 웹크롤링

async def naverRun() :  # 동기화된 함수
    # (1) playwright 실행하고 p 변수에 결과 받기
    async with async_playwright() as p :    # 
        # (2) await(대기) 상태를 이용한 크롬 실행  , await p.chromium.launch()
        # haedless = False : 브라우저가 직접 실행된다. <봇차단 방지>
        brower = await p.chromium.launch(headless=False)

        # (3) 실행된 브라우저 ( chromium ) 에서 새로운 페이지에 지정한 URL을 대입하여 이동
        url = "https://search.naver.com/search.naver?where=image&query=짱구"    # url
        page = await brower.new_page()                                                        # 새로운 페이지 (탭) 열기
        await page.goto(url)                                                                  # 이동할 url

        # (4) (자료가 표시될 때까지 기다리기) 대기상태 만들기 ,
        # (4-1) 스크롤 내리기 이벤트(JS)
        for i in range(2) :   # 스크롤 2번 내리기

        # page.wait_for_timeout(밀리초) : 시스템 (인터넷속도)에 따라 적절하게 지정
            await page.wait_for_timeout(3000)
            # window(브라우저).scrollTo(시작위치, 이동위치)
            # 이동위치 : document(현재html).body(본문).scrollHeight(스크롤높이) : 즉 현재 브라우저 스크롤을 가장 하단으로 이동 
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")    # await page.evaluate("JS코드")

        # (5) 실행된 페이지에서 지정한 요소 가져오기
        # page.query_selector_all(식별자) 여러개 , page.query_selecter (식별자) 한개
        items = await page.query_selector_all('.tile_item')
        
        image_list = []
        for item in items :   # 여러개 item 에서 제목과 이미지 가져오기
             title_tag = await item.query_selector('.info_title .txt')                
             image_title = await title_tag.inner_text() if title_tag else "제목없음" # 제목 

             # css 선택자 : #id , .class , 마크업 , 마크업.class , 
             image_tag = await item.query_selector('img._fe_image_tab_content_thumbnail_image')  # 이미지
             image_link = await image_tag.get_attribute('src') if title_tag else "링크없음"   # get_attribut('속성명')

             image_list.append(
             {'제목' :image_title , '링크' :image_link }
             )
             

        print(image_list) # 확인 

        # (*) (직접) 안전하기 브라우저 닫기
        await brower.close()
asyncio.run(naverRun())  # 동기화된 함수 실행