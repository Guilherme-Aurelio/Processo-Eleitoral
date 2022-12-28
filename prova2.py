
class Candidato:
    def __init__(self, nome: str, numero: str):
        self.__nome = nome
        self.__numero = numero

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def numero(self) -> str:
        return self.__numero
    
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    def __str__(self) -> str:
        return f'Candidato {self.nome} ({self.numero})'


class Voto:
    def __init__(self, id: str, candidato: 'Candidato'):
        self.__id = id
        self.__candidato = candidato

    @property
    def id(self) -> str:
        return self.__id
    
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def candidato(self) -> 'Candidato':
        return self.__candidato
    
    @candidato.setter
    def candidato(self, candidato: 'Candidato'):
        self.__candidato = candidato

from typing import List
class Urna:
    def __init__(self, id: str):
        self.__candidatos = []
        self.__votos = []
        self.__qtdVotos = 0
        self.__id = id
        self.votosBrancos = 0
        self.votosNulos = 0

    @property
    def candidatos(self) -> List[Candidato]:
        return self.__candidatos
    
    @property
    def votos(self) -> List[Voto]:
        return self.__votos
    
    @property
    def qtdVotos(self) -> int:
        return self.__qtdVotos

    @qtdVotos.setter
    def qtdVotos(self, qtdVotos: int):
        self.__qtdVotos = qtdVotos
    
    @property
    def id(self) -> str:
        return self.__id

    def inserirCandidatos(self, candidatos: List[Candidato]):
        self.candidatos.extend(candidatos)

    def adicionarVoto(self, num: str):
        if num == 0:
            self.votosBrancos += 1
            self.qtdVotos += 1
        else:
            candidato = next((c for c in self.candidatos if c.numero == num), None)
            if candidato:
                self.votos.append(Voto(num, candidato))
                self.qtdVotos += 1
            else:
                self.votosNulos += 1
                self.qtdVotos += 1

    def exibirCandidatos(self):
        for candidato in self.candidatos:
            print(candidato)

    def emitirExtrato(self):
        votos_por_candidato = {}
        for voto in self.votos:
            if voto.candidato not in votos_por_candidato:
                votos_por_candidato[voto.candidato] = 0
                votos_por_candidato[voto.candidato] += 1
        print(f'Total de votos na urna: {self.qtdVotos}')
        print('Votos por candidato:')
        for candidato, qtd_votos in votos_por_candidato.items():
            print(f'Candidato {candidato.nome} ({candidato.numero}): {qtd_votos} votos')
        print(f'Votos brancos: {self.votosBrancos}')
        print(f'Votos nulos: {self.votosNulos}')

class Eleitor   :
    def __init__(self, nome: str, titulo: str):
        self.__nome = nome
        self.__titulo = titulo

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    def votar(self, numCandidato: str, urna: 'Urna'):
        urna.adicionarVoto(numCandidato)

    def __str__(self) -> str:
        return f'Eleitor(nome={self.nome}, titulo={self.titulo})'

class Mesario(Eleitor):
    def emitirRelatorio(self, urna: Urna):
        urna.emitirExtrato()


candidatos = [
    Candidato('João', '001'),
    Candidato('Maria', '002'),
    Candidato('José', '003')
]

urna = Urna(id='1')
urna.inserirCandidatos(candidatos)

urna.exibirCandidatos()

eleitor1 = Eleitor('Guilherme', '123456789')
eleitor2 = Eleitor('Lucas', '345678922')
eleitor3 = Eleitor('João', '234567890')
eleitor4 = Eleitor('Maria', '456789012')
eleitor5 = Eleitor('José', '567890123')

eleitor1.votar('001', urna=urna)
eleitor2.votar('002', urna=urna)
eleitor3.votar('003', urna=urna)
eleitor4.votar( 0, urna=urna)
eleitor5.votar('999', urna=urna)

urna.emitirExtrato()

mesario = Mesario(nome='Natham', titulo='21221211')
#mesario.emitirRelatorio(urna)