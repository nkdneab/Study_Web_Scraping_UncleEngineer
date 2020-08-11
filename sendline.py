from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from songline import Sendline
token = 'gtr6GX7Rk4pPmOfJiDlGXjNozEDskKYpgAug9WsrEXG'
messenger = Sendline(token)
#messenger.sendtext("nnn")
#messenger.sticker(141,2)
#messenger.sendimage('https://image.shutterstock.com/image-vector/mm-letter-logo-260nw-712706803.jpg')
#print(help(Sendline))
def stock(symbol):
    url = f'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={symbol}&ssoPageId=9&selectPage=1'
    webopen = urlopen(url)
    page_html = webopen.read()
    webopen.close()
    data = soup(page_html, 'html.parser')
    price = data.findAll('div', {'class': 'col-xs-6'})
    update = data.findAll('div', {'class': 'flex-item'})
    realupdate = update[0].text
    realupdate = realupdate.replace("\n","")
    realupdate = realupdate.replace("\r","")
    realupdate = realupdate.replace("\t","")
    realupdate = realupdate.replace(" ", "")

    stockname = price[0].text
    realprice = price[2].text
    realprice = realprice.replace("\n","")
    realprice = realprice.replace("\r","")
    realprice = realprice.replace("\t","")
    realprice = realprice.replace(" ", "")

    change = price[3].text
    change = change.replace("\n","")
    change = change.replace("\r","")
    change = change.replace("\t","")
    change = change.replace(" ", "")
    pchange = price[4].text
    pchange = pchange.replace("\n", "")
    pchange = pchange.replace("\r", "")
    pchange = pchange.replace("\t", "")
    pchange = pchange.replace(" ", "")
    #รวมค่า
    alltext = ''
    alltext = alltext + f'Stock:{stockname}\n'
    alltext = alltext + f'Price:{realprice}\n'
    alltext = alltext + f"{change}\n"
    alltext = alltext + f"{pchange}\n"
    alltext = alltext + realupdate
    return alltext
allstock = ["SCB","MK","M","TMB","KBANK","KTB"]
alldata =""
for i in allstock:
    mystock = stock(i)
    alldata = alldata + mystock +"\n\n"
messenger.sendtext(alldata)