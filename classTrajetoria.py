from matplotlib import pyplot as plt
import numpy as np
from classHeader import Header
from classOrientacao import Orientacao
from classPONTO import Ponto
from classPose import Pose
from classPoseWithHeader import PoseWithHeader
from classTempo import Tempo
from classTemperatureWithHeader import TempratureWithHeader
from scipy.interpolate import CubicSpline

class Trajetoria:
    """
    @author: Paulo Cruz e Daniel Peixoto

    @info: exemplo de classe Trajetoria no âmbito da u.c. TOMSA

    Representa a trajetória de um veículo, composta por múltiplos objetos PoseWithHeader.

    Atributos:
        _pontos (list): Lista de objetos PoseWithHeader que representam os pontos da trajetória.
        _nome (str): Nome da trajetória.
        _freqMostragem (int): Intervalo de amostragem para a visualização dos vetores de orientação.
    """
    
    def __init__(self, freqMostragem=1):
        """Inicializa os atributos da classe"""
        self._pontos = []
        self._nome = ""
        self._freqMostragem = freqMostragem

    def ReadLogTrajetoria(self, pathFile):
        """Lê um arquivo de log de trajetória e adiciona à lista de pontos com objetos PoseWithHeader"""
        headerData = {}
        positionData = {}
        orientationData = {}
        countPontosTotal = 0
        countPontosValidos = 0
        tempo = None
        flagHeader, flagPosition, flagOrientation = False, False, False

        with open(pathFile, 'r') as file:
            for index, line in enumerate(file, start=1):
                line = line.strip()
                
                # Ignorar linhas vazias ou inválidas
                if not line:
                    continue

                try:
                    # Iniciar a leitura do header, posição ou orientação
                    if line.startswith("header:"):
                        countPontosTotal += 1
                        flagHeader = True
                        flagPosition = False
                        flagOrientation = False
                        tempo = Tempo()
                        headerData = {}
                    elif line.startswith("position:"):
                        flagHeader = False
                        flagPosition = True
                        flagOrientation = False
                        positionData = {}
                    elif line.startswith("orientation:"):
                        flagHeader = False
                        flagPosition = False
                        flagOrientation = True
                        orientationData = {}

                    # Processar dados do header
                    if flagHeader:
                        if line.startswith("seq:"):
                            try:
                                headerData['seq'] = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue
                        elif line.startswith("frame_id:"):
                            headerData['frame_id'] = line.split(":")[1].strip()
                        elif line.startswith("secs:"):
                            try:
                                tempo.secs = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue
                        elif line.startswith("nsecs:"):
                            try:
                                tempo.nsecs = int(line.split(":")[1].strip())
                            except ValueError:
                                flagHeader = False
                                continue

                    # Processar dados de posição (position)
                    if flagPosition:
                        if line.startswith("x:"):
                            try:
                                positionData['x'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagPosition = False
                                continue
                        elif line.startswith("y:"):
                            try:
                                positionData['y'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagPosition = False
                                continue
                        elif line.startswith("z:"):
                            try:
                                positionData['z'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagPosition = False
                                continue

                    # Processar dados de orientação (orientation)
                    if flagOrientation:
                        if line.startswith("x:"):
                            try:
                                orientationData['x'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagOrientation = False
                                continue
                        elif line.startswith("y:"):
                            try:
                                orientationData['y'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagOrientation = False
                                continue
                        elif line.startswith("z:"):
                            try:
                                orientationData['z'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagOrientation = False
                                continue
                        elif line.startswith("w:"):
                            try:
                                orientationData['w'] = float(line.split(":")[1].strip())
                            except ValueError:
                                flagOrientation = False
                                continue

                    # Verificar se temos uma pose completa (header, position, orientation)
                    if (headerData and 'seq' in headerData and 'frame_id' in headerData 
                        and hasattr(tempo, 'secs') and hasattr(tempo, 'nsecs')
                        and 'x' in positionData and 'y' in positionData and 'z' in positionData
                        and 'x' in orientationData and 'y' in orientationData and 'z' in orientationData and 'w' in orientationData):

                        try:
                            # Criar objetos correspondentes para a pose
                            header = Header(headerData['seq'], tempo, headerData['frame_id'])
                            position = Ponto(positionData['x'], positionData['y'], positionData['z'])
                            orientation = Orientacao(orientationData['w'], orientationData['x'], orientationData['y'], orientationData['z'])
                            pose = Pose(position, orientation)

                            # Armazenar a pose na lista de poses
                            novoPonto = PoseWithHeader(header, pose)
                            self._pontos.append(novoPonto)
                            countPontosValidos += 1  # Incrementar contagem de pontos válidos

                            # Imprimir o ponto recém-adicionado
                            # print(novoPonto)
                        except Exception:
                            # Ignorar este ponto e continuar com o próximo
                            continue

                        # Reiniciar os dicionários para o próximo ponto
                        headerData = {}
                        positionData = {}
                        orientationData = {}
                        flagHeader = False
                        flagPosition = False
                        flagOrientation = False

                except (ValueError, KeyError, AttributeError):
                    # Reiniciar os dicionários e flags para ignorar o ponto atual
                    headerData = {}
                    positionData = {}
                    orientationData = {}
                    flagHeader = False
                    flagPosition = False
                    flagOrientation = False
                    continue

        # Imprimir resumo dos pontos lidos
        print(f"Trajetórias do ficheiro {self._nome}, número de pontos válidos: {countPontosValidos} de {countPontosTotal}")

        return

    def PlotTrajetoria(self, pontosTemperatura=None):
        """Desenha a trajetória em 3D, com os eixos de orientação e temperaturas, se existirem."""
        # Cria o gráfico 3D
        figura = plt.figure()
        eixo = figura.add_subplot(111, projection='3d')

        # Chama os métodos auxiliares para criar a trajetória base, as orientações e as temperaturas
        self.PlotTrajetoriaBase(eixo)
        self.PlotOrientacoes(eixo)
        if pontosTemperatura:
            self.PlotTemperaturas(eixo, pontosTemperatura)

        # Definir rótulos e legenda
        eixo.set_xlabel('Eixo X (metros)')
        eixo.set_ylabel('Eixo Y (metros)')
        eixo.set_zlabel('Eixo Z (metros)')
        eixo.set_title(f"Trajetória com Vetores de Orientação: {self._nome}")
        eixo.legend()  # Exibir a legenda com os elementos adicionados

        # Mostrar o gráfico
        plt.show()

    def PlotTrajetoriaBase(self, eixo):
        """Desenha a linha que conecta os pontos da trajetória no gráfico 3D."""
        # Extrair os pontos (posição) da trajetória
        valoresX = [p.pose.posicao.x for p in self._pontos]
        valoresY = [p.pose.posicao.y for p in self._pontos]
        valoresZ = [p.pose.posicao.z for p in self._pontos]

        # Desenha a linha conectando os pontos da trajetória
        eixo.plot(valoresX, valoresY, valoresZ, color='skyblue', label='Trajetória')

    def PlotOrientacoes(self, eixo):
        """Adiciona vetores de orientação em pontos específicos da trajetória com base na frequência de amostragem."""
        countPrint = 0

        for index, ponto in enumerate(self._pontos):
            # Adiciona orientação com base na frequência de amostragem
            if index % self._freqMostragem == 0:
                posicao = ponto.pose.posicao
                orientacao = ponto.pose.orientacao

                # Extrai a matriz de rotação a partir dos quaterniões
                matrizRotacao = orientacao.RotationMatrix()

                # Vetores dos eixos locais (X, Y, Z) após aplicação da matriz de rotação e multiplicados por um fator de escala
                vetorX = matrizRotacao[:, 0] * 0.1  # Vetor X (vermelho)
                vetorY = matrizRotacao[:, 1] * 0.1  # Vetor Y (verde)
                vetorZ = matrizRotacao[:, 2] * 0.1  # Vetor Z (azul)

                # Desenha os vetores de orientação no ponto atual
                eixo.quiver(posicao.x, posicao.y, posicao.z, vetorX[0], vetorX[1], vetorX[2], color='r', normalize=False)
                eixo.quiver(posicao.x, posicao.y, posicao.z, vetorY[0], vetorY[1], vetorY[2], color='g', normalize=False)
                eixo.quiver(posicao.x, posicao.y, posicao.z, vetorZ[0], vetorZ[1], vetorZ[2], color='b', normalize=False)
                countPrint += 1

        print(f"Número de orientações impressas: {countPrint}")

        # Criar vetores apenas para a legenda
        eixo.quiver(0, 0, 0, 0, 0, 0, color='r', label='Vetor X')
        eixo.quiver(0, 0, 0, 0, 0, 0, color='g', label='Vetor Y')
        eixo.quiver(0, 0, 0, 0, 0, 0, color='b', label='Vetor Z')

        # Exibir a legenda
        eixo.legend(loc='upper right', fontsize='small')

    
    def PlotTemperaturas(self, eixo, pontosTemperatura=None):
        """Adiciona as temperaturas aos pontos da trajetória e realiza interpolação cúbica para suavizar a visualização."""
        if pontosTemperatura is None:
            return

        # Extrair os timestamps das poses
        poseNanoSegs = [p.header.stamp.secs * 1e9 + p.header.stamp.nsecs for p in self._pontos]

        # Extrair os valores de temperatura e respetivos timestamps
        temperaturas = [t.temperatura for t in pontosTemperatura]
        temperaturaNanoSegs = [t.header.stamp.secs * 1e9 + t.header.stamp.nsecs for t in pontosTemperatura]

        pontosFiltrados = []

        # Plotar cada ponto da trajetória e associar a temperatura mais próxima
        for i, poseNs in enumerate(poseNanoSegs):
            pontoAtual = self._pontos[i]

            # Encontrar a temperatura mais próxima em termos de tempo
            diferencasTempo = [abs(tempNs - poseNs) for tempNs in temperaturaNanoSegs]

            # Verificar se existe uma temperatura suficientemente próxima para associar
            if diferencasTempo:
                minDiferenca = min(diferencasTempo)
                indiceTempMaisProxima = diferencasTempo.index(minDiferenca)

                # Definir um limite para considerar uma temperatura próxima
                limiteTempo = 5000  

                if minDiferenca <= limiteTempo:
                    # Armazena a informação da temperatura para futura exibição
                    pontosFiltrados.append({
                        'x': pontoAtual.pose.posicao.x,
                        'y': pontoAtual.pose.posicao.y,
                        'z': pontoAtual.pose.posicao.z,
                        'temperatura': temperaturas[indiceTempMaisProxima]
                    })

        temperaturasInterpoladas = []
        xInterpolados, yInterpolados, zInterpolados = [], [], []

        # Interpolação de temperatura e posições
        for i in range(len(pontosFiltrados) - 1):
            ponto1 = pontosFiltrados[i]
            ponto2 = pontosFiltrados[i + 1]

            # Obter as temperaturas associadas aos pontos P1 e P2
            temp1 = ponto1['temperatura']
            temp2 = ponto2['temperatura']

            # Converter os pontos em arrays numpy para operações de vetor
            ponto1Arr = np.array([ponto1['x'], ponto1['y'], ponto1['z']])
            ponto2Arr = np.array([ponto2['x'], ponto2['y'], ponto2['z']])

            # Definir as temperaturas para a interpolação
            temperaturas = [temp1, temp2]

            # Definir a distância entre P1 e P2
            distancias = [0, np.linalg.norm(ponto2Arr - ponto1Arr)]

            # Criar a spline cúbica para a temperatura ao longo da distância
            splineCubic = CubicSpline(distancias, temperaturas)

            # Definir os pontos de interpolação ao longo da linha entre P1 e P2
            distInterpolada = np.linspace(0, distancias[1], 10)
            tempInterpolada = splineCubic(distInterpolada)

            # Adicionar os pontos interpolados para exibição futura
            for dist in distInterpolada:
                pontoInterpolado = ponto1Arr + (dist / distancias[1]) * (ponto2Arr - ponto1Arr)
                xInterpolados.append(pontoInterpolado[0])
                yInterpolados.append(pontoInterpolado[1])
                zInterpolados.append(pontoInterpolado[2])
                temperaturasInterpoladas.append(tempInterpolada[np.where(distInterpolada == dist)][0])

        # Criar o scatter plot dos pontos originais e interpolados
        dispersaoOriginal = eixo.scatter(
            [p['x'] for p in pontosFiltrados], 
            [p['y'] for p in pontosFiltrados], 
            [p['z'] for p in pontosFiltrados],
            c=[p['temperatura'] for p in pontosFiltrados], 
            cmap='autumn', 
            marker='o', 
            edgecolor='black', 
            s=50,  # Tamanho maior para destacar
            label='Pontos Originais'
        )

        dispersaoInterpolada = eixo.scatter(
            xInterpolados, 
            yInterpolados, 
            zInterpolados, 
            c=temperaturasInterpoladas, 
            cmap='viridis', 
            marker='x', 
            s=20,  # Tamanho menor para interpolados
            label='Pontos Interpolados'
        )

        # Adicionar uma barra de cores para representar as temperaturas
        barraCores = plt.colorbar(dispersaoInterpolada, ax=eixo, shrink=0.5, aspect=10)
        barraCores.set_label('Temperatura (°C)')

        # Definir os rótulos dos eixos
        eixo.set_xlabel('Eixo X (metros)')
        eixo.set_ylabel('Eixo Y (metros)')
        eixo.set_zlabel('Eixo Z (metros)')

        # Configuração inicial do título da figura para exibir os dados ao passar o cursor
        fig = eixo.figure
        fig.suptitle("Passe o cursor sobre os pontos para ver a temperatura", fontsize=12)

        def atualizarAnotacao(infoIndice, graficoDispersao, evento):
            # Obter o índice do ponto mais próximo
            indicePonto = infoIndice["ind"][0]
            if graficoDispersao == dispersaoOriginal:
                texto = f"Original - Temperatura: {pontosFiltrados[indicePonto]['temperatura']:.2f}°C"
            else:
                texto = f"Interpolado - Temperatura: {temperaturasInterpoladas[indicePonto]:.2f}°C"
            fig.suptitle(texto, fontsize=12)

        def PassarCursor(evento):
            # Verifica se o cursor está sobre o gráfico de dispersão
            tituloVisivel = fig._suptitle is not None
            if evento.inaxes == eixo:
                for graficoDispersao in [dispersaoOriginal, dispersaoInterpolada]:
                    contem, infoIndice = graficoDispersao.contains(evento)
                    if contem:
                        atualizarAnotacao(infoIndice, graficoDispersao, evento)
                        fig.canvas.draw_idle()
                        return
                if tituloVisivel:
                    fig.suptitle("Passe o cursor sobre os pontos para ver a temperatura", fontsize=12)
                    fig.canvas.draw_idle()

        # Ligar a função de hover ao evento de movimento do cursor
        fig.canvas.mpl_connect("motion_notify_event", PassarCursor)
        plt.show()



    @property
    def pontos(self):
        """
        Retorna:
            list: Lista de objetos PoseWithHeader que representam os pontos da trajetória.
        """
        return self._pontos
    
    @pontos.setter
    def pontos(self, pontos):
        """
        Define a lista de pontos da trajetória.

        Parâmetros:
            pontos (list): Lista de objetos PoseWithHeader.
        """
        self._pontos = pontos
