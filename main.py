import requests
from bs4 import BeautifulSoup


header = {'User-agent' : 'Mozila/2.0'}

keyword = '루테인'

know_li1 = []
know_li2 = []
know_li3 = []

know_count = 0

response2 = requests.get(
    f"https://search.naver.com/search.naver?ssc=tab.kin.kqna&where=kin&sm=tab_jum&query={keyword}", headers=header)
html2 = response2.text

soup2 = BeautifulSoup(html2, 'html.parser')
info_sub_li = soup2.select('a.question_text')

for info_sub in info_sub_li:
    if know_count < 3:
        res = requests.get(f"{info_sub['href']}", headers=header)
        know_html = res.text
        know_soup = BeautifulSoup(know_html,'html.parser')

        know_info = know_soup.select('span.c-userinfo__info')


        if know_count == 0: know_li1.append(know_info[0].text + ' ' +know_info[1].text)
        elif know_count == 1:   know_li2.append(know_info[0].text + ' ' +know_info[1].text)
        elif know_count == 2:   know_li3.append(know_info[0].text + ' ' +know_info[1].text)

        know_count = know_count + 1
    else: break
print(know_li1)
print(know_li2)
print(know_li3)
#지식인 조회수 & 날짜 확인
# for know_href in know_li:
#     res = requests.get(f"{know_href}", headers=header)
#     know_html = res.text
#     know_soup = BeautifulSoup(know_html,'html.parser')
#     know_date = know_soup.select_one('span.c-userinfo__info')
#
#     print(know_date.getText())

