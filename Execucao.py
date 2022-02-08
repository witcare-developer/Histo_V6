import threading
import time
from turtle import color
from Saidas import Saidas

class Execucao(threading.Thread):
    def __init__(self, dado, tela):
        threading.Thread.__init__(self)
        self._dado = dado
        self._tela = tela

    def run(self):
        print("Esta na rotina executando.")
        print(self._dado.temperatura_sistema)
        time.sleep(5)
        self._dado.set_texto_nome_processo("Estamos Processando")
        self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_nome_processo_TelaProcessando.objText, text=self._dado.texto_nome_do_processo)
        self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)        
        print("Saiu da rotina executando.")
        print(self._dado.temperatura_sistema)