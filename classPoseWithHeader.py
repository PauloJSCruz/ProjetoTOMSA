from classHeader import Header
from classPose import Pose

class PoseWithHeader:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe PoseWithHeader no âmbito da u.c. TOMSA

    Combina as informações de cabeçalho com a pose para um ponto da trajetória.

    Atributos:
        _header (Header): Informações de cabeçalho associadas ao ponto.
        _pose (Pose): Informações de posição e orientação associadas ao ponto.
    """
    
    def __init__(self, header: Header, pose: Pose):
        self._header = header
        self._pose = pose

    def __str__(self):
        return f"Header: {self._header}, Pose: {self._pose}"

    @property
    def header(self):
        """
        Retorna:
            Header: As informações de cabeçalho associadas ao ponto.
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Define as informações de cabeçalho associadas ao ponto.

        Parâmetros:
            header (Header): Objeto Header contendo as informações de cabeçalho.
        """
        self._header = header

    @property
    def pose(self):
        """
        Retorna:
            Pose: As informações de posição e orientação associadas ao ponto.
        """
        return self._pose

    @pose.setter
    def pose(self, pose):
        """
        Define as informações de posição e orientação associadas ao ponto.

        Parâmetros:
            pose (Pose): Objeto Pose contendo as informações de posição e orientação.
        """
        self._pose = pose