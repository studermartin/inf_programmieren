'''
===============================================================================
Kapitel 4 Verzweigung und bedingte Schleifen
===============================================================================
'''

'''
Verzweigungen und bedingte Schleifen
- Ein Programm soll abhängig von Variablenwerten Entscheidungen treffen.
  Analogie: Es regnet, also nehme ich den Regenschirm mit.

Lernziele:
- Anweisungen kennenlernen, mit denen ein Programm anhand von aktuellen Variablenwerten Entscheidungen trifft, 
  sodass eine bestimmte Tätigkeiten aus vorhandenen Möglichkeiten ausgewählt und ausgeführt wird.
- Verzweigungen mit dem Konzept der Schleifen kombinieren.
  Beispiel: Tätigkeit ausführen, bis der Wert einer Variable eine gewisse Grösse erreicht hat.
'''



'''
===============================================================================
Unterkapitel 4.1 Verzweigungen mit if-Anweisungen
===============================================================================
''' 


''' Beispiel 4.1: Lisa '''

#name = input("Wie ist dein Name?")
#if name=="Lisa":                        # if-Anweisung mit der Bedingung; Ist der Inhalt der Variablen name gleich "Lisa"
#    print("Hallo Lisa")                 # Eingerückt der Körper der if-Anweisung
#    print("Schön, dass du da bist")     # Der Körper der if-Anweisung wird nur ausgeführt, wenn die Bedingung den Wert True hat


''' Visualisierung mittels Flussdiagrammen '''




''' Aufgabe 4.1: Lösen Sie die Aufgabe '''


''' Aufgabe 4.2: Lösen Sie die Aufgabe '''



''' Neue Konzepte und Begriffe
- Datentyp boolean:
  Eine Variable die nur die Werte True oder False annimmt, nennen wir eine Boolesche Variable.
  Bei der if-Anweisung werte der Computer die Bedingung aus und erhält als Resultat True oder False.
  Python kürzt den Datentyp mit bool ab.
    
Python 2 Language Reference
- The if-statement: https://docs.python.org/2/reference/compound_stmts.html#the-if-statement
- Boolean operations: https://docs.python.org/2/reference/expressions.html#booleans
'''

''' Hinweis 1: Typ eines Ausdruckes '''
#print(type(1==4))

''' Hinweis 2: Implizite Umwandlungen '''
#x=7
#if x:
#    print("Ja") 



''' Beispiel 4.2: Vielecke'''

#from gturtle import *
#
#def vieleck(anzahl, seite):
#    repeat anzahl:
#        forward(seite)
#        right(360/anzahl)
#        
#def zeichne_vieleck(anzahl, seite):
#    if anzahl>2:
#        vieleck(anzahl, seite)
#    print("Ich bin fertig.")
#
#makeTurtle()
#zeichne_vieleck(2, 300)
#zeichne_vieleck(6, 70)


''' Neue Konzepte und Begriffe
- if <Bedingung>:
  Nach if geben Sie in der Bedingung an, was der Computer überprüfen soll, ob es wahr(True) oder falsch(False) ist.
  Beispielsweise kann man Werte auf beiden Seiten mit ==(gleich), >(grösser), >=(grösser gleich), <(kleiner), <=(kleiner gleich) und !=(ungleich) vergleichen.
  Die beiden Seiten des Vergleichs können arithmetische Ausdrücke sein, zum Beispiel (x+1)*y > 2*x/y+7.
- Wenn die Bedingung erfüllt ist, führt der Computer den Körper der if-Anweisung (den nach rechts eingerückten Programmteil) aus.
  Wenn die Bedingung nicht erfüllt ist, setzt der Computer die Ausführungen nach dem Körper der if-Anweisung fort.
    
Python 2 Language Reference
- The if-statement: https://docs.python.org/2/reference/compound_stmts.html#the-if-statement
- Boolean operations: https://docs.python.org/2/reference/expressions.html#booleans
'''



''' Beispiel 4.3: Lisa und Unbekannte '''

#name = input("Wie ist dein Name?")
#if name=="Lisa":                        
#    print("Hallo Lisa!")
#if name !="Lisa":
#    print("Hallo Unbekannte!")
#print("Schön, dass du da bist.")     


