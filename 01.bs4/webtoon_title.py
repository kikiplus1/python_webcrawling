from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re,os

try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image')) #현재 코드에 image파일 생성
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')

soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1_list = soup.findAll('div', {'class':'col_inner'})
# pprint(data1)

li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll('li'))

# pprint(li_list)

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) #해당 영역 글자가 아닌것은 ''으로 치환하기
    print(title,img_src)

    urlretrieve(img_src , './image/'+title+'.jpg') #주소, 파일경로+확장자