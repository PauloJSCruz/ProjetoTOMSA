import argparse
from classTrajetoria import Trajetoria
from classTemperatura import Temperatura

def main():
    """
    Função principal que processa informações de trajetória de um drone.

    Esta função utiliza argparse para receber argumentos da linha de comando e realizar as seguintes operações:
    1. Processa um ficheiro de log de trajetória.
    2. Desenha a trajetória do drone em 3D com base nas informações de posição e orientação.

    Exemplos de Execução:
    ---------------------
    Exemplo de execução no terminal (linha de comando):
        $ python script.py --log caminho/para/o/log.txt
        $ python script.py --log caminho/para/o/log.txt --f 5

        - No exemplo mostrado, o ficheiro de log está localizado em "caminho/para/o/log.txt".
        - A frequência com que os vetores de orientação são mostrados na trajetória
         é definida como 5, significando que a cada 5 pontos de posição serão
         desenhados os vetores de orientação. Caso não seja definido nenhum número,
         os vetores de orientação serão desenhados em todos os pontos de posição
         da trajetória.

    Argumentos da linha de comando:
    -------------------------------
    --logPose : str (obrigatório)
        Especifica o caminho para o ficheiro de log de trajetória.

    --logTemp : str (opcional)
        Especifica o caminho para o ficheiro de log da temperatura.

    --f : int, (opcional)
        Define a frequência de com que os vetores de orientação são desenhados
        no gráfico. (default = 1).

    Exceções:
    ---------
    FileNotFoundError:
        Ocorre se o caminho do ficheiro de log fornecido não for válido ou o
        ficheiro não existir nesse caminho.

    IOError:
        Ocorre se o ficheiro de log não pode ser lido .

    Retorna:
    --------
    NULL
    """

    # Usando argparse para lidar com os argumentos
    parser = argparse.ArgumentParser(description='Processar informações de trajetória de um drone.')

    # Adicionar os argumentos
    parser.add_argument('--logPose', required=True, type=str, help='Caminho para o ficheiro de log de trajetória.')
    parser.add_argument('--logTemp', type=str, default="", help='Caminho para o ficheiro de log de temperatura (opcional).')
    parser.add_argument('--f', type=int, default=1, help='Frequência com que os vetores de orientação são desenhados no gráfico. (default = 1).')

    # Parse dos argumentos recebidos na linha de comando
    args = parser.parse_args()

    # Verifica se o caminho do ficheiro é válido para o logPose
    try:
        with open(args.logPose, 'r') as file:
            pass
    except FileNotFoundError:
        print("Erro: O caminho do ficheiro fornecido para logPose não é válido ou o ficheiro não existe.")
        return
    except IOError:
        print("Erro: O ficheiro logPose não pôde ser lido.")
        return

    # Verifica se o caminho do ficheiro é válido para o logTemp (caso seja fornecido)
    if args.logTemp:
        try:
            with open(args.logTemp, 'r') as file:
                pass
        except FileNotFoundError:
            print("Erro: O caminho do ficheiro fornecido para logTemp não é válido ou o ficheiro não existe.")
            return
        except IOError:
            print("Erro: O ficheiro logTemp não pôde ser lido.")
            return

    # Inicializa a trajetória, lê o ficheiro log e cria os objetos
    trajetoria = Trajetoria(args.f)
    trajetoria.ReadLogTrajetoria(args.logPose)
    nome = args.logPose.split("/")[1].strip()
    nome = nome.split(".")[0].strip()
    trajetoria._nome = nome

    if not args.logTemp:
        # Desenha os pontos da trajetória com os respetivos vetores orientação
        trajetoria.PlotTrajetoria()
    else:
        temperatura = Temperatura()
        temperatura._nome = trajetoria._nome
        temperatura.ReadLogTempratura(args.logTemp)
        trajetoria.PlotTrajetoria(temperatura._pontosTemperatura)

    print("-- END --")

if __name__ == "__main__":
    main()
