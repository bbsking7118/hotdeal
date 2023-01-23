from bs4 import BeautifulSoup
import requests
import telegram

response = requests.get("https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu2")
# print(response) 
# print(response.txt)
soup = BeautifulSoup(response.text,"html.parser")
# print(soup)

# title = soup.find_all("span", class_="text")
# print(title)

# item = soup.find_all("tr",{'class':"list_notice list-notice-alarm-sponsor-tr"})[0]
# print(item)
# print(item.text)

# for item in soup.find_all("tr",{'class':"list_notice list-notice-alarm-sponsor-tr"}):
#     image = item.find("img").get("src")
#     print(image)

for item in soup.find_all("tr",{'class':['list_notice list-notice-alarm-sponsor-tr','list0','list1']}):
    try:
        item1 = item.find("div",class_= 'list_name')
        image = 'http://' + item1.find("img").get("src")[2:]
        
        # print(image)
        titles = item.find_all('a')
        title = titles[2].text.strip()
        # print(title)
        
        link = 'https://www.ppomppu.co.kr/zboard/' + titles[1].get('href')
        # print(link)
        
        reply_count = int(item.find('span',{'class':['list_comment','list_comment2']}).text)
        # print(title, reply_count)
        # print('\n')
        # print(rcounts[1])
        # reply_count = rcounts[2].text
        # # rcount = rcount if rcount.isdigit() else 0
        # reply_count = int(reply_count)
        # # print(rcount)
        
        up_count = item.find_all('td')[-2].text
        up_count = up_count.split('-')[0]
        # up_count = int(up_count) if up_count != null else 0
        up_count = int(up_count)
        # print(title, up_count)
        if up_count >= 37:
            print(image, title, link, reply_count, up_count)
    except Exception as e:
        # print(e)
        continue
    

    
    
