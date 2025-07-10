class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}\n'
    
    def aniversario(self):
        self.idade += 1
    
    def saudacao(self):
        if self.profissao:
            return f'Olá, {self.nome} seu cargo atual é: {self.profissao}.'
        else:
            return f'Olá, {self.nome}.'
    

pessoa_lucas = Pessoa(nome='Lucas', idade=21, profissao='Estudante')

print('Informações Pessoais:')
print(pessoa_lucas)

pessoa_lucas.aniversario()
print(pessoa_lucas)

print(pessoa_lucas.saudacao())