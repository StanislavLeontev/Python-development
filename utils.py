import requests
from bs4 import BeautifulSoup
import identifiers
import datetime

def currency_rates(code):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(r.text, "html.parser")
    dtm = identifiers.dt(soup)
    dat = datetime.date(int(dtm[0]),int(dtm[1]),int(dtm[2]))
    text = identifiers.id_s(soup)
    identifiers.search(code,soup,text,dat)

