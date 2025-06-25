
#===============================================================================
#Kapitel 5 Datenstrukturen
#===============================================================================


'''
-   Jede Variable speichert nur einen Wert.
    Beispiel: Alle Noten im Fach Informatik einlesen und den Durchschnitt berechnen?

Lernziele:
-   In Python mit Datenstrukturen beliebig grosse Sammlungen von Daten speichern und bearbeiten.
    Die Idee ist, eine Datenstruktur mit einem einzigen Namen für eine ganze Folge von beliebigen Werten zu verwenden.
    Indexieren der Variablen mit natürlichen Zahlen, so dass eine Folge von Variablen mit unterschiedlichen Indizes entsteht.
    Beispiel: note[1], note[2], note[3] usw.
    (Sie kennen das Konzept aus der Mathematik: x1, x2, x3, ..., xn
'''



'''
===============================================================================
Unterkapitel 5.1 Das Konzept der Listen
===============================================================================
''' 

''' Einführung '''

## Liste mit Werten erstellen
#daten = [ 5, 0, -2, 3, 51, 8, 13, -100, -100, 1]
#print(daten)
#print(type(daten))
#
## Element an mit Index 4 aus der Liste lesen
#print(daten[4]) # Die Indexe starten mit 0, nicht mit 1
#x = daten[4]
#
## Wert -10 an Index 8 in die Liste schreiben
#daten[8] = -10
#print(daten)



''' Beispiel 5.1: Summe aller Wert in einer Liste '''
#daten = [ 4, 2, -6, 17, 5, 12]
#i = 0
#summe = 0
#repeat 6:
#    wert = daten[i]
#    summe += wert
#    i += 1
#print(summe)



''' Anweisung len einsetzen '''



''' Aufgabe 5.3: Diskussion '''
''' Eine Liste mit dem Namen neue_daten hat 150 Elemente.
a) Was ist der Index des letzten Elements?
b) Was die Indizes der beiden mittleren Elemente?
c) Was bewirken die folgenden drei Zeilen?
neue_daten[1] = neue_daten[0]
neue_daten[2] = neue_daten[1]
neue_daten[3] = neue_daten[2]
d) Wie würdet ihr Vorgehen, um allen Elementen von neue_daten den Wert 0 zuzuweisen, 
ohne die Anweisung neue_daten = [0]*150 zu verwenden?
'''


''' Aufgabe 5.4 (alle Werte in einer Liste um 2 erhöhen): Lösen Sie die Aufgabe '''

''' Aufgabe 5.5 (alle geraden Werte in einer Liste halbieren): Lösen Sie die Aufgabe '''

''' Aufgabe 5.6 (Durchschnitt der Werte in der Liste): Lösen Sie die Aufgabe '''



''' Beispiel 5.2: Minimales Element in einer Liste '''

'''
    Demo an der Tafel: wie geht man von Hand durch?
    1. Beim ersten Element anfangen und alle Elemente durchgehen (Muster 1)
    2. Sich das bisher kleinste Element merken. Finde ich ein kleineres als das bisher kleinste, tausche ich aus. (Muster 2)
    
'''

#zahlen = [ -3, 1, 7, 2, -6, 4, 8, 12, 0, 7]
#minimum = zahlen[0]
#index = 0
#repeat len(zahlen)-1:
#    if zahlen[index] < minimum:
#        minimum = zahlen[index]
#    index += 1
#print("Der kleinste Wert der Liste ist", minimum)
#print("Die ganze Liste ist", zahlen)


