'''
===============================================================================
Kapitel 3 Variablen, Speicherung und Verarbeitung von Daten
===============================================================================
'''

'''
Bisher:
- Eingeschränkte Funktion, z. B. Zeichnen eines Quadrates mit Seitenlänge 100.
- Die Grösse 100 haben wir fest vorgegeben.

Neu:
- Programme sollen abhängig von Eingaben von Benutzern oder von Daten im Speicher arbeiten.
- Das Konzept der Variable ermöglicht dem Computer Daten einzulesen, auszugeben und zu speichern.

Lernziele:
- In diesem Kapitel lernst du mit Variablen umzugehen, ihnen Werte zuzuweisen und mit ihner Werten zu rechnen. 
'''

'''
===============================================================================
Kapitel 3.1 Einem Befehl Parameterwerte übergeben
===============================================================================
'''

''' Beispiel 3.1: Parameter übergeben '''

#def werteuebergabe(x1, x2, x3):
#    print("x1 =", x1, "x2 =", x2, "x3 =", x3)
#
#werteuebergabe(-7, 3, 6)
#werteuebergabe(0, 100, 56)
#werteuebergabe(3, 3, 3)

''' Erläuterung 
- Mit "def werteuebergabe(x1, x2, x3)" reserviert der Computer drei Speicherplätze mit Namen x1, x2 und x3.
- Die Variablen nennen wir auch Parameter des Befehls werteuebergabe().
- Parameter sind spezielle Variablen, der Werte beim Aufruf des Befehls in Klammern übergeben werden.

Ablauf des Programms (mit Debugger)
- Nach Ablauf des Aufruf eines Befehles werden die Werte der Parameter gelöscht.
'''

''' Konzepte und Begriffe
Arbeiten mit dem Speicher:
- Variablen ermöglichen das Arbeiten mit dem Speicher des Computers. 
- Parameter sind eine Form von Variablen. Die Werte von Parametern werden beim Aufruf in Klammern gesetzt.

Aufruf von Befehlen mit Parametern:
- Beim Befehlsausruf werden in Klammern so viele Werte mitgegeben, wie Parameter (=Variablen) bei der Befehlsdefinition stehen.
- Die Werte beim Aufruf werden von links nach rechts den Variablen in der Definition zugeordnet.
- Im Computer werden diese Werte auf Speicherplätze abgespeichert, die den Namen dieser Variablen als Bezeichnung haben.

Auswertung von Variablen:
- "Sieht" der Computer bei der Ausführung einer Programmzeile nicht eine Zahl oder einen Text, sondern eine Variable, 
geht er an den entsprechenden Platz im Speicher und ersetzt den Wert der Variablen durch diesen Wert.
- Erst dann führt der Computer die Anweisung mit konkreten Werten aus.

Fehlerhafte Aufrufe von Befehlen mit Parametern:
- Falls beim Aufruf zu wenige Werte mitgegeben werden, weigert sich der Computer, den Befehl auszuführen.
Beispiel: werteuebergabe(3, 3)
- Falls eine Variable noch keinen Wert zugewiesen bekommmen hat, kann der Computer bei der Ausführung die Variable nicht durch eine Wert ersetzen.
Beispiel: print(x4)
'''


''' Beispiel 3.2 '''

#def quadrat100():
#    repeat 4:
#        forward(100)
#        right(90)
#
#def quadrat200():
#    repeat 4:
#        forward(200)
#        right(90)
#
#def quadrat400():
#    repeat 4:
#        forward(400)
#        right(90)

''' Diskussion:
- Keine praktikable Lösung. (Wir haben auch nicht einen Befehl forward100, forward200 usw.)

Ansatz: 
1. Die Seitenlänge wollen wir frei wählbar machen.
2. Damit der Wert zur Verfügung steht, definieren wir den Wert als Parameter.
'''

#from gturtle import *
#
#def quadrat(seite):
#    repeat 4:
#        forward(seite)
#        right(90)
#
#makeTurtle()
#quadrat(100)
#quadrat(200)


''' Aufgabe 3.1: Sechsecke (Bitte lösen) '''


''' Beispiel 3.3 '''
''' Schritt:
1. Zeichnen: Rechtwinkliges gleichschenkliges Dreieck mit Winkeln und Katheten und Hypothenuse zeichnen.
2. Erläutern: Wir können die Werte von Parametern nutzen, um weitere Werte zu berechnen.
- Wir möchten einen Befehl rw_dreieck schreiben, bei der die Länge der Katheten als Parameter mitgegeben werden kann.
- Wir berechnen die Länge der Hypothenuse im Befehl.
3. Aufruf festlegen
4. Implementation
'''

