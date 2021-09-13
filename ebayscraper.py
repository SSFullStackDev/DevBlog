from bs4 import BeautifulSoup as bs
import requests
import os


source = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=xm4&_sacat=0&_sop=1&LH_ItemCondition=1500%7C2000%7C2500%7C3000%7C1000&rt=nc&LH_BO=1')
"""source.text and html.parser instead of source and html need to look at bs docs"""
soup = bs(source.text, 'html.parser')
print(soup.title.text)
priceList = []

for item in soup.find_all('div', class_ = 's-item__info clearfix'):
    price = item.find('span', class_='s-item__price')
    try:
        price = float(price.text[1:])
        priceList.append(price)

    except AttributeError:
        pass
print(priceList)
"""Get average price/day save to a csv create graph from csv"""
"""Set email alerts for price drops"""
"""create functions with ability to imput parameters for search"""
"""Build Gui for parameter input and graphs"""
"""Android App"""