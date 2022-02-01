
class road:
    def __init__(self,_length,_width):
        self.length = _length
        self.width = _width
    def calc(self):
        return f'{self.width * self.length * 25 * 5 / 1000} т.'

a = road(5000,20)
print(a.calc())