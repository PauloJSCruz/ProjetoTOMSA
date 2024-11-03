from classPONTO import Ponto 
from classOrientacao import Orientacao

class Pose:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Pose no âmbito da u.c. TOMSA

    Representa uma pose composta por posição e orientação no espaço 3D.

    Atributos:
        _posicao (Ponto): Posição 3D representada por um objeto Ponto.
        _orientacao (Orientacao): Orientação 3D representada por um objeto Orientacao.
    """
    
    def __init__(self, posicao: Ponto, orientacao: Orientacao):
        self._posicao = posicao  # Posição é representada por um objeto Ponto
        self._orientacao = orientacao  # Orientação é representada por um objeto Orientacao

    def __str__(self):
        return f"Posição: {self._posicao}, Orientação: {self._orientacao}"

    @property
    def posicao(self):
        """
        Retorna:
            Ponto: A posição 3D.
        """
        return self._posicao

    @posicao.setter
    def posicao(self, posicao):
        """
        Define a posição 3D.

        Parâmetros:
            posicao (Ponto): Objeto Ponto contendo a posição 3D.
        """
        self._posicao = posicao

    @property
    def orientacao(self):
        """
        Retorna:
            Orientacao: A orientação 3D.
        """
        return self._orientacao

    @orientacao.setter
    def orientacao(self, orientacao):
        """
        Define a orientação 3D.

        Parâmetros:
            orientacao (Orientacao): Objeto Orientacao contendo a orientação 3D.
        """
        self._orientacao = orientacao
