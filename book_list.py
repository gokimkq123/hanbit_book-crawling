import sys
import re
from urllib.request import urlopen
from html import unescape

f = urlopen('http://hanbit.co.kr/store/books/full_book_list.html')
file = open('dp.html', 'w')

encoding = f.info().get_content_charset(failobj="utf-8")
# HTTP 헤더를 기반으로 인코딩 방식 추출(값이 없다면 utf-8을 기본으로 사용)

print('encoding:', encoding, file=sys.stderr)
# 인코딩 방식을 표준 오류에 출력

text = f.read().decode(encoding)
# 추출한 인코딩 방식으로 디코딩

html = text
# html에 text 내용 저장

for temp_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # re.findall을 사용해 도서 하나에 해당하는 HTML을 추출

    url = re.search(r'<a href="(.*?)">', temp_html).group(1)
    url = 'http://hanbit.co.kr' + url
    # 도서의 url을 추출

    title = re.sub(r'<.*?>', '', temp_html)
    title = unescape(title)
    # 태그를 제거해서 도서의 제목을 추출
    print('url:', url)
    print('title:', title)
    print('-----')
