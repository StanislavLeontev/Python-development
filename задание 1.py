import requests
import requests.utils

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

def request_logs (url):
    resp = requests.get(url)
    enc = requests.utils.get_encoding_from_headers(resp.headers)
    cont = resp.content.decode(encoding=enc)
    with open('nginx_logs.txt','w',encoding='utf-8') as file:
        file.write(cont)

def select_data ():
    line_1 = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line_list = line.split(' ')
            tpl = (
                line_list[0],
                line_list[5][1:],
                line_list[6]
            )
            line_1.append(tpl)
    return line_1