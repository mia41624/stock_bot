import requests #請求工具
from bs4 import BeautifulSoup #解析工具
import time #暫停時間

stock=['1101','2330','5347'] #要爬的股票

for i in range(len(stock)): #迴圈依序爬股票
  stockid=stock[i] #o->1
  url='https://tw.stock.yahoo.com/quote/'+stockid+'.TW'
  r=requests.get(url)
  soup=BeautifulSoup(r.text,'html.parser')
  price=soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  #假如是上櫃
  if price==None:
    url='https://tw.stock.yahoo.com/quote/'+stockid+'.TWO' #上櫃網址規則
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    price=soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  message="股票"+stockid+"的即時價格為:" +price.getText()
  token='6974861997:AAEPcBT9C3NYrRX_ICOmV-8S3mETWvgePd0'
  chat_id='6861035633'
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url)
  time.sleep(3)
