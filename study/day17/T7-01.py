# 웹 크롤링 : 웹페이지에 존재하는 데이터들을 수집하는 기술 
# 기초 지식 : html/css (식별자) 필요 
# 파이썬 크롤링 라이브러리 : request, BeautifulSoup 정적 / Selenium, Playwright 동적(js/대기)
# 크로링(로봇) 허용 여부 확인 : 도메인/robots.txt 사용
#   예] https://www.jobkorea.co.kr/robots.txt , Disallow 불가능 , Allow 가능
# 적절한 크롤링은 윤리적으로 사용하기 

# [1] HTML/CSS  식별자(마크업, #id, .class, 자손선택자 띄어쓰기 , 자식선택자 >) 찾기 
# 개발자도구 -> [F12] -> 왼쪽 상단에 마우스아이콘 ( CTRL + SHIFT + C ) 클릭 

# [2] 파이썬 크롤링
# 네이버 검색어 -> 안양 날씨 -> 현재 날씨 크롤링

# 1. 주소 : https://search.naver.com/search.naver?query=안양날씨
#   - 쿼리스트링(주소상에 변수) : URL?변수명=값&변수명=값  , 필요한 변수만 정리해서 가져오기
#   - url에서는 한국어가 불가능해서 인코딩해야함
# 2. 크롤링 선택자 : .temperature 

# [3] 정적 라이브러리 
import requests                 # URL 요청 라이브러리
from bs4 import BeautifulSoup   # 요청된 URL의 HTML 조작 라이브러리

# (1) requests.get(url)
response = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%95%88%EC%96%91%EB%82%A0%EC%94%A8")
print(response)

# (2) 요청(200)된 url에서 HTML 형식으로 파싱하기, BeautifulSoup( response.text, "html.parser")
soup = BeautifulSoup( response.text, "html.parser")
# print(soup)

# (3) 가젼온 HTML 에서 특정한 요소(식별자)만 가져오기 , soup.select_one (식별자)
txt_temp = soup.select_one('.txt_temp')
print(txt_temp)

# (4) 가져온 요소에서 텍스트만 추출 , <마크업> * 텍스트* </마크업> , 요소변수.get_text()
print(txt_temp.get_text())