''' Visualisierung mittels Flussdiagrammen '''


#name = input("Wie ist dein Name?")
#if name=="Lisa":                        
#    print("Hallo Lisa!")
#else:
#    print("Hallo Unbekannte!")
#print("Schön, dass du da bist.")     


''' Visualisierung mittels Flussdiagrammen '''


''' Aufgabe 4.5: Diskussion '''



''' Neue Konzepte und Begriffe
- Die strukturierte Anweisung if-else ermöglicht uns, ein Programm in zwei Zweige zu unterteilen und danach wieder zusammenzuführen.
  In einem Zweig liegt der Programmteil, der ausgeführt wird, wenn die Bedingung erfüllt (True) ist.
  Der andere Zweig wird ausgeführt, wenn die Bedingung nicht erfüllt (False) ist.
'''



''' Aufgabe 4.7: Bitte lösen '''



''' Aufgabe 4.8: Bitte lösen '''



''' Beispiel 4.4 Mehrere if vs. if-elsif-... '''

# Variante 1
#
#from gturtle import *
#
#def quadrat(seite):
#    repeat 4:
#        forward(seite)
#        left(90)
#
#def quad(seite, farbzahl):
#    setPenColor("black")
#    if farbzahl == 1:
#        setPenColor("yellow")
#    if farbzahl == 2:
#        setPenColor("red")
#    if farbzahl == 3:
#        setPenColor("blue")
#    if farbzahl == 4:
#        setPenColor("green")
#    quadrat(seite)
#    
#makeTurtle()
#quad(40, 4)


# Variante 2

#from gturtle import *
#
#def quadrat(seite):
#    repeat 4:
#        forward(seite)
#        left(90)
#
#def quad(seite, farbzahl):
#    setPenColor("black")
#    if farbzahl == 1:
#        setPenColor("yellow")
#    elif farbzahl == 2:
#        setPenColor("red")
#    elif farbzahl == 3:
#        setPenColor("blue")
#    elif farbzahl == 4:
#        setPenColor("green")
#    quadrat(seite)
#    
#makeTurtle()
#quad(40, 4)



''' Visualisierung mittels Flussdiagrammen '''



''' Neue Konzepte und Begriffe
- Mit der strukturierten Anweisung if-elif-else kann man ein Programm in beliebig viele Wege verzweigen.
  Unter if und elif listet man alle Bedingungen auf, die man betrachtet.
  Wenn keiner dieser Bedingungen zutrifft, wird der else-Zweig ausgeführt.
  Somit ermöglicht es if-elif-else genau eine der aufgelisteten Möglichkeiten zu wählen.
- Man kann in if-elif-else auch Bedingungen stellen, die sich nicht gegenseitig ausschliessen, d.h. mehrere Bedingungen können gleichzeitig erfüllt sein.
  In diesem Fall wird der Zweig ausgeführt, der der ersten erfüllten Bedingung entspricht.
  Für die Verständlichkeit ist es von Vorteil, in if-elif-else nur Bedingungen zu stellen, die sich gegenseitig ausschliessen.
'''



''' Aufgabe 4.12: Lösung von quadratischen Gleichungen (Bitte lösen) '''



'''
===============================================================================
Unterkapitel 4.2 Logische Operatoren
===============================================================================
''' 



''' Bitte lesen: Seite 76, Logische Operatoren '''
''' Aufgabe 4.15: (Bitte lösen) '''
''' Aufgabe 4.16: (Bitte lösen) '''
''' Aufgabe 4.17: (Bitte lösen) '''
''' Aufgabe 4.18: (Bitte lösen) '''



''' Beispiel 4.5: not '''
#x = 1
#repeat 30:
#    if not x % 7 == 0:
#        print(x)
#    x += 1



''' Neue Konzepte und Begriffe
-   Mit not <Bedingung> berechnet man in Python die Negation der Bedingung.
    Somit ist not <Bedingung> genau dann erfüllt (True), wenn die Bedingung nicht erfüllt ist (False).
    Beispielsweise wird bei 
        if not x > 0: 
    der Körper von if immer dann ausgeführt, wenn x nicht grösser als null ist.
'''


