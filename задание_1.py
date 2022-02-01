
import time

class TrafficLight:
    __color = 'красный','желтый','зелёный'
    def running(self,__color = __color):
        print(__color[0])
        time.sleep(7)
        print(__color[1])
        time.sleep(2)
        print(__color[2])

tl = TrafficLight()
tl.running()
