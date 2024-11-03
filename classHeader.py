import numpy as np
from classTempo import Tempo

class Header:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Header no âmbito da u.c. TOMSA

    Representa o cabeçalho de um ponto da trajetória.

    Atributos:
        _seq (int): Sequência única do ponto.
        _stamp (Tempo): Informações de tempo associadas ao ponto.
        _frame_id (str): ID do quadro de referência utilizado.
    """
    
    def __init__(self, seq: int, stamp: Tempo, frame_id: str) -> None:
        self._seq = seq  
        self._stamp = stamp
        self._frame_id = frame_id

    def __str__(self):
        return f"Header(seq={self._seq}, stamp={self._stamp}, frame_id={self._frame_id})"

    @property
    def seq(self):
        """
        Retorna:
            int: Sequência única do ponto.
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        """
        Define a sequência única do ponto.

        Parâmetros:
            seq (int): Sequência única do ponto.
        """
        self._seq = seq

    @property
    def stamp(self):
        """
        Retorna:
            Tempo: Informações de tempo associadas ao ponto.
        """
        return self._stamp

    @stamp.setter
    def stamp(self, stamp):
        """
        Define as informações de tempo associadas ao ponto.

        Parâmetros:
            stamp (Tempo): Objeto Tempo contendo as informações temporais do ponto.
        """
        self._stamp = stamp

    @property
    def frame_id(self):
        """
        Retorna:
            str: ID do quadro de referência utilizado.
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        """
        Define o ID do quadro de referência utilizado.

        Parâmetros:
            frame_id (str): ID do quadro de referência.
        """
        self._frame_id = frame_id