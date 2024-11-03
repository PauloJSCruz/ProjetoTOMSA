from classTempo import Tempo
from classHeader import Header
from classTemperatureWithHeader import TempratureWithHeader

class Temperatura:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Temperatura no âmbito da u.c. TOMSA

    Representa os dados de temperatura de um veículo, compostos por múltiplos objetos TempratureWithHeader.

    Atributos:
        _pontosTemperatura (list): Lista de objetos TempratureWithHeader que representam os pontos de temperatura ao longo do tempo.
        _nome (str): Nome dos dados de temperatura.
    """

    def __init__(self) -> None:      
        self._pontosTemperatura = []
        self._nome = ""

    def ReadLogTempratura(self, pathFile):
        """Lê um arquivo de log de temperatura e adiciona à lista de objetos TempratureWithHeader"""
        header_data = {}
        countTemperaturas = 0
        countPontosValidos = 0
        temperatura = None
        variancia = None
        flagHeader = False

        with open(pathFile, 'r') as f:
            for index, line in enumerate(f, start=1):
                line = line.strip()                
                # Ignorar linhas vazias ou inválidas
                if not line:
                    continue

                try:
                    # Iniciar a leitura de um novo header
                    if line.startswith("header:"):
                        countTemperaturas += 1
                        flagHeader = True
                        header_data = {}
                        tempo = Tempo()
                        temperatura = None
                        variancia = None

                    # Processar dados do header
                    if flagHeader:
                        if line.startswith("frame_id:"):
                            header_data['frame_id'] = line.split(":")[1].strip()
                        elif line.startswith("seq:"):
                            try:
                                header_data['seq'] = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue
                        elif line.startswith("nsecs:"):
                            try:
                                tempo.nsecs = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue
                        elif line.startswith("secs:"):
                            try:
                                tempo.secs = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue
                        elif line.startswith("temperature:"):
                            try:
                                temperatura = float(line.split(":")[1].strip())
                            except ValueError:
                                continue
                        elif line.startswith("variance:"):
                            try:
                                variancia = float(line.split(":")[1].strip())
                            except ValueError:
                                continue

                    # Verificar se temos todos os dados necessários para criar um ponto de temperatura
                    if (header_data and hasattr(tempo, 'nsecs') and hasattr(tempo, 'secs') 
                        and temperatura is not None 
                        and variancia is not None  
                        and "frame_id" in header_data 
                        and "seq" in header_data):

                        try:
                            # Criar objetos correspondentes para a temperatura
                            header = Header(header_data['seq'], tempo, header_data['frame_id'])
                            novaTemperatura = TempratureWithHeader(header, temperatura, variancia)
                            self._pontosTemperatura.append(novaTemperatura)
                            countPontosValidos += 1  # Incrementar contagem de pontos válidos

                            # Imprimir o ponto recém-adicionado
                            # print(novaTemperatura)
                        except Exception:
                            # Ignorar este ponto e continuar com o próximo
                            continue

                        # Resetar variáveis temporárias
                        header_data = {}
                        tempo = Tempo()
                        temperatura = None
                        variancia = None
                        flagHeader = False

                except (ValueError, KeyError, AttributeError):
                    # Reiniciar as variáveis temporárias para ignorar o ponto atual
                    header_data = {}
                    tempo = Tempo()
                    temperatura = None
                    variancia = None
                    flagHeader = False
                    continue

        # Imprimir resumo dos pontos lidos
        print(f"Temperaturas do ficheiro {self._nome}, número de pontos válidos: {countPontosValidos} de {countTemperaturas}")

        return
    
    @property
    def pontosTemperatura(self):
        """
        Retorna:
            list: Lista de objetos TempratureWithHeader que representam os pontos de temperatura ao longo do tempo.
        """
        return self._pontosTemperatura

    @pontosTemperatura.setter
    def pontosTemperatura(self, pontos):
        """
        Define a lista de pontos de temperatura.

        Parâmetros:
            pontos (list): Lista de objetos TempratureWithHeader.
        """
        self._pontosTemperatura = pontos
