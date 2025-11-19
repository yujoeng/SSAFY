import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'   # 알라딘 요청 api 입력 
API_KEY = 'ttbdnwjd8121139002'  # 내 api key 입력 

params = {
    'ttbkey': API_KEY,
    'QueryType' : 'ItemNewSpecial', # 주목할 만한 신간 리스트 
    'MaxResults' : 50,  # 최대 50권까지 응답 
    'SearchTarget': 'Book',   # 도서만 조회 
    'Output': 'js', # 응답을 json 형태로 받기
    'Version' : '20131101'   # 최신 버전의 api 사용 
}


# request로 알라딘 api_url을 호출하면 params 딕셔너리가 쿼리스트링으로 붙어서 전송됨 
response = requests.get(API_URL, params=params)
print('status_code:', response.status_code)
data = response.json()  
print('data 타입:', type(data))


items = data.get('item', [])   # 도서 목록 리스트 / data['item'] 에 도서 목록이 리스트로 들어있지만, 
print('item 개수:', len(items))                  # 응답을 json -> 파이썬 dict로 변환 
                               # []을 추가로 입력한 이유는 혹시라도 item 키가 없을 경우 에러 대신 빈 리스트를 받기 위해서 

for book in items:
    title = book.get('title')
    author = book.get('author')
    pub_date = book.get('pubDate')
    isbn = book.get('isbn13') or book.get('isbn')

    print(f'국제 표준 도서 번호: {isbn}')
    print(f'저자: {author}')
    print(f'제목: {title}')
    print(f'출간일: {pub_date}')
    print(f'-' * 40)