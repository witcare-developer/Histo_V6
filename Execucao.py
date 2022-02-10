import threading
import time
from turtle import color
from Saidas import Saidas

class Execucao(threading.Thread):
    def __init__(self, dado, tela, rotina):
        threading.Thread.__init__(self)
        self._dado = dado
        self._tela = tela
        self._rotina = rotina
        self._index_banho = 0
        self._toggle = True

    def run(self):
        while self._dado.controle_estah_acionado:
            self.config_ganho_proporcional()
            self.config_setpoint()

            self.toggle_banho(self._index_banho)

            time.sleep(1)
        # while self._dado.controle_estah_acionado:
        #     time.sleep(1)
        #     #print(self._dado.temperatura_sistema)

        #     #self._rotina.banho.temperatura_banho[0]
        #     #self._rotina.banho.tempo_banho[0]
        #     #self._rotina.banho.ganho_proporcional[0]
        #     #self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)        
            
        #     self._dado.set_texto_nome_processo(self._rotina.banho.nome_banho[self._index_banho])
        #     self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_nome_processo_TelaProcessando.objText, text=self._dado.texto_nome_do_processo)
            
        #     self._index_banho += 1
        #     print( "{} / {}".format(self._index_banho, len(self._rotina.banho.nome_banho)) )

        #     if self._index_banho >= len(self._rotina.banho.nome_banho):
        #         self._index_banho = 0

        #     self.toggle_banho()

    def config_ganho_proporcional(self):
        self._dado.set_ganho_poporcional_sistema(self._rotina.banho.ganho_proporcional[self._index_banho])
    
    def config_setpoint(self):
        self._dado.set_temperatura_set_point(self._rotina.banho.temperatura_banho[self._index_banho])

    def toggle_banho(self, index):
        if self._toggle == True:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)
        else:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)

        self._toggle = not self._toggle

    