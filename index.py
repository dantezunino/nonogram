import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
import random

lili = []
filas = []
columnas = []
labelFilas = []
labelColumnas = []
winCondition = []
sisi = []

def setWinCondition():
    for l in lili:
        if l == "1":
            winCondition.append(l)
        else:
            pass

def limpieza():
    while len(lili) != 0:
        lili.remove(lili[0])
    while len(winCondition) != 0:
        winCondition.remove(winCondition[0])
    if len(sisi) != 0:
        sisi.remove(sisi[0])
    while len(filas) != 0:
        filas.remove(filas[0])
    while len(columnas) != 0:
        columnas.remove(columnas[0])
    while len(labelFilas) != 0:
        labelFilas.remove(labelFilas[0])
    while len(labelColumnas) != 0:
        labelColumnas.remove(labelColumnas[0])

def make_bitseq(s, k, lili):
    emptis = []
    tamanopi = int(k)
    tamano = tamanopi*tamanopi
    for letter in s:
        if letter == " ":
            pass
        else:
            emptis.append(bin(ord(letter))[2:])
    i = 0
    listaMasGrande = []
    while i < len(emptis):
        for bito in emptis[i]:
            listaMasGrande.append(bito)
        i += 1
    if len(listaMasGrande) < tamano:
        while len(listaMasGrande) < tamano:
            listaMasGrande.append("0")
    if len(listaMasGrande) > tamano:
        while len(listaMasGrande) > tamano:
            listaMasGrande.remove(listaMasGrande[1])
    for bini in listaMasGrande:
        lili.append(bini)


def botonio(a):
    a.background_color=(0,0,0,1)
    a.disabled=True
    winCondition.remove(winCondition[0])
    if len(winCondition) != 0:
        pass
    else:
        MyLayout.winScreen(MyLayout)
        winCondition.append("1")

def loser(b):
    MyLayout.loseScreen(MyLayout)

def comprension(kk):
    tamanuski = int(sisi[0])
    print(sisi[0])
    linea = tamanuski
    juju = 0
    while juju < tamanuski:
        filas.append("")
        columnas.append("")
        labelFilas.append("")
        labelColumnas.append("")
        juju += 1
    i = 0
    j = 0
    while j < tamanuski:
        while i < tamanuski:
            posicionF = (linea*j)+i
            posicionC = (linea*i)+j
            filas[j] += lili[posicionF]
            columnas[j] += lili[posicionC]
            i += 1
        i = 0
        j += 1
    h = 0
    while h < tamanuski:
        poporo = ""
        cotoro = ""
        sorongo = filas[h].split("0")
        porongo = columnas[h].split("0")
        for sara in sorongo:
            if len(sara) != 0:
                poporo += str(len(sara)) + " "
            else:
                pass
        for cara in porongo:
            if len(cara) != 0:
                cotoro += str(len(cara)) + " "
            else:
                pass
        labelFilas[h] = poporo
        labelColumnas[h] = cotoro
        h += 1

class MyLayout(Widget):
    def chhh(self):
        limpieza()
        choro = self.ids.pcho.text
        k = self.ids.biterios.text
        sisi.append(k) 
        make_bitseq(choro, k, lili)
        setWinCondition()
    
    def randomizar(self):
        i=0
        tat = ""
        while i < 200:
            tat += str(random.getrandbits(8))
            i += 1
        self.ids.pcho.text = tat
        
    
    def winScreen(self):
        view = ModalView(size_hint=(None, None), size=(600, 300))
        winLabel = Label(text="Ganaste viejo, bien ahí, qué capo que sos")
        view.add_widget(winLabel)
        view.open()

    def loseScreen(self):
        view = ModalView(size_hint=(None, None), size=(600, 300))
        loseLabel = Label(text="Mal ahí. Perdiste. Sos un gil")
        view.add_widget(loseLabel)
        view.open()

    def jueguito(self):
        self.chhh()
        view = ModalView(size_hint=(None, None), size=(600, 600))
        totoro = int(sisi[0])
        tablita = GridLayout(cols=totoro)
        superBoxy = BoxLayout(orientation='vertical')
        boxy = BoxLayout(orientation='horizontal')
        boxyLabel = BoxLayout(size_hint=(0.2,1), orientation='vertical')
        boxyTop = BoxLayout(size_hint=(1, 0.3), orientation='horizontal')
        blackspace = BoxLayout(size_hint=(0.2, 1), orientation='horizontal')
        boxyColu = BoxLayout(size_hint=(1, 1), orientation='horizontal')
        for bini in lili:
            if bini == "0":
                sat = Button(background_color=(1,1,1,1), on_press=loser)
                sat.bind(on_release=view.dismiss)
                tablita.add_widget(sat)
            if bini == "1":
                bat = Button(background_color=(1,1,1,1), on_press=botonio)
                tablita.add_widget(bat)
        comprension(self)
        blackspace.add_widget(Label(text=" "))
        blackspace.add_widget(Label(text=" "))
        for elemento in labelFilas:
            tic = Label(text=elemento)
            boxyLabel.add_widget(tic)
        for hache in labelColumnas:
            pasadena = hache.split(" ")
            ars = ""
            for pas in pasadena:
                ars += pas + "\n" + " " + "\n"
            mic = Label(text=ars, font_size=12)
            boxyColu.add_widget(mic)
        boxy.add_widget(boxyLabel)
        boxy.add_widget(tablita)
        boxyTop.add_widget(blackspace)
        boxyTop.add_widget(boxyColu)
        superBoxy.add_widget(boxyTop)
        superBoxy.add_widget(boxy)
        view.add_widget(superBoxy)
        view.open()


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()