'''
===============================================================================
Kapitel 2 Modularer Programmentwurf
===============================================================================
'''

'''
Modularer Programmentwurf
- Kleinere Programme, die einfache Tätigkeiten erledigen, sogenannte Bausteine, 
  werden geschickt zu grösseren Programmen, die komplexere Tätigkeiten erledigen, kombiniert.
- Erweiterung der Programmiersprache um neue Befehle

Analogie:
- In der Umgangssprache definieren wir auch neue Wörter. 
  Einen "Begriff googlen" kann als Erweiterung der Umgangssprache verstehen. 
  "Googlen" besteht eine Kombination aus einfachen Tätigkeiten, wie 1. Laptop/Handy öffnen, 2. Browser öffnen, 
  3. Browser öffnen, 4. URL www.google.ch eingeben, 5. Begriff eintippen, 6. Enter drücken...

Lernziele:
- mit Hilfe des modularen Entwurfs komplexere aber immer noch übersichtliche Programme erstellen
- Programmieren von Animationen
'''

'''
===============================================================================
Unterkapitel 2.1 Neue Befehle definieren und verwenden
===============================================================================
''' 


''' Beispiel 2.1: Befehl quadrat100 definieren '''

from gturtle import *

def quadrat100():       # neuen Befehl mit Namen quadrat100 definieren
   repeat 4:           # Beschreibung des neuen Befehls quadrat100.
       forward(100)    # Alle Zeilen, die unterhalb von def eingericht sind, 
       right(90)       # gehören zum Körper des Befehls.
                       # Der Computer lernt den Befehl, führt ihn aber nicht aus.

makeTurtle()
quadrat100()
left(45)
quadrat100()


''' Aufgabe 2.1: Definition und Nutzung Befehl dreieck50 (Bitte lösen)'''


''' Konzepte und Begriffe
- def <Befehlsname>: Mit def bringen Sie dem Computer einen neuen Befehl bei.
  Der Befehlsname muss am Ende immer Klammern haben.
  Nach dem Namen und den Klammern kommt der Doppelpunkt.
  Darunter steht gegenüber def eingerückt die Beschreibung des neuen Befehls.
  Diese Beschreibung bezeichnet man als Körper des Befehls.
- Der Name des Befehls muss ein Wort ohne Leerzeichen oder Umlaute (also "ä", "ö" oder "ü") sein.
  Wenn Sie mehrere Wörter zu einem Namen zusammenfügen möchten, dann können sie den Unterstrich verwenden.
  Sie dürfen eine Zahl anhängen, aber nicht mit einer Zahl beginnen.
  Beispiel: name_mit_3_woertern()
- Wenn Sie einen Befehl mit def definieren, dann zeichnet die Turtle noch nichts.
  Der Computer lernt zwar die Bedeutung des neuen Wortes, aber dies ist auf dem Bildschirm nicht sichtbar.
  Der Computer zeichnet erst dann etwas, wenn Sie den neuen Befehl im Programm auch aufrufen.
  Ein neuer Befehl muss immer vor dem ersten Aufruf definiert werden.
'''
    

''' Beispiel 2.2: Befehl quadrat100 nutzen um ein Fenster zu zeichnen '''
from gturtle import *

def quadrat100():       # neuen Befehl mit Namen quadrat100 definieren
   repeat 4:           # Beschreibung des neuen Befehls quadrat100.
       forward(100)    # Alle Zeilen, die unterhalb von def eingericht sind, 
       right(90)       # gehören zum Körper des Befehls.
                       # Der Computer lernt den Befehl, führt ihn aber nicht aus.

makeTurtle()
repeat 4:
   quadrat100()
   left(90)


''' Aufgabe 2.2: Blumen zeichnen (Bitte lösen)'''



''' Programme und Unterprogramme '''

''' Hinweise: Hauptprogramme und Unterprogramme
- Ein Programm (siehe Beispiel 2.2) besteht aus einem Hauptprogramm und mehreren Unterprogrammen.
'''

from gturtle import *

def quadrat100():       # neuen Befehl mit Namen quadrat100 definieren
   repeat 4:           # Beschreibung des neuen Befehls quadrat100.
       forward(100)    # Alle Zeilen, die unterhalb von def eingericht sind, 
       right(90)       # gehören zum Körper des Befehls.
                       # Der Computer lernt den Befehl, führt ihn aber nicht aus.

makeTurtle()
repeat 4:
   quadrat100()
   left(90)


''' Hinweise: langfristiges Speichern
- Befehle können langfristig gespeichert werden.
- Variante 1: in TigerJython ("Dauerhaft markieren/speichern")
- Variante 2: in separate Datei auslagern. Achtung: Dateien in demselben Ordner speichern
'''

''' Aufgabe 2.4: Gleichseitiges Dreieck (Bitte lösen)'''


''' Aufgabe 2.5: Quadrate (Freiwillige Aufgabe)'''


''' Aufgabe 2.7: Offene Quadrate (Freiwillige Aufgabe)'''


''' Was ich gelernt habe 
- neue Befehle definieren
    - Namen des neuen Befehls nach def und dem Doppelpunkt
    - Körper des Befehls eingerückt
- Entwurfstechnik "modularer Entwurf"
    - Jeder Baustein beinhaltet einen überschaubaren Teil des Programs und hat einen eindeutigen Namen
'''

'''
===============================================================================
Unterkapitel 2.2 Der modulare Entwurf mit Schleifen
===============================================================================
'''

'''
Wie bereits bekannt, darf man repeat auch im Körper einer anderen Schleife verwenden und so eine Schleife in eine andere setzen.
Übersichtlicher ist es aber oftmals, wenn du den modularen Entwurf verwendest und für die innere Schleife eigenen eigenen Befehl definierst.
'''

