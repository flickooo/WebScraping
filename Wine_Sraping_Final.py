import urllib.request
from bs4 import BeautifulSoup as bs
import requests
import time



web_input = input('write site here ---->  ')
headers = {
    'authority': 'www.wine-searcher.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': web_input,
    'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8,sr;q=0.7',
    'cookie': 'ID=GKZ4CQL8F440031; IDPWD=I07535321; COOKIE_ID=GKZ4CQL8F440031; visit=GKZ4CQL8F440031^%^7C20200519115111^%^7C^%^2Ffind^%^2Flieu^%^2Bdit^%^2Bchenin^%^2Bblanc^%^2B2017^%^2F1^%^2Fusa^%^7C^%^7Cend+; fflag=flag_store_manager^%^3A0^%^2Cend; _csrf=pzyY-L-DJKm3ZuzASyJmqQJ1Gm_MEzCL; _pxhd=288fa3d8fdc20c1e1a8a2b163d469e4b29672820562d67c2789c92a796f079bc:a7269120-99be-11ea-9181-c73c69e92a36; _pxvid=a7269120-99be-11ea-9181-c73c69e92a36; _gid=GA1.2.783861869.1589885472; __pxvid=8ed9427f-99d3-11ea-b61a-0242ac110003; search=start^%^7Clieu^%^2Bdit^%^2Bchenin^%^2Bblanc^%^2B2017^%^7C1^%^7CUSA^%^7CRSD^%^7C^%^7C^%^7C^%^7C^%^7C^%^7C^%^7C^%^7C^%^7Ce^%^7Cend; _ga_M0W3BEYMXL=GS1.1.1589893446.2.1.1589894544.0; _ga=GA1.2.530545828.1589885472; _gat_UA-216914-1=1; _px3=289e9c481b52a7c925b23518ce3b960920838f1b18e8f1611e2c68472f3e523e:WvKDXAOHViJNjV3SLO2wKFtg9/4f/Cw/gzCjhFeQuYj58ZEMeHAmnw4GRsyxNA0rE53fVK6lbmbRaN8Yp9fNVQ==:1000:/V4It+hhBAiw5oOxbqcd37mX8K1N7fvKU9qmH8pBV9l2d7WM/UrmXevUlqiGtKo/0Cn9iiz2oEw0p5TW6Z1/fxUH+AXNOCSRJ/VUeQwqQaGcI1e7vav/g725h8zga2bn9HNrZwyXUtH78kUOxCWqcEA+j5sjQv1wH6AziP+ZQDs=; _px2=eyJ1IjoiYzZmYjc5NjAtOTlkMy0xMWVhLWI5ZDgtOGRkNDMzNmQ4MGZhIiwidiI6ImE3MjY5MTIwLTk5YmUtMTFlYS05MTgxLWM3M2M2OWU5MmEzNiIsInQiOjE1ODk4OTQ4NDU5OTYsImgiOiI0NDMwMjVlYTAwZWFiOGE0ZjgwNmJhZGUwMDczYjVjNjBlOWI1ZWViNTgzYjg1ODUyZWRmMGE4N2U0YjVhY2MxIn0=; _pxde=d7c30eab00f2178267d096ac4332f56e9033bbfe18652f2188cd97578e38953c:eyJ0aW1lc3RhbXAiOjE1ODk4OTQ1NTM1MjMsImZfa2IiOjAsImlwY19pZCI6W119',
}

response_first = requests.get(web_input, headers=headers)
html = response_first.text



def result(parsed_url):


    page_soup = bs(parsed_url, 'html.parser')

    container = page_soup.findAll('span', {'class':'dtlbl sidepanel-text'})
    avg_price = container[0].b.text


    container_2 = page_soup.findAll('a',{'class':'mnt-link2'})
    lowest_source = container_2[0].div.span.text


    container_3 = page_soup.findAll('span',{'class':'offer_price'})
    lowest_price = container_3[0]['content']

    print(avg_price)
    print(lowest_price)
    print(lowest_source)

    


result(html)
input("press any key")