''' Neue Konzepte und Begriffe
-   daten = [ x.1, x.2, ... , x.n-1]
    Erstellt eine Liste mit dem Namen daten, die n Elemente enthält.
    Auf das Element x.i an der Stelle i der eingegebenen Folge kann jederzeit mit daten[i] zugegriffen werden.
    Wir nennen daten[0], daten[1], ..., daten[n-1] die Elemente der Liste daten.
    Die Zahl i nennen wir den Index des Elements daten[i].
    Die Werte können sowohl Daten als auch Texte sein.
    Wir können daten[i] hierbei wie eine einzelne Variable verwenden und ihren Wert mit den =, +=, -= ändern.
-   daten = [x] * n
    Erstellt eine Liste mit dem Namen daten, die n Elemente mit dem Wert x enthalten.
-   daten[i] = x
    Weist dem Element an der Stelle i den Wert x zu.
-   x = daten[i]
    Weist der Variablen x den Wert an der Stelle i der Liste daten zu.
-   len(daten)
    Gibt die Anzahl Elemente in der Liste zurück.
-   print(daten)
    Gibt die gesamte Folge von Werten im Ausgabefenster aus, die in der Liste daten gespeichert ist.
    
Python 2 Language Reference
- The if-statement: https://docs.python.org/2/reference/expressions.html#subscriptions
- Boolean operations: https://docs.python.org/2/reference/expressions.html#booleans
'''



''' Aufgabe 5.7 (Index und Wert des minimalen Elements in einer Liste): Lösen Sie die Aufgabe '''


''' Aufgabe 5.9 (Anzahl 7 in einer Liste zählen): Lösen Sie die Aufgabe '''
''' An der Tafel in Pseudocode entwickeln:
        1. 
		    Der Reihe nach alle Elemente in der Liste durchgehen:
			    Falls eine 7 gefudnen wurde, dann den Zähler um 1 erhöhen.
		    Zähler ausgeben.
        2.
            Zähler auf 0 setzen.
'''



''' Beispiel 5.3: Bubble-Sort '''

''' Sortieralgorithmen 
Schritt 1: Einschränkung der Operationen
- Zwei Zahlen an je zwei Indexstellen vergleichen
- Zwei Zahlen an je zwei Indexstellen austauschen
(3 Karten offen hinlegen)

Schritt 2: Karten geschlossen hinlegen
Ein SuS kann 
    - Fragen stellen: Ist die Karte an der Stelle 0 kleiner als die Karte an der Stelle 2
    - Operationen auslösen: Vertausche die Karten an der STelle 0 und 2
Ein Sus führt die Operationen (bei verdeckten Karten) durch.
'''


''' Hinweis: https://de.wikipedia.org/wiki/Bubblesort '''
#x = [ 1, 7, 2, 20, 105, 6, -5, 0, 18, 200]
#repeat len(x):
#    index = 0
#    repeat len(x)-1:
#        if x[index] > x[index+1]:
#            z = x[index]
#            x[index] = x[index+1]
#            x[index+1] = z
#        index += 1
#print(x)



''' Aufgabe 5.10a): Diskussion '''



''' Aufgabe 5.11 (Bubblesort: Hilfsvariable, Begründung): Bitte lösen '''

''' Aufgabe 5.12 (Bubblesort: Abbruch bei sortierter Liste): Bitte lösen '''

''' Aufgabe 5.13 (Skalarprodukt): Bitte lösen '''



''' Beispiel 5.4: Binäre Suche '''

#y = input("Welchen Wert möchte Sie suchen?")
#x = [-20, -17, -13, -13, 2, 5, 7, 7, 9, 10]
#links = 0
#rechts = len(x)-1
#gefunden = False
#while not gefunden and links <= rechts:
#    mitte = (links+rechts) // 2
#    if y == x[mitte]:
#        gefunden=True
#    elif y < x[mitte]:
#        rechts = mitte -1
#    else:
#        links = mitte + 1
#if gefunden:
#    print(y,"ist an der Stelle", mitte)
#else:
#    print(y,"kommt in x nicht vor")



''' Hinweis: Darstellung an der Wandtafel '''



''' Aufgabe 5.14 (Binäre Suche: Nachvollziehen): Bitte lösen '''

