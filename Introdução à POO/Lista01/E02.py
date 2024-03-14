class viagem:
    def __init__(self):
        self.dist = 0
        self.tempo_horas = 0
        self.tempo_minutos = 0
    def velocidade(self):
        x = self.tempo_minutos/60
        return self.dist/(self.tempo_horas+x)

x = viagem()
print("Digite a distância percorrida em KM:")
x.dist = float(input())
print("Digite a o tempo gasto na viagem no formato HH MM, onde H são a horas e o M os minutos:")
x.tempo_horas, x.tempo_minutos = map(int, input().split())
print(x.velocidade())