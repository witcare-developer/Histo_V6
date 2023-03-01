## Processador Histológico por Microondas Versão 6 - Fevereiro de 2022

### Configurações
```
1 - Instalar Raspibian no cartão SD

2 - Baixar o código do github no diretório home/pi:
    git clone https://github.com/witcare-developer/Histo_V6.git
    
3 - Configurar o raspberry para comunicação I2C para comunicação com sensor IR:
    Menu->Preferencias->Raspberry Pi Configuration->Interfaces->I2C=Enable.
    Reiniciar o Raspberry.
    
4 - Instalar o pacote para o LCD:
    a) Faca o clone: git clone https://github.com/goodtft/LCD-show.git
    b) chmod -R 755 LCD-show
    não execute o comando que habilita o LCD ainda
    link com tutorial: http://www.lcdwiki.com/3.5inch_RPi_Display
    
5 - Fazer comando para que inicie o Raspberry rodando a aplicação:
    a) Primeiro, abra o terminal e digite o seguinte comando para criar um arquivo .desktop no diretório autostart:
       sudo mousepad /etc/xdg/autostart/display.desktop .
       Usamos display.desktop como nome de arquivo, mas você pode nomear o arquivo da área de trabalho como quiser.
    b) No arquivo .desktop, adicione as seguintes linhas de código:
        [Desktop Entry]
        Name=Histo_V6
        Exec=/usr/bin/python3 /home/pi/Histo_V6/main.py 
       O diretório /usr/bin/pythyon3 é onde está instalado o python,normalmente no raspberry esse é o local padrão.
       
6 - Agora vá até o diretório onde foi baixado os arquivos do LCD-show:
    a) cd /home/pi/LCD-show/
    b) sudo ./LCD35-show
    executando esse último comando o sistema irá reiniciar agora com o LCD e a aplicação rodando
    
7 - Para sair do modo LCD-show tem que, com o teclado, apertar crtl+alt e esc ou F1 até aparecer o console, 
    depois digite LCD-hdmi. O sistema vai reiniciar e voltar com o monitor mais a aplicação. Se quiser 
    parar a aplicação abra um terminal - ctrl+alt+T e digite "ps axf" abrirá as execuções. Na coluna 
    comando procure bin/python3 e veja o número do PID em seguida execute sudo kill e o número do PID.
```
