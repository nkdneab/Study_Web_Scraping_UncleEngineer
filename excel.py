from openpyxl import Workbook
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
def checkcrypto(code="bitcoin",start="20190403",stop="20200403"):
    url = f'https://coinmarketcap.com/currencies/{code}/historical-data/?start={start}&end={stop}'
    webopen = urlopen(url)
    page_html = webopen.read()
    webopen.close()
    data = soup(page_html, 'html.parser')
    price = data.findAll('tr', {'class': 'cmc-table-row'})
  #  row = price[0]
  #  column = row.findAll("td")
    result_Date=[]
    result_open=[]
    result_close=[]

    for row in price:
       column = row.findAll("td")
       result_Date.append(column[0].text)
       result_open.append(float(column[1].text.replace(',',"")))
       result_close.append(float(column[4].text.replace(',',"")))

    #print(result_Date)
    #print(result_open)
    #print(result_close)
    return (result_Date,result_open,result_close)
allresult = checkcrypto('xrp',"20190403","20190603")

excelfile = Workbook()
sheet = excelfile.active

header = ['DATE','OPEN PRICE','CLOSE PRICE']
sheet.append(header) #เพิ่มค่าเข้าไปทั้งเเเถว
for x,y,z in  zip(allresult[0],allresult[1],allresult[2]):
    sheet.append([x,y,z])
excelfile.save("cryto.xlsx")