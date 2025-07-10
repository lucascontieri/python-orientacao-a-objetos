from models.avaliacao import Avaliacao

class Restaurante:
   # Representa um restaurante e suas características 
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Inicializa os atributos de uma instância classe através do método especial __init__

        Parâmetros:
        - nome (str): Nome do restaurante
        - categoria (str): Categoria do restaurante)
        '''
        self._nome = nome.title() # função do Python que torna a primeira letra maiúscula
        self._categoria = categoria.upper() # torna todas as letras maiúsculas
        self._ativo = False # Convenção de deixar o atributo protegido utilizamos o _ na frente
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # self é a referência da instância (objeto) atual que estamos localizados
    def __str__(self):
        '''Retorna uma representação em formato de string de restaurante'''
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        '''Imprime uma lista de todos os restaurantes cadastrados '''
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}")

    # Modificando com o decorator do Python @property, onde ele capaz de alterar a forma como o atributo do método é lido
    @property
    def ativo(self):
        '''Retorna um ícone de acordo com o status do restaurante, ativo ou inativo'''
        return "✅" if self._ativo else "❌"
    
    # Método para os Objetos Instanciados
    def alternar_estado(self):
        '''Alterna o estado do restaurante '''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        ''' Recebe uma avaliação para o restaurante

        Parâmetros:
        - cliente (str): O nome do cliente que está avaliando o restaurante
        - nota (float): A nota que o cliente deu para o restaurante entre 1 a 5
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante'''
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas,1)
        return media
    

# Utilizando a função dir para conseguir visualizar informações do objeto
# Vars podemos observar um dicionário dos atributos e métodos da classe
# A forma como aparece __classe__, o '__', representa um método especial que toda classe python vai ter.
