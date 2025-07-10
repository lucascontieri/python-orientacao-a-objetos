class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica_internacional = Musica('Hometown Glory', 'Adele', '3:32')
musica_sertanejo = Musica('Barulho do Foguete', 'Zé Neto e Cristiano', '2:14')

Musica.listar_musicas()

