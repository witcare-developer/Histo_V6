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
        self.config_ganho_proporcional()
        self.config_setpoint()
        self.config_nome_banho()
        self.config_display_banhos()

        cnt_temp = 0

        while self._dado.controle_estah_acionado:
            self.toggle_banho(self._index_banho)

            time.sleep(1)

            cnt_temp += 1

            if cnt_temp >= 5:
                self._index_banho += 1
                if self._index_banho >= len(self._rotina.banho.nome_banho):
                    self._index_banho = 0
                    self.config_display_banhos()

                self.config_ganho_proporcional()
                self.config_setpoint()
                self.config_nome_banho()
                
                cnt_temp = 0

    def config_ganho_proporcional(self):
        self._dado.set_ganho_poporcional_sistema(self._rotina.banho.ganho_proporcional[self._index_banho])
    
    def config_setpoint(self):
        self._dado.set_temperatura_set_point(self._rotina.banho.temperatura_banho[self._index_banho])

    def config_nome_banho(self):
        self._dado.set_texto_nome_processo(self._rotina.banho.nome_banho[self._index_banho])
        self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_nome_processo_TelaProcessando.objText, text=self._dado.texto_nome_do_processo)

    def config_display_banhos(self):
        if self._dado.formol_esta_ativado == True:
            if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            else:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)

        else:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)

        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
        
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
        
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            
            if self._dado.reagente == self._dado.REAGENTE_XILOL or self._dado.reagente == self._dado.REAGENTE_WITCLEAR:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
            else:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            

    def toggle_banho(self, index):
    
        if self._rotina.banho.nome_banho[self._index_banho] == "FORMOL" or self._rotina.banho.nome_banho[self._index_banho] == "FORMOL1":
            self.toggle_color(self._tela.btind_primeira_fixacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._index_banho] == "FORMOL2":
            self.toggle_color(self._tela.btind_segunda_fixacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_primeira_fixacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._index_banho] == "ALCOOL1":
            self.toggle_color(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec)
            if self._rotina.banho.nome_banho[self._index_banho-1] == "FORMOL2":
                self.acende_anterior(self._tela.btind_segunda_fixacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "ALCOOL2":
            self.toggle_color(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "ALCOOL3":
            self.toggle_color(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "ALCOOL4":
            self.toggle_color(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "ALCOOL5":
            self.toggle_color(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._index_banho] == "XILOL1" or self._rotina.banho.nome_banho[self._index_banho] == "ISOPROPANOL1" or self._rotina.banho.nome_banho[self._index_banho] == "WITCLEAR1":
            self.toggle_color(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec)
            if self._rotina.banho.nome_banho[self._index_banho-1] == "ALCOOL5":
                self.acende_anterior(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec)
        
            if self._rotina.banho.nome_banho[self._index_banho-1] == "ALCOOL3":
                self.acende_anterior(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "XILOL2" or self._rotina.banho.nome_banho[self._index_banho] == "ISOPROPANOL2" or self._rotina.banho.nome_banho[self._index_banho] == "WITCLEAR2":
            self.toggle_color(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._index_banho] == "XILOL3" or self._rotina.banho.nome_banho[self._index_banho] == "ISOPROPANOL3" or self._rotina.banho.nome_banho[self._index_banho] == "WITCLEAR3":
            self.toggle_color(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec)
            self.acende_anterior(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec)
        
        

    def toggle_color(self, obj):

        if self._toggle == True:
            self._tela.canvas_TelaProcessando.itemconfig(obj, fill= self._dado.green)
        else:
            self._tela.canvas_TelaProcessando.itemconfig(obj, fill= self._dado.cor_indicacao_processo)

        self._toggle = not self._toggle

    def acende_anterior(self, obj):
        self._tela.canvas_TelaProcessando.itemconfig(obj, fill= self._dado.green)


    