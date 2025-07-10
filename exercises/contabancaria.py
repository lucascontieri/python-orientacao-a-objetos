# aboradagem phytonica significa encapsular os atributos da classe
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'Cliente {self._titular} | Saldo: R${self._saldo} \n'
    
    @classmethod
    def ativar_conta(cls, titular, saldo=0):
        conta = cls(titular, saldo)
        conta._ativo = True
        return conta
    
contabancaria_lucas = ContaBancaria(titular='Lucas', saldo=1000)

print(contabancaria_lucas)

# Exemplo de conta utilizando o método de classe

contabancaria_cristiano = ContaBancaria.ativar_conta(titular='Cristiano', saldo=2000)

print(contabancaria_cristiano)


