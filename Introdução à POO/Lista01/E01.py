import math


class circulo:
    def __init__(self):
        self.r = 0
        
    def area(self):
        return math.pi*self.r**2 
    def circun(self):
        return math.pi*self.r*2        

print("Digite o raio:")
x = circulo()
x.r = float(input())

print("Área:",x.area())
print("Circunferencia:", x.circun())