#from gturtle import *
#
#def rw_dreieck(kathete):
#    print("hier kommt das Zeichnen hin")
#
#makeTurtle()
#rw_dreieck(100)


#from gturtle import *
#
#def rw_dreieck(kathete):
#    right(45)
#    forward(kathete)
#    right(90)
#    forward(kathete)
#    right(135)
#    forward(kathete * sqrt(2))
#
#makeTurtle()
#rw_dreieck(100)


''' Beispiel 3.4: Treppe zeichnen '''

''' Treppe mit Höhe 240 Pixel und Breite 300 Pixel.
Wir wollen die Anzahl Stufen eingeben. 
Das Programm soll die Höhe und Breite der Stufen berechnen.'''

#from gturtle import *
#
#def treppe(anzahl_stufen):
#    repeat anzahl_stufen:
#        forward(240 / anzahl_stufen)
#        right(90)
#        forward(300 / anzahl_stufen)
#        left(90)
#    
#makeTurtle()
#treppe(4)


''' Aufgabe 3.2: Regelmässige Vielecke (Bitte lösen) '''


''' Texte als Parameter '''

''' 
- Der Befehl farb_quadrat hat zwei Parameter: seite und farbe.
- Neu: Die Werte von Parametern können nicht nur Zahlen, sondern auch Texte (Datentyp string) sein.
'''

#from gturtle import *
#
#def farb_quadrat(seite, farbe):
#    setPenColor(farbe)
#    repeat 4:
#        forward(seite)
#        right(90)
#    
#makeTurtle()
#farb_quadrat(100, "red")
#left(45)
#farb_quadrat(100, "gold")


''' Aufgabe 3.3: Farbige Dreiecke (Bitte lösen) '''


''' Aufgabe 3.4: Farbige Vielecke (Bitte lösen) '''


''' Aufgabe 3.7: Rotes Dreieck mit Fehlern (Bitte lösen) '''


''' Aufgabe 3.8: Warum sollten Parameter möglichst sinnvolle Namen haben (Diskussion) '''

''' Was wir gelernt haben:
- Befehle ohne Parameter: def befehlsname():
- Befehle mit Parametern: def befehlsname(parameter1, parameter2, ...):

Beachte:
Beim Aufruf: 
- Übergabe der korrekten Anzahl Werte (Zahlen, Texte, Ausdrücke) in der korrekten Reihenfolge.
- Erzeugen von Speicherplätzen(=Variablen) mit den Parameternamen. Die Variablen bekommen als Wert die übergebenen Werte.
'''


'''
===============================================================================
Kapitel 3.2 Wie der Computer mit Variablen arbeitet
===============================================================================
'''

#from gturtle import *
#
#def vieleck(anzahl_ecken, seite):
#    repeat anzahl_ecken:
#        forward(seite)
#        right(360/anzahl_ecken)
#
#makeTurtle() 
#vieleck(36, 720/36)

''' Wie läuft das Programm ab?
Simulation des Programmablaufs:
- Links: Programm zeigen und nächste durchzuführende Zeile hervorheben
- Rechts: Tabellen in OneNote zeichnen

1. Zeile vieleck(36, 720/36)
- Ausrechnen der Parameter
- Aufruf der Funktion

2. Zeile def vieleck(anzahl_ecken, seite):
- Tabelle "Vieleck" erstellen. (Die Tabelle ist ein vereinfachtes Modell des effektiven Speichers des Rechners.)
- Die Tabelle hat zwei Zeilen (=Variablen) für die zwei Parameter.
- Die Werte der Variablen werden auf die beim Funktionsaufruf geänderten Werte gesetzt.

3. Körper des Befehls vieleck ausführen:
- Während der Durchführung schaut der Computer die Variablenwerte jeweils in der Tabelle nachschauen.


Vergleiche mit der Durchführung im Debugger!
'''

'''
- print-Befehle einführen
'''

''' Aufgabe 3.9: Tabelle für Rechtecke zeichnen (Bitte lösen) '''


