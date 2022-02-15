import threading
import time
from Saidas import Saidas
from Dados import Dado

class Beep(threading.Thread):
    def __init__(self, dado):
        threading.Thread.__init__(self)
        self.out = Saidas()
        self.dado = dado
        
    def run(self):
        while True:
            if self.dado.aciona_buzzer == True:  
                #print('Beeeep!')    
                #self.out.buzzer(1)
                time.sleep(0.2)
                self.out.buzzer(0)
                self.dado.aciona_buzzer = False
