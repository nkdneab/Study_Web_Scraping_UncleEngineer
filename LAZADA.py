from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
import time
def LAZADA(keyword="ร้องเท้า"):
    #opt = webdriver.ChromeOptions()
    #opt.add_argument('headless')

    driver = webdriver.Chrome()#(options=opt)
    url = 'https://www.lazada.co.th/'
    driver.get(url)

    search = driver.find_element_by_name('q')
    find = search.send_keys(keyword)
    click = driver.find_element_by_class_name('search-box__search--2fC5')
    click.click()
    time.sleep(3)
    page_html = driver.page_source
    data = soup(page_html, 'html.parser')
    name = data.findAll('div', {'class': 'c16H9d'})
    price = data.findAll('span', {'class': 'c13VH6'})

    #url_ss = name[0].a['href']
    #url_s = "https:"+url_ss

    product=[]
    productprice=[]
    producturl=[]

    for pd in name:
        product.append(pd.text)
        producturl.append("https:"+pd.a['href'])
    for pr in price:
        productprice.append(float(pr.text.replace('฿',"").replace(',',"")))
    driver.close()
    excelfile = Workbook()
    sheet = excelfile.active
    header = ["สินค้า","ราคา","URL"]
    sheet.append(header)
    for x,y,z in zip(product,productprice,producturl):
        sheet.append([x,y,z])
    from datetime import datetime
    dt =datetime.now().strftime('%Y-%m-%d')
    excelfile.save(f'LAZADA{keyword}_{dt}.xlsx')
LAZADA("nintendo")