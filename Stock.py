from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=PTT&ssoPageId=9&selectPage=1'
webopen = urlopen(url)
page_html = webopen.read()
webopen.close()
data = soup(page_html, 'html.parser')
price = data.findAll('div',{'class':'col-xs-6'})
update = data .findAll('div',{'class':'flex-item'})
realupdate = update[0].text
realupdate = realupdate.replace("\n","")
realupdate = realupdate.replace("\r","")
realupdate = realupdate.replace("\t","")
realupdate = realupdate.replace(" ","")
print("Count", len(price))
print("Stock", price[0].text)
realprice = price[2].text
realprice = realprice.replace("\n", "")
realprice = realprice.replace("\r", "")
realprice = realprice.replace("\t", "")
realprice = realprice.replace(" ", "")
print("Price", realprice)
change = price[3].text
change = change.replace("\n","")
change = change.replace("\r","")
change = change.replace("\t","")
change = change.replace(" ","")
print(change)
pchange = price[4].text
pchange = pchange.replace("\n","")
pchange = pchange.replace("\r","")
pchange = pchange.replace("\t","")
pchange = pchange.replace(" ","")
print(pchange)
print(realupdate)
