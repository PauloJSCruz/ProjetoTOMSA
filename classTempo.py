import numpy as np

class Tempo:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Tempo no âmbito da u.c. TOMSA

    Representa as informações de tempo associadas à trajetória.

    Atributos:
        _secs (int): Número de segundos.
        _nsecs (int): Número de nanosegundos.
    """
    
    def __init__(self):
        self._secs: int
        self._nsecs: int

    def __str__(self):
        return f"sec: {self._secs}, nsec: {self._nsecs}"

    @property
    def secs(self):
        """
        Retorna:
            int: Número de segundos.
        """
        return self._secs

    @secs.setter
    def secs(self, secs):
        """
        Define o número de segundos.

        Parâmetros:
            secs (int): Número de segundos.
        """
        self._secs = secs

    @property
    def nsecs(self):
        """
        Retorna:
            int: Número de nanosegundos.
        """
        return self._nsecs

    @nsecs.setter
    def nsecs(self, nsecs):
        """
        Define o número de nanosegundos.

        Parâmetros:
            nsecs (int): Número de nanosegundos.
        """
        self._nsecs = nsecs
