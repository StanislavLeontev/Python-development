
def valid(func):

    def checker(x):
        if str(x).isdigit() and x > 0:
            return func(x)
        raise ValueError

    return checker

@valid
def calc_cube(x):
    return x ** 3

a = calc_cube(2)
print(a)