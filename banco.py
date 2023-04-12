class Conta(): #CLASSE MÃE

    #atributos 3

    def __init__(self):  
        self.__saldo = 0

    #MÉTODOS

    #vê o valor do atributo __saldo

    def verSaldo(self):
        print(f'*SEU SALDO É DE: {self.__saldo:.2f} R$*')

    #acrescenta um valor positivo ao atributo __saldo

    def depositar(self,valor):
        if valor < 0:
            print('*VALOR INVÁLIDO*')
        else:
            self.__saldo += valor
            print(f'*DEPOSITO NO VALOR {valor:.2f} R$ REALIZADO COM SUCESSO*')
            self.verSaldo()

    #verifica se há saldo disponível e subtrae do atributo __saldo

    def sacar(self,valor):
        if valor < 0:
            print('*VALOR INVÁLIDO*')
        if self.__saldo < valor:
            print('*SALDO INSUFICIENTE*')
        else:
            self.__saldo -= valor
            print(f'*SAQUE NO VALOR {valor:.2f} R$ REALIZADO COM SUCESSO*')
            self.verSaldo()
            

#CLASSES FILHO

#define os atributos e reutiliza os métodos da classe mãe "Conta"

class ContaPoupanca(Conta):
    def __init__(self):
        self.juros = 0.01
        super().__init__()
    
    def rendimento(self, intervalo):
        if intervalo < 0:
            print('*VALOR DE INTERVALO INVÁLIDO*')
        else:
            cont = 0
            n = self._Conta__saldo 
            while cont != intervalo:
                 n = n + (self.juros * n) 
                 cont += 1
            print(f'*SEU SALDO DAQUI {intervalo} MESES SERÁ DE: {n:.2f} R$*')
            cont = 0

#define os atributos e reutiliza os métodos da classe mãe "Conta"

class ContaCorrente(Conta):
    def __init__(self):
        self.__chequeEspecial = 1000
        self.__saldo = 0
        super().__init__()

    #vê o valor do atributo __chequeEspecial

    def verCheque(self):
        print(f'VALOR RESTANTE DO CHEQUE ESPECIAL É DE: {self.__chequeEspecial} R$')

    #caso não haja valor suficiente no atributo __saldo /vê se existe saldo suficiente do atributo __chequeEspecial e subtrae o valor do mesmo

    def sacar(self, valor):
        if valor < 0:
            print('*VALOR INVÁLIDO*')
        if self.__chequeEspecial > 0 and valor <= self.__chequeEspecial:
            if valor > self.__saldo:
                valor -= self.__saldo  
                self.__chequeEspecial -= valor    
                print(f'*SAQUE NO VALOR {valor:.2f} R$ REALIZADO COM SUCESSO*')
                self.verCheque()      
            else:
                self.__saldo -= valor
                print(f'*SAQUE NO VALOR {valor:.2f} R$ REALIZADO COM SUCESSO*')
        else:
            print(f'*SALDO NO CHEQUE ESPECIAL INSUFICIENTE. SEU SALDO É DE {self.__chequeEspecial} R$*')
            
def helpMe():
    print('*TIPOS DE CONTA*\nConta Poupnaça - x = ContaPoupanca() ')
    print('verSaldo - Mostra o saldo disponível \ndepositar - Adiciona um  valor no saldo \nsacar - subtrai um valor no saldo \nverCheque - Mostra o valor disponível no cheque especial /nrendimento - Mostra o saldo após um intervalo de x meses em um rendimento de 0.01\n')

print('Ultilize "helpMe()" para mostrar os métodos diponíveis')

     #from banco import Conta, ContaPoupanca, ContaCorrente, helpMe
