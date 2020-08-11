from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

user1 = 'loong@gmail.com'
password = 'loong'

urllogin = 'http://www.uncle-school.com/login/'

driver.get(urllogin)

elem_user = driver.find_element_by_id('username')
elem_pass = driver.find_element_by_id('password')
elem_user.send_keys(user1)
elem_pass.send_keys(password)
elem_pass.send_keys(Keys.RETURN)
time.sleep(2)
url = 'http://www.uncle-school.com/'
driver.get(url)

allmenu = driver.find_elements_by_class_name('nav-item')

allmenus = []
allurl = []

for mn in allmenu:
    menu = mn.text
    rurl = mn.find_element_by_css_selector('a').get_attribute('href')#เนื้อหาของurlซ่อนอยู่ในscrip
    allmenus.append(menu)
    allurl.append(rurl)
urlsearch = 'http://www.uncle-school.com/search'
driver.get(urlsearch)

allstudent = ['6210001','6210002','6310001','6310002']
for st in allstudent:
    searchbox = driver.find_element_by_name('search')
    searchbox.send_keys(st)
    searchbox.send_keys(Keys.RETURN)
    studentname = driver.find_element_by_tag_name('p')
    if studentname.text[:2] == 'ID':
        print('IDSearch: {} Result: {}'.format(st,studentname.text))
    else:
        print('ไม่มีผลลัพท์')
driver.close()