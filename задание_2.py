
class Div_zero:
    def __init__(self,num):
        self.num = num

    def __truediv__(self, other):
        try:
            return self.num / other.num
        except ZeroDivisionError:
            return '∞'

a = Div_zero(4)
b = Div_zero(2)
c = Div_zero(0)

print(a/b)
print(a/c)