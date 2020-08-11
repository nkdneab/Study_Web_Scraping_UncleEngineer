from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(options=opt)
url = 'http://www.pttor.com/oilprice-province.aspx'
driver.get(url)
time.sleep(3)
page_html = driver.page_source
data = soup(page_html,'html.parser')
table = data.findAll('table',{'id':'tbData'})
table = table[0].findAll('tbody')
rows = table[0].findAll('tr')
todayprice = rows[0].findAll('td')

oiltitie = ['อำเภอ','Diesel Premium','Diesel','DieselB10','DieselB20','Benzene','Gasohol95','Gasohol91','GasoholE20','GasoholE85,''NGV']
oilprice = []
for ol in todayprice:
    oilprice.append(ol.text)
result = {}
for t,o in zip(oiltitie,oilprice):
    result[t] = o
print(result)
driver.close()