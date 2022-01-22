import os

dir_names = ['my_project','settings','mainapp','adminapp','authapp']

def dir_gen (d_names):
    if not os.path.exists(d_names[0]):
        os.makedirs(d_names[0])
        os.chdir(d_names[0])
        for i in d_names[1:]:
            os.makedirs(i)
    else:
        os.chdir(d_names[0])
        for i in d_names[1:]:
            if not os.path.exists(i):
                os.makedirs(i)


dir_gen(dir_names)
