from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#url = 'https://www.google.com'
url = 'https://www.facebook.com/'
driver.get(url)
#search = driver.find_element_by_name('q')
#search.send_keys('กฤติน')
#search.send_keys(Keys.RETURN)
username = driver.find_element_by_name('email')
password = driver.find_element_by_name('pass')
username.send_keys("neab")
password.send_keys("mmmm")
login = driver.find_element_by_id("u_0_b")
login.click()