''' Was wir gelernt haben:
- Zu jedem Befehlsaufruf mit Variablen erzeugt der Computer eine Tabelle. 
- Die Tabelle enthält für jede Variable des Befehls eine Zeile mit dem Namen und dem Wert der Variablen. 
- Beim Befehlsaufruf setzt Python für jeden Parameter einen Wert (z. B. eine Zahl oder einen Text) in die entsprechende Zeile der Tabelle ein. 
Somit sind die Werte aller Variablen des Befehls im Computer abgespeichert. 
- Wenn der Computer bei der Ausführung des Befehls in der gerade auszuführenden Anweisung einen Variablennamen sieht, 
geht er in die entsprechende Zeile der Tabelle, liest den Wert ab und ersetzt den Variablennamen durch diesen Wert. 
Danach kann der Computer die Anweisung mit diesem konkreten Wert ausführen. 
'''

'''
===============================================================================
Kapitel 3.3 Übertragung von Variablenwerten zwischen Befehlen
===============================================================================
'''

''' Beispiel 3.7: Kreis '''
#from gturtle import *
#
#def vieleck(anzahl_ecken, seite):
#    repeat anzahl_ecken:
#        forward(seite)
#        right(360/anzahl_ecken)
#
#def kreis(umfang):
#    vieleck(36, umfang/36)
#
#makeTurtle()
#hideTurtle()
#kreis(720)

''' Erläuterung des Ablaufs mit den Wertetabellen
Desktop-Aufteilung
- Links: Programm im Debugmodus zeichnen
- Rechts: Tabellen in OneNote im angedockten Fenster zeichnen 
(Durch das Andocken kann der - nicht benötigte Debuggerteil - unter OneNote verschoben werden.)
'''

''' Beispiel 3.8: Vieleck '''

''' Modularer Aufbau:
Die Figur besteht ist wie folgt aufgebaut:
- Die Figur besteht aus Quadrate mit unterschiedlichen Grössen und Farben --> Befehl Quadrat
- Die Figur besteht auf Fenstern bestehend aus 4 Quadraten in unterschiedliche Grössen und Farben --> Befehl Fenster
- Das Mosaik lässt sich über Fenster unterschiedlicher Grösse und Farbe zeichnen
'''

#from gturtle import *
#
#def quadrat(seite, farbe):
#    setPenColor(farbe)
#    repeat 4:
#        forward(seite)
#        right(90)
#
## Zeichne ein Fenster bestehend aus 2x2 Teilen in der Farbe <farbe>.
## Das Fenster wird von der Fenstermitte her gezeichnet. 
## Der Parameter <seite> gibt die Seitenlänge eines Teilfensters an.
#def fenster(seite, farbe):
#    repeat 4:
#        quadrat(seite, farbe)
#        right(90)
#
## Zeichne ein Mosaik bestehend in der Farbe <farbe1>, 
## welches links/oben und rechts/unten in der Farbe <farbe2> weiter unterteilt ist
#def mosaik(seite, farbe1, farbe2):
#    # Zeichne äusseres Fenster in <farbe1>
#    fenster(2*seite, farbe1)
#    forward(seite)
#    left(90)
#    forward(seite)
#    fenster(seite, farbe2)
#    backward(seite)
#    right(90)
#    backward(2*seite)
#    right(90)
#    forward(seite)
#    fenster(seite, farbe2)
#
#makeTurtle()
#hideTurtle()
#mosaik(100, "blue", "red")


''' Aufgabe 3.12: Reihe (Bitte lösen) '''


''' Aufgabe 3.13: Gitter (Bitte lösen) '''


''' Aufgabe 3.15: Schach (Bitte lösen) '''


''' Was wir gelernt haben:
- Im Körper eines Befehls können Sie die Variablenwerte des Befehls (d.h. des Hauptprogramms) an Variablen anderer Befehle (d. h. der Unterprogramme) weitergeben. 
Sie können aus den Variablenwerten auch neue Werte berechnen und die Resultate an die Variablen anderer Befehle in der Rolle von Unterprogrammen weitergeben. 
- Den Umgang mit den Werten und ihre Speicherung kann man mithilfe von Tabellen gut veranschaulichen. 
Bei jedem Befehlsaufruf entsteht eine Tabelle mit dem Befehlsnamen und die einzelnen Zeilen der Tabelle sind nach den Parametern des Befehls benannt. Nach der Ausführung des Befehls wird die Tabelle gelöscht. 
'''


