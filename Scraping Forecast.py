from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
n=1
while n <= 500:
    try:
        url = 'https://tmd.go.th/province.php?id=' + str(n)
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        temp = data.findAll('td', {'class': 'strokeme'})
        station = data.findAll('td', {'class': 'SelectStation'})
        tt = data.title.text.replace(' ', '').split('-')
        num = len(station)
        n = n + 1
        if num > 0:
            if tt[1].replace('อากาศจังหวัด','') == station[0].text:
                print(tt[1],'เฉลี่ย', temp[0].text)
            else:
                print(tt[1],station[0].text, temp[0].text)
        else:
            print(tt[1], temp[0].text)
    except:
        n = n + 1