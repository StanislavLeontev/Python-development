

def id_s (sp):
    dec = {}
    text_1 = []
    text_2 = []
    text = str(sp).split('>')
    text = str(sp).split('<')
    for i in range(len(text)):
        if 'id' in text[i]:
         text_1.append(text[i])
         text_2.append(text[i+3][:-4:-1])
    for i in range(len(text_2)):
        text_1[i] = text_1[i].replace('valute id="','')
        text_1[i] = text_1[i].replace('">', '')
        text_2[i] = text_2[i][::-1]
        dec[text_2[i]] = text_1[i]
    return dec


def search(code,soup,dec,dat):
    code = code.upper()
    if str(code) not in dec:
        print('такой валюты нет')
        return None
    else:
        value = soup.find('valute', {'id': dec[code]}).find('value').text
        nominal = soup.find('valute', {'id': dec[code]}).find('nominal').text
        name = soup.find('valute', {'id': dec[code]}).find('name').text
        print('Курс на {}\n{} {} равен {} ₽'.format(dat,nominal,name,value))
    return value

def dt(soup):
    text = str(soup).split(" ")
    date = []
    for i in range(len(text)):
        if 'date' in text[i]:
            date.append(text[i])
            date[0] = date[0].replace('date="','')
            date[0] = date[0].replace('"', '')
            date = str(date).replace("['","")
            date = str(date).replace("']", "")
            date = date.split('.')
            date.reverse()
            break
    return date