'''
===============================================================================
Kapitel 3.4 Speicherinhalte ändern
===============================================================================
'''

'''
- Wir haben Variablen (Parameter) so verwendet, dass wir einmal - beim Aufruf - einen Wert gesetzt haben.
(Wir haben beim Aufruf eines Befehls den Wert in die Tabellen eingesetzt, aber nie verändert.
- Der Wert einer Variablen lässt sich aber während der Befehlsausführung verändern.
'''

''' Beispiel 3.9 '''
#from gturtle import *
#
#def spirale(seite):
#    forward(seite)
#    left(90)
#    forward(seite+5)    # erhöhe Seite um 5
#    left(90)
#    forward(seite+10)    # erhöhe Seite um 10
#    left(90)
#    forward(seite+15)    # erhöhe Seite um 15
#    left(90)
#    # erhöhe, bewege und drehe 46 weitere Mal
#    # forward(seite+245)
#    # left(90)
#    
#makeTurtle()
#hideTurtle()
#spirale(10)


''' Bemerkung:
- Wir können keine repeat-Anweisung verwenden, weil beim Befehl forward(seite+<Zahl>) immer eine andere Zahl steht.
- Hätten wir einen Befehl, um die Seite jeweis um 5 zu erhöhen, dann würde es klappen
'''

#def spirale(seite):
#    repeat 50:
#        forward(seite)
#        left(90)
#        # erhöhe den Wert von seite um 5


''' Bemerkung:
Den Wert erhöhen:
    seite += 5
'''

#from gturtle import *
#
#def spirale(seite):
#    repeat 50:
#        forward(seite)
#        left(90)
#        seite += 5
#        
#makeTurtle()
#hideTurtle()
#spirale(10)


''' Aufgabe 3.17: Spirale (Bitte lösen) '''


''' Neue Konzepte und Begriffe
- Eine Variable ist ein Speicherplatz mit einem Namen. Im Speicherplatz kann genau ein Wert gespeichert werden. Diesen Wert nennen wir den aktuellen Wert der Variablen. Der Name «Variable» betont, dass sich der Wert im Speicherplatz während der Ausführung des Programms ändern darf. Der Wert kann also variieren. 
- Sie ändern den Wert einer Variablen, indem Sie mit einen Zahlenwert hinzuzählen. Mit x += add erhöhen Sie den Wert der Variablen x um den Wert der Variablen add. 
- Mit -= können Sie einen Zahlenwert vom Wert der Variablen abziehen. 
- Mit der Anweisung *= wird der Wert der Variablen mit dem darauffolgenden Zahlenwert multipliziert. 
- Mit /= wird der Wert der Variablen durch den folgenden Zahlenwert dividiert. 
- So können Sie den Wert der Variablen x mit x *= 2 verdoppeln und und mit x /= 2 halbieren. 
'''


''' Aufgabe 3.21: Spirale von aussen nach innen (Bitte lösen) '''


''' Aufgabe 3.22: Sechseeckige Spirale von innen nach aussen (Bitte lösen) '''


''' Beispiel 3.10 '''

''' Zeittabellen
- Für jeden Durchgang durch eine Schleife eine Spalte
- Die Zeittabelle ist ein Hilfsittel um sich vorstellen zu können, was beim Ausführen des Programms im Speicher des Computers passiert.
'''

#from gturtle import *
#
#def kreis(umfang):
#    repeat 36:
#        forward(umfang / 36)
#        right(10)
#        
#def muschel(anzahl, umfang):
#    repeat anzahl:
#        kreis(umfang)
#        umfang *= 1.2
#
#makeTurtle()
#hideTurtle()
#muschel(5, 500)


''' Beispiel 3.11 (Quadratzahlen ausgeben) '''

''' 
- Variablen nicht nur dazu verwendet werden, um Figuren unterschiedliche gross zu zeichnen.
- Sondern beispielsweise auch zum Berechnen von Quadratzahlen.
'''

#def schreib_quadrate(x):
#    repeat 10:
#        print(x*x)
#        x += 1
#
#schreib_quadrate(3)


''' Aufgabe 3.29: Quadratzahlen ausgeben (Bitte lösen) '''


''' Aufgabe 3.30: Reiskörner auf Schachbrett (Bitte lösen) '''