''' Aufgabe 5.15 (Binäre Suche: ohne Boolesche Variable): Bitte lösen '''


'''
===============================================================================
Unterkapitel 5.2 Wie der Computer mit Listen arbeitet
===============================================================================
''' 


''' Umsetzung von Listen im Speicher
-   Liste x der Länge 10000:
            -------------------------------
    x -->   | x[0] | x[1] | ... | x[9999] | 
            -------------------------------
    Variable x "zeigt" auf das erste Element: x enthält die Adresse (im Speicher) des ersten Elements.
    Die Elemente liegen direkt nacheinander im Speicher.
-   Direkter Zugriff/Random access x[i]:
    Adresse von x nehmen und i Speicherplätze nach rechts schauen, also Adresse x+i.
'''


''' Copy by Reference: Ausgabe folgendes Programmes? '''

#a = [1, 2, 3, 4, 5]
#b = a
#print(a)
#b[2] = -9
#print(a)



''' Aufgabe 5.16: Liste kopieren (Bitte lösen, Abgabe im Teams) '''
''' Hinweis: die gegebene Aufgabe zuerst zeichnen; dann eine Lösung erarbeiten. '''


''' Details
- The Python Standard Library (https://docs.python.org/2/library/index.html) führt definiert die Standard-Bibliothek, z. B. den Datentyp Listen.
- Der Datentyp Listen (https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange) hat in Version 2 von Python keine copy-Methode.
  Mittels Slicing (https://docs.python.org/2/reference/expressions.html#slicings) kann einfach eine Kopie erstellt werden.
'''

#a = [1, 2, 3, 4, 5]
#b = a[:]
#print(a)
#b[2] = -9
#print(a)



''' Beispiel 5.5: Insert-Operation in Listen '''
#x = [3, 4, 1, -2, 6, 7]

''' Zahl 5 an Index 1 einfügen:
            ------------------------------
    x -->   | 3 | 5 | 4 | 1 | -2 | 6 | 7 |
            ------------------------------
Umsetzung im Speicher?
'''


''' Aufgabe 5.17 (Einfügen in Liste): Bitte lösen '''



''' Neue Konzepte und Begriffe
-   Die Elemente einer Liste befinden sich in unserem Modell im Speicher des Computers direkt nebeneinander, was einen sehr effizienten Zugriff ermöglicht.
    Das hat aber den Nachteil, dass das Einfügen und Entfernen von Elementen einen grossen Aufwand bedeutet.
-   daten2 = daten1
    Diese Zuweisung kopiert nicht die Element der Liste daten1 in eine Liste daten2, sondern gibt der ursprünglichen Liste daten1 den zusätzlichen Namen daten2.
    Dies hat zur Folge das Änderungen an daten1 auch automatisch daten2 betreffen.
    Um eine echte Kopie von daten1 zu erstellen muss eine neue Liste daten2 erstellt werden, in welche alle Elemente von daten1 explizit kopiert werden.
'''



'''
===============================================================================
Unterkapitel 5.3 Dynamische Datenstrukturen
===============================================================================
''' 


''' 
-   Listen wurden bisher mit einer festen Grösse erzeugt.
-   Listen in Python können aber erweitert werden (--> dynamische Datenstrukturen)
'''

''' Beispiel 5.6: Listen-Methode append '''
#primzahlen = [2, 3]
#print(primzahlen)
#primzahlen.append(5)
#print(primzahlen)



''' Aufgabe 5.18 (Primzahlen einer Liste anfügen): (Bitte in Teams abgeben) '''



''' Beispiel 5.7: Listen-Methode pop '''
#primzahlen = [2, 3, 5]
#print(primzahlen)
#primzahlen.pop()
#print(primzahlen)



