
class Clothes:
    def __init__(self,type,size):
        self.type = type
        self.size = size

    @property
    def calc(self):
        if self.type == 'пальто':
            return round(self.size / 6.5 + 0.5 ,1)
        elif self.type == 'костюм':
            return round(2 * self.size + 0.3 ,1)

a = Clothes('пальто',60)
b = Clothes('костюм',60)

print(a.calc)
print(b.calc)