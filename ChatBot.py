import json
import subprocess as sp
from builtins import eval

class ChatBot():

    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["Jr", "Priscila"], {"Oi": "Olá, qual o seu nome?", "Tchau": "Até à próxima!", '
                          '"oi": "Olá, qual o seu nome?", "Bot abra a pasta petropolis": "petropolis", '
                          '"Bot abra a pasta pv": "pv", "Bot abra o chrome": "chrome", '
                          '"Bot abra a ibm blue mix": "ibm", "Bot abra meu email": "email",'
                          '"Bot abra o my times": "times"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]

    def escuta(self, frase=None):
        if frase == None:
            frase = input('Você: ')

        # if frase == 'anote' or frase == 'Anote':
        #     return frase
        # frase = frase.lower()
        #frase = str(frase)
        return frase

    def pensa(self, frase):

        # frase = frase.title()

        if frase in self.frases:
            return self.frases[frase]

        if frase == 'Anote' or frase == 'anote':
            return 'Digite a pergunta'


        # salva perguntas e respostas na memoria
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual o seu nome?':
            resposta = self.conhecido(frase)
            return resposta

        if ultimaFrase == 'Digite a pergunta':
            self.chave = frase
            return 'Digite a resposta'
        if ultimaFrase == 'Digite a resposta':
            self.frases[self.chave] = frase
            self.gravaMemoria()
            return 'Anotado'


        if frase == 'tchau':
            resposta ='Bye'
            return resposta

        try:
            resposta = eval(frase)
        except:
            resposta = 'Não tenho essa resposta. Pode me ensinar!?'

        return resposta


    def fala(self, frase):

        self.abrir(frase)
        print(frase)
        self.historico.append(frase)


    def conhecido(self, usuario):
        nome = usuario.title()
        if nome in self.conhecidos:
            resp = 'Muito prazer em ter você aki novamente'
        else:
            self.conhecidos.append(nome)
            self.gravaMemoria()
            resp = 'Muito prazer em conhece-lo {nome}'

        return resp

    def abrir(self, frase):

        if frase == 'petropolis':
            try:
                sp.Popen(['xdg-open', '/home/anselmojunior/projeto_petropolis'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

        if frase == 'pv':
            try:
                sp.Popen(['xdg-open', '/home/anselmojunior/projeto_pv'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

        if frase == 'chrome':
            try:
                sp.Popen(['xdg-open', 'http://www.google.com'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

        if frase == 'ibm':
            try:
                sp.Popen(['xdg-open', 'https://cloud.ibm.com/'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

        if frase == 'email':
            try:
                sp.Popen(['xdg-open', 'https://exchange.embratelmail.com.br/owa/#path=/mail'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

        if frase == 'times':
            try:
                sp.Popen(['xdg-open', 'https://mytimes.embratel.com.br:20443/MyTimes/Login2.xhtml'])
                print('Aberta')
            except FileNotFoundError:
                print('Sorry. Algo deu errado.')

    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()
