from bs4 import BeautifulSoup
import requests
import telegram
import asyncio
from hotdeal.models import Deal
from datetime import datetime, timedelta

response = requests.get("https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu2")
soup = BeautifulSoup(response.text,"html.parser")
BOT_TOKEN = '5732635289:AAEljPJ0nxaKnbTxudjHqlEYlwjHkDwOPoU'

bot = telegram.Bot(token=BOT_TOKEN)
async def botAsynMain(msg):
    await bot.send_message(chat_id=-1001859218840,text=msg)

def run():
    print('스크립트 시작...')
    for item in soup.find_all("tr",{'class':['list_notice list-notice-alarm-sponsor-tr','list0','list1']}):
        try:
            item1 = item.find("div",class_= 'list_name')
            image = 'http://' + item1.find("img").get("src")[2:]
            
            titles = item.find_all('a')
            title = titles[2].text.strip()
            
            link = 'https://www.ppomppu.co.kr/zboard/' + titles[1].get('href')
            
            reply_count = int(item.find('span',{'class':['list_comment','list_comment2']}).text)
            
            up_count = item.find_all('td')[-2].text
            up_count = up_count.split('-')[0]
            
            up_count = int(up_count)
            # print(image,title,link,reply_count,up_count)
            if up_count >= 6:
                print('>= 37조건 충족...',Deal.objects.filter(link__iexact=link))
                Deal(image_url=image,title=title,link=link,reply_count=reply_count,up_count=up_count).save()
                asyncio.run(botAsynMain('{} {}'.format(title, link)))
                # link__iexact : 대소문자 상관없이 같은지...
                # if(Deal.objects.filter(link__iexact=link) == NULL):
                #     print(title,up_count)
                #     Deal(image_url=image,title=title,link=link,reply_count=reply_count,up_count=up_count).save()
                #     asyncio.run(botAsynMain('{} {}'.format(title, link)))
                
        except Exception as e:
            continue
        

    
    