''' Was wir gelernt haben:
- Variablen sind Speicherplätze mit einem Namen. 
- Jede Variable hat zu jedem Zeitpunkt genau einen Wert.
- Der Computer kann diesen Wert während der Ausführung eines Programms ändern, indem er auf dem entsprechenden Speicherplatz einen neuen Wert abspeichert. 
Dabei wird der alte Wert der Variablen überschrieben und vom Computer vergessen. 

'''


'''
===============================================================================
Kapitel 3.5 Zeittabellen für die Übertragung von Variablenwerten
===============================================================================
'''

'''
- Was passiert, wenn ein Programm den Wert einer Variablen an ein Unterprogramm übergibt?
- Kann ein Unterprogramm den Wert einer Variablen im Hauptprogramm verändern.
'''

''' Beispiel 3.12 '''

''' Tabellen zeichnen
- Zuerst ohne Zeittabelle
- Dann mit Zeittabelle und den Positionen A und B
- Dann mit print-Befehlen arbeiten
'''

#from gturtle import *
#
#def quadrat(seite):
#    repeat 4:
#        forward(seite)
#        right(90)
#
#def quadrat_muster(laenge):
#    repeat 50:
#        quadrat(laenge)
#        laenge += 3
#        
#makeTurtle()
#hideTurtle()
#quadrat_muster(30)



''' Aufgabe 3.31: Dreiecksmuster (Bitte lösen) '''



''' Beispiel 3.13 '''

'''
Wie entwickelen sich die Werte von seite und differenz bei jedem Schleifendurchgang?
- Überlege im Kopf und schreibe auf
- Überprüfe mit einer passenden print-Anweisung
'''
#from gturtle import *
#
#def spirale(n, seite, differenz):
#    repeat n:
#        forward(seite)
#        right(60)
#        seite += differenz
#        differenz += 1
# 
#makeTurtle()
#hideTurtle()
#spirale(20, 10, 1)


''' Was wir gelernt haben:
- Variablen sind Namen für Speicherplätze. 
- Wir dürfen unter einem Variablennamen unterschiedliche Werte abspeichern, diese Werte verwenden und nach Bedarf auch ändern. 
- Wenn wir die Änderung der Werte während der Ausführung des Programms beobachten wollen, erstellen wir für uns eine Zeit-Tabelle. 
Dazu müssen wir zunächst bestimmen, wo wir im Programm (nach der Ausführung welcher Zeile) die Variablenwerte beobachten wollen. 
- Ein Hauptprogramm kann beim Aufruf eines Unterprogramms die Werte von eigenen Variablen an die Variablen des Unterprogramms übergeben. 
- Ein Programm oder ein Befehl darf eine beliebige Anzahl von Variablen verwenden, deren Werte sich während der Ausführung des Programms verändern. 
Sogar der Zuwachs in der Anweisung variable += Zuwachs darf eine Variable sein, deren Wert sich ändert.
'''

'''
===============================================================================
Kapitel 3.6 Variablen, die keine Parameter sind
===============================================================================
'''

'''
Bisher:
- Variablen haben wir im Befehlsnamen als Parameter aufgeführt.
Neu:
- Variablen können an beliebiger Stelle definiert werden.
'''

''' Beispiel 3.14 '''

#def rechne(x, y):
#    summe = x + y
#    print(summe)
#
#rechne(3,11)

''' Tabellen mit Variablen zeichnen
'''

''' Neue Konzepte und Begriffe
- variable = Wert oder allgemein variable = Ausdruck
Wenn die Variable auf der linken Seite noch nicht im Programm vorhanden ist, dann wird eine neue Variable definiert und benannt. Allgemein weisst dieser Variablen einen Wert zu.
- Bei der Verwendung von variable = Wert musst du den Namen der Variable nicht im Voraus bei der Definition des Befehls in Klammern angeben.
Wenn du innerhalb des Programms einer neuen (vorher nicht definierten) Variablen einen neuen Wert zuweist, 
betrachtet der Computer diese Variable automatisch als eine Variable des Programms und fügt diese in die Tabelle des Programms ein
'''


''' Aufgabe 3.35: Rechne 2x^2-3x+1 (Diskussion) '''



''' Beispiel 3.15 
Summe aller natürlichen Zahlen von 1 bis n.

Wie würdest dieses Aufgabe von Hand lösen?
x           1  2  3  4  5  6  ...
summe   0   1  3  6 10 15 21  ...

Pseudocode:
x startet bei 1
summe hat den Wert 0

x läuft von 1 bis 100:
    summe jeweils um x erhöhen
summe ausgeben
'''