'''
-------------------------------------------------------------------------------
Thema: Wahrheitstabellen
-------------------------------------------------------------------------------
'''

''' Wahrheitstabellen für die Operatoren and und or zeichnen '''



''' Aufgabe 4.20: (Bitte lösen) '''



'''
-------------------------------------------------------------------------------
Thema: Bedingungen verknüpfen
-------------------------------------------------------------------------------
'''

''' Beispiel 4.6: Bedingungen vernüpfen '''

#antwort = input("Nennen einen Kanton, in dem man italienisch spricht.")
#if antwort == "Tessin" or antwort == "Graubünden":
#    print("Richtig!")
#else:
#    print("Falsch!")



''' Neue Konzepte und Begriffe
-   if <Bedingung1> or <Bedingung2>:
    Wenn du in einer if-Anweisung zwei Bedingungen mit or (oder) verknüpfst, dann führt den Computer den Körper aus, wenn mindestens eine der beiden Bedingungen erfüllt ist.
    Es dürfen auch beide Bedingungen erfüllt sein.
-   if <Bedingung1> and <Bedingung2>:
    Wenn du in einer if-Anweisung zwei Bedingungen mit and (und) verknüpfst, dann führt den Computer den Körper nur aus, beiden Bedingungen erfüllt sind.
'''


''' Aufgabe 4.22: (Bitte lösen) '''
''' Aufgabe 4.25: (Bitte lösen) '''



'''
===============================================================================
Unterkapitel 4.3 Schleifen abbrechen
===============================================================================
''' 


''' Beispiel 4.7: Spirale mit break '''
#from gturtle import *
#
#def spirale(seite, add, max_seite):
#    repeat:
#        if seite > max_seite:
#            break
#        forward(seite)
#        right(90)
#        seite += add
#    print("Ich bin fertig.")
#    
#makeTurtle()
#spirale(20, 5, 200)



''' Aufgabe 4.28: (Diskussion) '''



''' Neue Konzepte und Begriffe
-   break
    Die Anweisung break sorgt in einer Schleife dafür, dass die Ausführung der Schleife sofort abgebrochen wird.
    Mit break springt der Computer bei der Ausführung des Programms in die erste Zeile nach dem Körper der Schleife - gerade so, als hätte er bereits alle Wiederholungen der Schleife abgeschlossen.
'''


''' Aufgabe 4.30: (Diskussion) '''




''' Aufgabe 4.31: (Bitte lösen) '''



''' Beispiel 4.8: kleinster echter Teiler '''
#def kleinster_teiler(zahl):
#    teiler = 2
#    repeat zahl - 1:
#        if zahl % teiler == 0:
#            break
#        teiler += 1
#    print("Der kleinste Teiler von", zahl, "ist", teiler)
#    
#    if (teiler == zahl):
#        print("Die Zahl", zahl, "ist eine Primzahl.")
#
#kleinster_teiler(4)
#kleinster_teiler(5)



''' Aufgabe 4.33: (Bitte lösen) '''



'''
===============================================================================
Unterkapitel 4.4 While-Schleifen
===============================================================================
''' 

'''
Einführung:
-   Die Anweisung repeat in Kombination mit if und break bricht eine Schleife ab, sobald eine bestimmte Bedinung erfüllt ist.
    Dafür kann die Schleifen-Anweisung while verwendet werden.
'''

''' Beispiel 4.9: Repeat-break mit While ersetzen '''
''' - Beispiel 4.7 nehmen und umbauen '''

#from gturtle import *
#
#def spirale(seite, add, max_seite):
#    while seite <= max_seite:
#        forward(seite)
#        right(90)
#        seite += add
#    print("Ich bin fertig.")
#    
#makeTurtle()
#spirale(20, 20, 200)


''' Flussdiagramm zeichnen '''


''' Aufgabe 4.36: (Bitte lösen) '''

''' Aufgabe 4.38: (Bitte lösen) '''

''' Aufgabe 4.42: (Bitte lösen) '''

''' Aufgabe 4.44: (Bitte lösen) '''

''' Aufgabe 4.46: (Bitte lösen) '''