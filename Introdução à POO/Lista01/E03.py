import os

class Banco:
    def __init__(self):
        self.nome = 0
        self.conta = 0
        self.saldo = 0
    
    def get_saldo(self):
        return self.saldo
    
    def set_deposito(self,x):
        self.saldo = self.saldo + x
    
    def set_saque(self,y):
        if(self.saldo-y < 0):
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - y

z = Banco() 
contador=0
while(contador==0):
    os.system('cls')
    print("\tBem Vindo ao Banco do IF\n")
    print("Digite a opereção que deseja fazer:")
    print("1 - Deposito")
    print("2 - Saque")
    print("0 - Finalizar Operação\n")
    x = int(input())
    os.system('cls')
    
    if(x==0):
        contador = 1
    elif(x==1):
        print("Digite o valor do Deposito:")
        z.set_deposito(float(input))
    elif(x==2):
        print("Digite o valor do Saque:")
        z.set_saque(float(input()))



    

    

    