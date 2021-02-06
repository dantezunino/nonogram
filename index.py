import kivy
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.input.providers import mouse
from kivy.clock import Clock
from kivy.core.window import Window
import random
import string

lili = []
filas = []
columnas = []
labelFilas = []
labelColumnas = []
winCondition = []
sisi = []
clickerio = ["left"]

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
    if clickerio[0]=="right" or clickerio[0]=="middle":
        a.background_normal=''
        a.background_disabled_down=''
        a.background_color=(0.6,0.4,0.4,0.7)
    else:
        a.background_normal=''
        a.background_disabled_down=''
        a.background_color=(0.25,0.25,0.25,1)
        a.disabled=True
        winCondition.remove(winCondition[0])
        if len(winCondition) != 0:
            pass
        else:
            MyLayout.winScreen(MyLayout)
            winCondition.append("1")

def loser(b):
    print(clickerio[0])
    if clickerio[0]=="right" or clickerio[0]=="middle":
        b.background_disabled_normal=''
        b.background_disabled_down=''
        b.background_color=(0.6,0.4,0.4,0.7)
        b.disabled=True
    if clickerio[0]=="left":
        pass
        #MyLayout.loseScreen(MyLayout)

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
        
    def on_touch_down(self, touch, after=False):
        if after:
            clickerio[0] = touch.button
            #mm = touch.pos
            #for widget in self.walk():
            #    print(widget)
            return
        else:
            Clock.schedule_once(lambda dt: self.on_touch_down(touch, True))
            return super(MyLayout, self).on_touch_down(touch)

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
        while i < 100:
            tat += random.choice(string.ascii_letters)
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
    
    def something(self):
        self.ids.caroso.load_previous()
        self.ids.nonogram.clear_widgets()

    def jueguito(self):
        
        self.chhh()
        #self.view = ModalView(size_hint=(None, None), size=(600, 600))
        totoro = int(sisi[0])
        self.tablita = GridLayout(cols=totoro)
        self.superBoxy = BoxLayout(orientation='vertical')
        self.boxy = BoxLayout(orientation='horizontal')
        self.boxyLabel = BoxLayout(size_hint=(0.2,1), orientation='vertical')
        self.boxyTop = BoxLayout(size_hint=(1, 0.3), orientation='horizontal')
        self.blackspace = BoxLayout(size_hint=(0.2, 1), orientation='horizontal')
        self.boxyColu = BoxLayout(size_hint=(1, 1), orientation='horizontal')
        for bini in lili:
            if bini == "0":
                self.sat = Button(background_down="",background_color=(1,1,1,1), on_release=loser)
                #self.sat.bind(on_press=(trigger_action(duration=0.1))
                self.tablita.add_widget(self.sat)
            if bini == "1":
                self.bat = Button(background_down="", background_color=(1,1,1,1), on_press=botonio)
                self.tablita.add_widget(self.bat)
        comprension(self)
        self.blackspace.add_widget(Button(text="BACK", background_color=(0,0,0.5,0.5), on_press=lambda a:self.something()))
        for elemento in labelFilas:
            self.tic = Label(text=elemento)
            self.boxyLabel.add_widget(self.tic)
        for hache in labelColumnas:
            pasadena = hache.split(" ")
            ars = ""
            for pas in pasadena:
                ars += pas + "\n" + " " + "\n"
            self.mic = Label(text=ars, font_size=12)
            self.boxyColu.add_widget(self.mic)
        self.boxy.add_widget(self.boxyLabel)
        self.boxy.add_widget(self.tablita)
        self.boxyTop.add_widget(self.blackspace)
        self.boxyTop.add_widget(self.boxyColu)
        self.superBoxy.add_widget(self.boxyTop)
        self.superBoxy.add_widget(self.boxy)
        #self.view.add_widget(self.superBoxy)
        #self.view.open()
        
        #self.ids.bigLayout.clear_widgets()
        self.ids.nonogram.add_widget(self.superBoxy)
        self.ids.caroso.load_next()

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()