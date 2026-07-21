from bs4 import BeautifulSoup
import requests
order = requests.get('https://economictimes.indiatimes.com//topic/CJP').text
soup = BeautifulSoup(order, 'lxml')
news = soup.find('div', class_='clr flt topicstry story_list')
for baatmi in news:
#         baatmi = news
        print(baatmi)
# print(news.text)