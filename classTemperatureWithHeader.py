from classHeader import Header

class TempratureWithHeader:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe TemperatureWithHeader no âmbito da u.c. TOMSA

    Representa a combinação de informações de cabeçalho com a temperatura para um ponto específico na trajetória.
    Esta classe permite acessar e modificar os valores de cabeçalho, temperatura e variância associados ao ponto.

    Componentes:
    - _header: Informações temporais e de sequência do ponto (Header)
    - _temperatura: Valor da temperatura associado ao ponto
    - _variancia: Valor da variância, indicando a precisão da temperatura
    """
    
    def __init__(self, header: Header, temperatura, variancia):
        self._header = header
        self._temperatura = temperatura
        self._variancia = variancia

    def __str__(self):
        return f"Header: {self._header}, Temperatura: {self._temperatura}, Variancia: {self._variancia}"

    @property
    def header(self):
        """
        Retorna:
            Header: Informações temporais e de sequência associadas ao ponto.
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Define as informações de cabeçalho associadas ao ponto.

        Parâmetros:
            header (Header): Novo valor de cabeçalho.
        """
        self._header = header

    @property
    def temperatura(self):
        """
        Retorna:
            float: Valor da temperatura associado ao ponto.
        """
        return self._temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        """
        Define o valor da temperatura associado ao ponto.

        Parâmetros:
            temperatura (float): Novo valor de temperatura.
        """
        self._temperatura = temperatura

    @property
    def variancia(self):
        """
        Retorna:
            float: Valor da variância associado à medição de temperatura.
        """
        return self._variancia

    @variancia.setter
    def variancia(self, variancia):
        """
        Define o valor da variância associado à medição de temperatura.

        Parâmetros:
            variancia (float): Novo valor de variância.
        """
        self._variancia = variancia
    