''' Neue Konzepte und Begriffe
-   daten = []
    Erstellt eine leere Liste mit dem Namen daten.
-   daten.append(wert)
    Am Ende der Liste wird das neue Element wert angehängt.
    Somit wird die Liste um ein Element verlängert.
-   daten.pop()
    Entfernt das letzte Element aus der Liste. 
    Dadurch wird die Liste um ein Element kürzer.
'''


''' Beispiel 5.8: wird übersprungen '''
''' Exkursion: In der Praxis würde man nicht separate Listen wählen, sondern z. B. Dictionaries verwenden  '''
#teilnehmende = []
#anzahl = input("Wie viele Teilnehmende gibt es?")
#repeat anzahl:
#    vorname = input("Vorname:")
#    km = input("Km:")
#    alter = input("Alter:")
#    teilnahme = { "Vorname": vorname, "Km": km, "Alter:": alter}
#    teilnehmende.append(teilnahme)
#print(teilnehmende)


''' Beispiel 5.9: Liste von Quadratzahlen '''
#quadratzahlen = []
#x = 1
#repeat 10:
#    quadratzahlen.append(x*x)
#    x += 1
#print(quadratzahlen)


''' Aufgabe 5.22 (Liste der Quadratzahlen kleiner 1000): Bitte lösen '''



''' Aufgabe 5.19 (Fibonacci-Zahlen): Bitte lösen '''
#fibonacci = [1,1]



''' Aufgabe 5.25 (echte Teiler): Bitte lösen '''


''' Was wir gelernt haben
- Eine Liste speichert eine beliebige Anzahl Werte.
- Die Anzahl Element muss im Voraus nicht bekannt sein. 
Es können jederzeit neue Werte hinzugefügt werden.
- In Python erzeugst du eine Liste mit Folge von Werten in eckigen Klammern.
Die Klammern können auch leer sein, womit eine leere Liste erzeugt wird.
Danach fügst du mit append() weitere Zahlenwert hinzu.

- Liste können neben Zahlen auch andere Datentypen wie beispielsweise Texte enthalten.
- Eine Zahl oder ein Text darf in der Liste mehrfach vorkommen.
'''



'''
===============================================================================
Unterkapitel 5.4 Die Elemente einer Liste durchlaufen
===============================================================================
''' 


''' IU
- Wir haben bisher die Elemente einer Liste mit einer Schleife und einem Zähler durchlaufen.

zahlen = [ -3, 1, 7 ]
i = 0
repeat len(zahlen):
    zahl = zahlen[i]
    print(zahl)
    i += 1

- Weil man sehr oft die Elemente einer Liste durchläuft gibt es dafür eine eigene Art von Schleife.
Die for-Schleife.

zahlen = [ -3, 1, 7 ]
for zahl in zahlen:
    print(zahl)

'''

''' Beispiel 5.10 '''

#zahlen = [ -3, 1, 7, 2, -6, 4, 8, 12, 0, 7 ]
#minimum = zahlen[0]
#for zahl in zahlen:
#    if zahl < minimum:
#        minimum = zahl
#print("Der kleinste Wert der Liste ist", minimum)
#print("Die ganze Liste ist", zahlen)


''' Aufgabe 5.29 (Diskussion) 
Vergleiche Beispiel 5.10 mit Beispiel 5.2.
'''

#zahlen = [ -3, 1, 7, 2, -6, 4, 8, 12, 0, 7]
#minimum = zahlen[0]
#index = 0
#repeat len(zahlen)-1:
#    if zahlen[index] < minimum:
#        minimum = zahlen[index]
#    index += 1
#print("Der kleinste Wert der Liste ist", minimum)
#print("Die ganze Liste ist", zahlen)


''' Neue Konzepte und Begriffe
- for Wert in Liste:
Bei einer for-Schleife gebst du einen Variablennamen und eine Liste an.
Python setzt dann der Reihe nach jedes Element aus der Liste in die Variable ein und führt den Schleifenkörper aus.
- Beispiel:
    for wert in [2, 3, 5]
Python setzt als erstes den Wert 2 ein, dann den Wert 3 und zum Schluss den Wert 5.
'''


