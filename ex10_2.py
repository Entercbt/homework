import requests
from bs4 import BeautifulSoup
allUniv=[]
def getHTMLText(ur1):
     send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    try:
        r = requests.get(ur1,hearders=send_headers)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = 'utf-8'
        return r.text
    except:
        return""
def fillUnivList(soup,allUniv):
    data = soup.find_all('div',{'class':re.compile('shadow_dark')})
    for div in data:
        singleUniv = []
        divl = div.find('div',('style':'margin_left:2.5rem:'})
        rank = divl.get_text().strip()
        singleUniv.append(rank.split(' ')[0])
        h3 = div.find('h3')
        singleUniv.append(h3.get_text().strip())
        ldiv = div.find_all('div',{'style':'padding_right: 0.5rem:'})
        singleUniv.append(ldiv[0].strong.string)
        singleUniv.append(ldiv[1].strong.string)
        allUniv.append(singleUniv)
def printUnivList(allUniv):
    print("{:<6}{:<20}{:<6}{:<10}".format("排名","学校名称","学费","培养规模"))
    for u in allUniv:
        print("{:<6}{:<20}{:<6}{:<10}".format(u[0],u[1],u[2],u[3]))
   
main('江西')
