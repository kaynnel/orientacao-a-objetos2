class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, episodios):
        super().__init__(nome, ano)
        self.episodios = episodios

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.episodios} eps - {self._likes} likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


interestelar = Filme("interestelar", 2014, 169)
vagabond = Serie("vagabond", 2019, 16)
batman = Filme("batman", 2022, 174)
justiceiro = Serie("O Justiceiro", 2017, 10)

interestelar.dar_like()
vagabond.dar_like()
batman.dar_like()
justiceiro.dar_like()

filmes_e_series = [interestelar, vagabond, batman, justiceiro]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana.listagem:
    print(programa)




