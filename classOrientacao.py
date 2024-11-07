import numpy as np

class Orientacao:
    """ 
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Orientacao no âmbito da u.c. TOMSA
    
    Um quaternião representa a orientação no espaço 3D. 
    quaterniões são usados para representar rotações no espaço 3D, esta classe fornece métodos para converter o quaternião em uma matriz de rotação.

    Componentes do quaternião:
    - q_0: parte escalar (real)
    - q_1, q_2, q_3: parte vetorial (componentes imaginárias correspondentes aos eixos ( x, y, z ))
    
    A matriz de rotação R(q) derivada do quaternião ( q = (q_0, q_1, q_2, q_3) ) é calculada como:

        R(q) = [[2(q_0^2 + q_1^2) - 1, 2(q_1q_2 - q_0q_3), 2(q_1q_3 + q_0q_2)],
                [2(q_1q_2 + q_0q_3), 2(q_0^2 + q_2^2) - 1, 2(q_2q_3 - q_0q_1)],
                [2(q_1q_3 - q_0q_2), 2(q_2q_3 + q_0q_1), 2(q_0^2 + q_3^2) - 1]]

    """

    def __init__(self, q_0: float, q_1: float, q_2: float, q_3):
        """
        Inicializa o quaternião com os componentes q_0, q_1, q_2, q_3.
        
        Parâmetros:
        - q_0: parte escalar (real)
        - q_1, q_2, q_3: parte vetorial (componentes imaginárias correspondentes aos eixos x, y, z)
        """
        self._q_0 = q_0  # parte escalar (real)
        self._q_1 = q_1  # parte imaginária correspondente ao eixo x
        self._q_2 = q_2  # parte imaginária correspondente ao eixo y
        self._q_3 = q_3  # parte imaginária correspondente ao eixo z

    def RotationMatrix(self):
        """
        Converte o quaternião em uma matriz de rotação 3x3.

        A matriz de rotação é derivada do quaternião da seguinte forma:

        R(q) = [[2(q_0^2 + q_1^2) - 1, 2(q_1q_2 - q_0q_3), 2(q_1q_3 + q_0q_2)],
                [2(q_1q_2 + q_0q_3), 2(q_0^2 + q_2^2) - 1, 2(q_2q_3 - q_0q_1)],
                [2(q_1q_3 - q_0q_2), 2(q_2q_3 + q_0q_1), 2(q_0^2 + q_3^2) - 1]]

        Retorna:
        - Um array numpy 3x3 representando a matriz de rotação.
        """
        q_0, q_1, q_2, q_3 = self._q_0, self._q_1, self._q_2, self._q_3
        return np.array([
            [2 * (q_0 ** 2 + q_1 ** 2) - 1, 2 * (q_1 * q_2 - q_0 * q_3), 2 * (q_1 * q_3 + q_0 * q_2)],
            [2 * (q_1 * q_2 + q_0 * q_3), 2 * (q_0 ** 2 + q_2 ** 2) - 1, 2 * (q_2 * q_3 - q_0 * q_1)],
            [2 * (q_1 * q_3 - q_0 * q_2), 2 * (q_2 * q_3 + q_0 * q_1), 2 * (q_0 ** 2 + q_3 ** 2) - 1]
        ])

    def RotateVector(self, v):
        """
        Roda um vetor 3D v usando o quaternião.

        Parâmetros:
        - v: Um vetor 3D (array numpy de tamanho 3) a ser rotacionado.

        Retorna:
        - Um vetor 3D (array numpy) rotacionado de acordo com a orientação do quaternião.
        """
        R = self.RotationMatrix()
        return R.dot(v)

    @property
    def q_0(self):
        """
        Retorna:
            float: Parte escalar (real) do quaternião.
        """
        return self._q_0

    @q_0.setter
    def q_0(self, q_0):
        """
        Define a parte escalar (real) do quaternião.

        Parâmetros:
            q_0 (float): Valor da parte escalar.
        """
        self._q_0 = q_0

    @property
    def q_1(self):
        """
        Retorna:
            float: Componente imaginário correspondente ao eixo x.
        """
        return self._q_1

    @q_1.setter
    def q_1(self, q_1):
        """
        Define o componente imaginário correspondente ao eixo x.

        Parâmetros:
            q_1 (float): Valor da componente imaginária no eixo x.
        """
        self._q_1 = q_1

    @property
    def q_2(self):
        """
        Retorna:
            float: Componente imaginário correspondente ao eixo y.
        """
        return self._q_2

    @q_2.setter
    def q_2(self, q_2):
        """
        Define o componente imaginário correspondente ao eixo y.

        Parâmetros:
            q_2 (float): Valor da componente imaginária no eixo y.
        """
        self._q_2 = q_2

    @property
    def q_3(self):
        """
        Retorna:
            float: Componente imaginário correspondente ao eixo z.
        """
        return self._q_3

    @q_3.setter
    def q_3(self, q_3):
        """
        Define o componente imaginário correspondente ao eixo z.

        Parâmetros:
            q_3 (float): Valor da componente imaginária no eixo z.
        """
        self._q_3 = q_3