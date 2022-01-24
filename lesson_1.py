import re

regex_valid = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex_split = re.compile(r'(.*)@(.*)')
email = 'someone@geekbrains.ru'
users = {}

def users_dict (eml):
     usrs = {}
     dct = re.findall(regex_split,eml)
     usrs['username'] = dct[0][0]
     usrs['domain'] = dct[0][1]
     return usrs

def valid (eml):
     if re.fullmatch(regex_valid,eml):
          return True
     else:
          raise ValueError


if valid(email) == True:
     users = users_dict(email)
     print(users)