''' Beispiel 2.3: Quadrat mit runden Ecken '''
from gturtle import * 

makeTurtle()
repeat 4:
   repeat 9: 
       forward(4)
       left(10)
   forward (75) 

''' Fragen 
1. Ist das übersichtlich?
2. Wie könnt man hier jetzt mit dem modularen Entwurf die Lesbarkeit verbessern?
'''


''' Schleifen durch Befehle ersetzen zur Erhöhung der Verständlichkeit '''
from gturtle import * 

def viertelkreis():
   repeat 9: 
       forward(4)
       left(10)

def rund_quadrat():
   repeat 4:
       viertelkreis()    
       forward(75) 

makeTurtle()
rund_quadrat()


''' Hinweise: Was ein gutes Programm ausmacht
- Zerlegen Sie eine komplexe Problemstellung, wenn es sinnvoll ist, in einfachere Teilaufgaben. 
Entwickeln Sie für jede dieser Teilaufgaben einen Befehl. 
Setzen Sie die Befehle für die Teilaufgaben in einem Programm so dass die ursprünglichen Problemstellung gelöst wird. 
- Für ein gut strukturiertes Programm gilt folgende Regel: 
Sie sehen bei jedem Programmteil sofort, was er macht und wie er es macht. 
Beispielsweise sehen Sie im Programm oben, wie das «runde Quadrat» gezeichnet wird:
Viermal nacheinander werden ein Viertelkreis und eine gerade Linie der Länge 75 gezeichnet. 
'''


''' Aufgabe 2.8 A: Halbkreise horizontal nebeneinander (Bitte lösen) '''

''' Aufgabe 2.8 B: Quadrate als Pfeilspitze (Bitte lösen) '''

'''
===============================================================================
Unterkapitel 2.3 Befehle in Befehlen verwenden
===============================================================================
''' 

''' Beispiel 2.4: Farbiger Stern '''

''' Hinweis: Schrittweises entwickeln des Programms '''

from gturtle import *

def zacke():
   forward(100)
   left(120)
   forward(100)
   right(60)

def zacke_rot():
   setPenColor("red")
   zacke()

def zacke_blau():
   setPenColor("blue")
   zacke()

def stern():
   repeat 3:
       zacke_rot()
       zacke_blau()

makeTurtle()
stern()


''' Aufgabe 2.9: 2x2-Fenster (Bitte lösen) '''


'''
===============================================================================
Unterkapitel 2.4 Animationen programmieren
===============================================================================
'''

''' Beispiel 2.5: Animation '''
from gturtle import * 

def dreieck100():
   repeat 3:
       forward(100)
       right(120)

def zeige_dreieck():
   setPenColor("red")
   dreieck100()
   delay(1000)
   setPenColor("white")
   dreieck100()
   
makeTurtle()
hideTurtle()
repeat 50:
   zeige_dreieck()
   right(90)
   penUp()
   forward(5)
   penDown()
   left(90)
showTurtle()

''' Fragen
- Wie könnte man die Lesbarkeit noch verbessern?
  - Die Befehle right(90) bis left(90) zusammenfassen zu einem Befehl?
  - Ist der Name des Befehls zeige_dreieck klar?
- Wie können wir die die Animation schneller machen?
'''

''' Aufgabe 2.12: nach oben laufendes rotes Quadrat (Bitte lösen) '''

''' neue Konzepte und Begriffe
- Figur löschen: Überschreiben mit weisser Farbe
- hideTurtle/showTurtle: 
- delay(<Zeit>): Warten in Millisekunden
'''

''' Aufgabe 2.13: Sekundenzeiger '''
# Musterlösung

from gturtle import * 

def zeige_sekundenzeiger():
   setPenWidth(2)
   setPenColor("red")
   forward(100)
   delay(1000)
   setPenWidth(4)
   setPenColor("white")
   backward(100)
   setPenWidth(2)
   
makeTurtle()
hideTurtle()
repeat 60:
   zeige_sekundenzeiger()
   right(360/60)
showTurtle()

''' Aufgabe 2.15: Digitaler Zähler (Bitte in 3er/4er-Gruppen lösen) '''

''' Aufgabe 2.18: Tieranimation (Bitte lösen) '''

''' Was ich gelernt habe 
- Unterschiedliche Befehle können als Bausteine und anschliessend zusammengesetzt werden, um komplexere Programme zu schreiben
- Animationen erstellen durch Lösen als übermalen mit weisser Farbe.
'''

'''
===============================================================================
Selbsttest
===============================================================================
'''

''' Konzepte und Befehle (Bitte lösen) '''


''' Aufgaben (Bitte lösen) '''

''' Selbsttest-Aufgabe 2.2 (Schneeflocke) '''

# Musterlösung
from gturtle import *

def astspitze():
   left(45)
   repeat 3:
       forward(40)
       backward(40)
       right(45)
   left(2*45)
       
def ast():
   forward(40)
   astspitze()
   backward(40)
   
def schneeflocke():
   repeat 6:
       ast()
       left(360/6)

makeTurtle()
hideTurtle()
schneeflocke()

''' Selbsttest-Aufgabe 2.5 (fünfzackiger Stern) '''
# Musterlösung

from gturtle import *

# Zeichne ein gleichseitiges Dreieck linksherum startend mit einer Seite in Blickrichtung der Turtle
def gleichseitiges_dreieck():
   repeat 3:
       forward(100)
       left(120)
       
def fuenfseitiger_stern():
   repeat 5:
       gleichseitiges_dreieck()
       forward(100)
       right(360/5)

makeTurtle()
hideTurtle()
fuenfseitiger_stern()
