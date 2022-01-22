
import os, shutil

for i in os.walk('my project'):
    if 'base.html' in i[2] and len(i[0].split('\\')) >= 4:
        path_ac = r'my project\templates{}'.format(i[0][i[0].rindex('\\'):-1])
        try:
            shutil.copytree(i[0],path_ac)
        except FileExistsError:
            print('файл уже существует')