''' Aufgabe 5.30 (Diskussion) '''
#from gturtle import *
#
#makeTurtle()
#seiten = [80, 50, 80, 50]
#for s in seiten:
#    forward(s)
#    right(90)


''' Beispiel 5.11 '''
''' 
Mit der for-Schleife kann ich alle Elemente durchgehen, ohne eine Variablen für den Index zu nutzen.
Ich habe damit dann natürlich auch keine Möglichkeit, den Index zu nutzen, z. B. für eine Ausgabe.
Natürlich kann ich zusätzlich eine Variable für den Index einführen.
'''

#primzahlen = [2, 3, 5, 7, 11, 13, 17, 19]
#index = 0
#for zahl in primzahlen:
#    print(index, "tes Element:", zahl)
#    index += 1
    
''' Aufgabe 5.31 (Diskussion) '''
''' Modifizieren wir das Beispiel so, dass wir eine while-Schleife benutzen '''
#primzahlen = [2, 3, 5, 7, 11, 13, 17, 19]
#index = 0
#while index < len(primzahlen):
#    print(index, "tes Element:", primzahlen[index])
#    index += 1



''' ---- Listen aufteilen --- '''

''' Mit einer for-Schleife kann man eine Liste in zwei Listen aufteilen.
Beispielsweise alle geraden Zahlen in eine Liste, alle ungeraden in eine andere Liste. '''

''' Beispiel 5.12 '''
#zahlen = [2, 6, 7, 9, 12, 4, 5, 11]
#gerade = []
#ungerade = []
#for zahl in zahlen:
#    if zahl%2==0:
#        gerade.append(zahl)
#    else:
#        ungerade.append(zahl)
#print("Gerade Zahlen:", gerade)
#print("Ungerade Zahlen:", ungerade)



''' Aufgabe 5.33: Laufteilnehmende unterteilen (Bitte lösen) '''


''' Aufgabe 5.34: Indexe der geraden Zahlen (Bitte lösen) '''


''' ---- Die Werte einer Liste auf einen Wert reduzieren --- '''

''' Beispiel 5.13 '''
#liste = [1, 2, 3, 4, 5]
#summe = 0
#for zahl in liste:
#    summe += zahl
#print(summe)


''' Aufgabe 5.36: Summe der Quadratzahlen von 1 bis 100 (Bitte lösen) '''


''' Aufgabe 5.38: Durchschnitt (Bitte lösen) '''


''' ---- Eine Liste bearbeiten --- '''

''' Weitere typische Listenoperationen:
- Filtern von Listen: nur gewisse Elemente in der Liste lassen
'''

''' Beispiel 5.14 '''
#x = [1, 2, 3, 7, 2, 3, 4, 1, 3]
#gefilterte_liste = []
#print(x)
#for element in x:
#    if element != 3:
#        gefilterte_liste.append(element)
#x = gefilterte_liste
#print(x)


''' Aufgabe 5.39: Liste ohne Zahlen im Bereich 2-4 (inklusive) (Bitte lösen) '''


''' Aufgabe 5.40 '''

# satz = "Der Himmel ist blau"
# liste_von_woertern = satz.split()
# print(liste_von_woertern)


''' Was wir gelernt haben
- Die Elemente einer Liste mit einer for-Schleife durchlaufen.
- Bei dr Ausführung einer for-Schleife setzt der Computer im (i+1)ten Durchlauf 
den Wert des Elements an der Stelle i in die Variable der for-Schleife ein.
Somit kann man im (i+1)-ten Durchlauf mit dem Element an der Stelle i arbeiten.
- Häufige Aufgaben die mit for-Schleifen gelöst werden können: 
Berechnen von Summen, des Minimums oder Maximums von Elementen, das Aufteilen oder das Filtern von von Listen.
'''


