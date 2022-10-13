
import threading
import os                                                          
from multiprocessing import Pool


def call_madeira() -> None:
    """Chamar Funções """
    from madeira import MadeiraMadeira
    madeira =  MadeiraMadeira()
    madeira.get_produtos()
    madeira.compara_precos()

def call_google() -> None:
    """Chamar Funções """
    from google import GoogleShopping

    google = GoogleShopping()
    google.get_produtos()
    google.compara_precos()

def inicia_programa(nome_arquivo):
    print(nome_arquivo)
    os.system('py -3.9.2 {}'.format(nome_arquivo))
    
if __name__ == "__main__":

    arquivos = [call_madeira()]

    processos = []
    for arquivo in arquivos:
        processos.append(threading.Thread(target=inicia_programa, args=(arquivo,)))

    for processo in processos:
        processo.start()