#summe = 0
#x = 1
#repeat 100:
#    summe += x
#    x += 1
#print(summe)



''' Aufgabe 3.36: Addition (Diskussion) '''
#def addition(x, y, s):
#    s = x + y
#    print(s)
#
#addition(3, 11, 0)

''' Fragen
- Berechnet addition(x,y,s) genau wie rechne(x,y) immer die Summe x+y?
- Spielt es eine Rolle, was für einen Wert wir für s beim Aufruf von addition() mitgeben?
- Welchen der zwei Befehle rechne() oder addition() würdest du bevorzugen?
'''

''' Aufgabe 3.37: Summe der ersten 10 Kubikzahlen (Bitte lösen) '''


''' Aufgabe 3.38: Summe der Reiskörner auf dem Schachbrett (Bitte lösen)'''




''' Was wir gelernt haben:
Wir haben zwei Möglichkeiten kennen gelernt, Variablen in Programmen einzuführen. 
- Die erste Möglichkeit ist, die Variablen als Parameter hinter def und dem Befehlsnamen in Klammern aufzulisten. 
- Die zweite Möglichkeit ist, in einer beliebigen Programmzeile variable = Ausdruck zu schreiben. In diesem Ausdruck dürfen auch wiederum Variablen vorkommen, aber nur solche, die 
bereits definiert worden sind und somit einen Wert besitzen. 
'''


'''
===============================================================================
Kapitel 3.7 Werte bei der Ausführung eingeben
===============================================================================
'''

''' Einleitung
Bisher: Befehle mit konkreten Variablenwerte aufrufen, z. B. vieleck(10).
Neu: Die konkreten Werte werden vom Programm abgefragt.
'''

''' Beispiel 3.15 '''
#from gturtle import *
#
#def vieleck(n, seite):
#    repeat n:
#        forward(seite)
#        right(360/n)
# 
#def zeichne_vieleck():
#    anzahl = input("Wie viele Seiten möchtest du?")
#    umfang = input("Wie gross soll der Umfang sein")
#    vieleck(anzahl, umfang/anzahl)
#
#makeTurtle()
#hideTurtle()
#zeichne_vieleck()


''' Neue Konzepte und Begriffe
- x = input(Fragetext)
Bei Ausführen erscheint ein kleines Fenster mit dem Fragetext. Die Eingabe des Benutzers wird in die Variable x geschrieben.
Gibt man 5 ein, dann ist das identisch zu
    x = 5
- Der Befehl input wandelt Zahlen in den passenden Datentyp um. Also eine ganze Zahl wird zu einer ganzen Zahl, mit der ich rechnen kann.
Ein Text wird zu einem Text.
'''

''' Beispiel 3.16 '''
#name = input("Wie ist dein Name?")
#print("Hallo", name)



''' Aufgabe 3.40: 10x10 Wörter (Bitte lösen) '''



''' Aufgabe 3.42: Quadrat auf Kreisbahn (Bitte lösen) '''

# Mögliche Lösung
#from gturtle import *
#
#def quadrat(seite, farbe):
#    setPenColor(farbe)
#    repeat 4:
#        forward(seite)
#        right(90)
#
#def zeichne_quadrat(seite, zeit):
#    quadrat(seite, "black")
#    delay(zeit)
#    quadrat(seite, "white")
#    
#def umlauf():
#    repeat 360:
#        zeichne_quadrat(100, 10)
#        forward(1)
#        left(1)
#
#makeTurtle()
#hideTurtle()
#anzahl_umlaeufe = input("Wie viele Umläufe soll das Quadrat machen?")
#repeat anzahl_umlaeufe:
#    umlauf()


''' Was wir gelernt haben:
Werte von Variablen können nicht nur beim Schreiben eines Programmes angegeben werden.
Mit input(Frage) kann der Benutzer den Wert einer Variablen eingeben, während das Programm bereits läuft. 
'''

'''
===============================================================================
Selbsttest
===============================================================================
'''

''' Kapitel 3-Selbsttest-Konzepte und Begriffe '''

''' Kapitel 3-Selbsttest-Aufgabe 3.1 (Turm aus Quadraten) '''

''' Kapitel 3-Selbsttest-Aufgabe 3.3 (Zahlensumme) '''

''' Kapitel 3-Selbsttest-Aufgabe 3.4 (Ueberraschung) '''
