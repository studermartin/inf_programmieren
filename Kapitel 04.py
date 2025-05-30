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




''' Aufgabe 4.1: (Diskussion)'''


''' Aufgabe 4.2: (Diskussion) '''



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


''' Visualisierung mittels Flussdiagrammen '''


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


''' Aufgabe 4.3: Quadrat (Bitte lösen)'''


''' Aufgabe 4.4: if-Bedingung ohne Variable (lassen wir weg) '''


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


''' Aufgabe 4.7: Gleiche Wirkung (Bitte lösen) '''

''' Erläuterung: 
- if, if-else und if-elif-else Befehle lassen sich verschachteln wie das zweite Beispiel zeigt.
'''


''' Aufgabe 4.8: Sicheres Vieleck (Bitte lösen) '''



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


''' Aufgabe 4.9: (Diskussion) '''


''' Aufgabe 4.9: (Weglassen) '''



''' Neue Konzepte und Begriffe
- Mit der strukturierten Anweisung if-elif-else kann man ein Programm in beliebig viele Wege verzweigen.
  Unter if und elif listet man alle Bedingungen auf, die man betrachtet.
  Wenn keiner dieser Bedingungen zutrifft, wird der else-Zweig ausgeführt.
  Somit ermöglicht es if-elif-else genau eine der aufgelisteten Möglichkeiten zu wählen.
- Man kann in if-elif-else auch Bedingungen stellen, die sich nicht gegenseitig ausschliessen, d.h. mehrere Bedingungen können gleichzeitig erfüllt sein.
  In diesem Fall wird der Zweig ausgeführt, der der ersten erfüllten Bedingung entspricht.
  Für die Verständlichkeit ist es von Vorteil, in if-elif-else nur Bedingungen zu stellen, die sich gegenseitig ausschliessen.
'''

''' Aufgabe 4.11: Bilder abhängig von Eingabe zeichnen (Bitte lösen) '''


''' Aufgabe 4.14: Quiz (Bitte lösen) '''


''' Aufgabe 4.13: Lineare Gleichungen (Bitte lösen) '''


''' Aufgabe 4.12: Lösung von quadratischen Gleichungen (Weglassen) '''


'''
===============================================================================
Unterkapitel 4.2 Logische Operatoren
===============================================================================
''' 

''' Einführung
if-Anweisungen führen den Körper (die Befehle) durch, falls die Bedingung wahr ist.
Manchmal möchte man die Befehle durchführen, 
- wenn die Bedingung nicht erfüllt ist.
- wenn mehrere Bedingungen erfüllt sind.
 '''

''' Negation 
Beispiel: 
                    Bedingung             Neg. der Bed. (mit Not)     Negation der Bed. (ohne not)
Umgangssprachlich   "x ist 10"            "x ist nicht gleich 10"     "x ist ungleich 10"   
Python              x != 0                not (x == 10)               x != 10
                                          
Umgangssprachlich   x ist grösser als 10  x ist nicht grösser als 10  x ist gleich oder kleiner 10
Python              x > 10                not x > 10                  x <= 10


Die Negation einer Behauptung ist komplementär zu dieser Behauptung

Wahrheitstabelle:
    Umgangssprachlich
    Bedingung         Negation der Bedingung
    Wahr/Gültig       Falsch/Ungültig
    Falsch/Ungültig   Wahr/Gültig

    Python          
    a           not a
    True        False
    False       True
'''


''' Aufgabe 4.15: (Diskussion) '''

''' Aufgabe 4.16: (Bitte im Teams lösen) '''

''' Aufgabe 4.17: (Bitte im Teams lösen) '''

''' Aufgabe 4.18: (Diskussion) '''

#def test_1(x):
#    if x == 0:
#        print ("x ist gleich null.")
#    else:
#        print ("x ist nicht gleich null.")
#
#def test_2(x):
#    if x != 0:
#        print ("x ist nicht gleich null.")
#    else:
#        print ("x ist gleich null.")
#
#def test_3(x):
#    if not x == 0:
#        print ("x ist nicht gleich null.")
#    else:
#        print ("x ist gleich null.")
#
#def test(x):
#    test_1(x)
#    test_2(x)
#    test_3(x)
#
#test(0)
#test(2)

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


''' Aufgabe 4.19: Nichtteiler von 24 (Bitte lösen) '''



'''
-------------------------------------------------------------------------------
Thema: Wahrheitstabellen
-------------------------------------------------------------------------------
'''

'''
Konkrete Beispiele:
Aussage 1: Die Sonne scheint.
Aussage 2: Es regnet.

Situationen (Zeichne):
- Wolken, aber kein Regen.
- Wolken, mit Regeln
- Sonne, ohne Regen
- Sonne mit Regen

Bild:
Zeichne vier Bilder mit
- Sonne in der Mitte oder Wolken
- Regen (ein paar senkrechte Striche) oder kein Regen (keine senkrechte Striche)


Für welche Situationen gilt:
- "Die Sonne scheint." und "Es regnet."
- "Die Sonne scheint." oder "Es regnet."
'''

''' Wahrheitstabellen für die Operatoren and und or zeichnen 
    Ergänzen mit einem Beispiel: x>0, x<10
    Wann gilt: x>0 und x<10?
    Wann gilt: x>0 oder x<10?
'''


''' (siehe Buch) '''


''' Aufgabe 4.20: (Bitte lösen, keine Abgabe im Teams) '''


''' Aufgabe 4.21: (Bitte lösen, keine Abgabe im Teams) '''



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
-   if <Bedingung1> and not <Bedingung2>:
    Mit and und not können Sie zwei Bedingungen so verknüpfen, dass
    der Körper der if-Anweisung nur dann ausgeführt wird, wenn die erste
    Bedingung erfüllt ist, aber nicht die zweite (not Bedingung 2).
'''


''' Aufgabe 4.22: (Diskussion) '''

#from gturtle import *
#
#def rechteck(a, b):
#    if a >= 10 and b >= 10 and a + b <= 500:
#        repeat 2:
#            forward(a)
#            right(90)
#            forward(b)
#            right(90)
#    else:
#        print("Mindestens eine Seite ist zu kurz " + 
#            "oder beide zusammen sind zu lang.")
#
#makeTurtle()
#hideTurtle()
#
#rechteck(10, 20)
#rechteck(10, 5)


''' Aufgabe 4.24: Teiler 24 und 54 (Bitte lösen, bitte im Teams abgeben) '''


''' Aufgabe 4.25: Teiler von 7 aber nicht 3 (Bitte lösen, bitte im Teams abgeben) '''


''' Aufgabe 4.27: Begrüssung (Bitte lösen, bitte im Teams abgeben) '''


'''
===============================================================================
Unterkapitel 4.3 Schleifen abbrechen
===============================================================================
''' 

''' 
Mit repeat: ohne Angabe einer Anzahl kann eine unendliche Wiederholung realisiert werden.
Mit einer if- und break-Anweisung in Kombination im Körper der Schleife kann diese abgebrochen wird,
sobald eine gegebene Aufgabe erledigt ist.
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


''' Flussdiagramm zeichnen '''


''' Aufgabe 4.28: (Diskussion) '''


''' Weglassen: Aufgabe 4.29 '''


''' Neue Konzepte und Begriffe
-   break
    Die Anweisung break sorgt in einer Schleife dafür, dass die Ausführung der Schleife sofort abgebrochen wird.
    Mit break springt der Computer bei der Ausführung des Programms in die erste Zeile nach dem Körper der Schleife - gerade so, als hätte er bereits alle Wiederholungen der Schleife abgeschlossen.
'''


''' Aufgabe 4.30: (Diskussion) '''



''' Aufgabe 4.31: (Bitte lösen, Abgabe im Teams) '''


''' Umsetzung der repeat-Anweisung mit Zähler
'''

# from gturtle import *

# makeTurtle()
# repeat 6:
#   forward(lOO)
#   right(60)

# Umsetzung 1

# from gturtle import *

# makeTurtl()
# i_schleife = 0
# repeat:
#   if i schleife < 6:
#     forward(lOO)
#     right(60)
#     i_schleife += 1
#   else:
#     break

# Umsetzung 2

# from gturtle import *

# makeTurtle()
# i_schleife = 0
# if i_schleife < 6:
#   forward(lOO)
#   right (60)
#   i_schleife += 1
#   goto 5


''' Aufgabe 4.32: (Bitte lösen, Abgabe im Teams) '''


'''
Wir möchten, dass der Computer für uns den kleinsten echten Teiler einer Zahl grösser als 1 sucht. 
Der Teiler muss grösser als 1 sein. Wir beginnen bei 2 und probieren alle möglichen Teiler aus.
Wir brechen die Schleife ab, sobald wir einen Teiler gefunden haben. 
Ist dies kein echter Teiler, so ist der kleinste gefundene Teiler die Zahl selbst und diese somit eine Primzahl.

--> Das Programm aus dem Text entwickeln

'''

''' Beispiel 4.8: kleinster echter Teiler '''
#def kleinster_teiler(zahl):
#    teiler = 2
#    repeat zahl - 1:
#        if zahl % teiler == 0:
#            break
#        teiler += 1
#    print("Der kleinste Teiler von", zahl, "ist", teiler)
#    
#    if teiler == zahl:
#        print("Die Zahl", zahl, "ist eine Primzahl.")
#
#kleinster_teiler(4)
#kleinster_teiler(5)


'''
Flussdiagramm (wie im Buch 2-spaltig zeichnen)
'''



''' Aufgabe 4.33: (Bitte lösen, Abgabe im Teams) '''



''' Aufgabe 4.34: (Bitte lösen, Abgabe im Teams) '''



''' Aufgabe 4.35: (Diskussion) '''



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


''' Aufgabe 4.36: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.37: (Bitte lösen, Quiz im Teams) '''


''' Aufgabe 4.38: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.39: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.40: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.41: (Bitte lösen, Abgabe im Teams, Weglassen) '''


''' Aufgabe 4.42: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.43: (Bitte lösen, Abgabe im Teams, Weglassen) '''


''' Aufgabe 4.44: (Bitte lösen, Abgabe im Teams) '''


''' Aufgabe 4.45: (Bitte lösen, Abgabe im Teams, Weglassen) '''


''' Aufgabe 4.46: (Bitte lösen, Abgabe im Teams) '''


'''
===============================================================================
Selbsttest
===============================================================================
'''

''' Kapitel 4-Selbsttest-Konzepte und Begriffe '''


''' Kapitel 4-Selbsttest-Aufgabe 4.1 (Berechnung mit Zahlen) '''


''' Kapitel 4-Selbsttest-Aufgabe 4.2 (Zahlenvergleich) '''


''' Kapitel 4-Selbsttest-Aufgabe 4.3 (Dreiecksfigur) '''


''' Kapitel 4-Selbsttest-Aufgabe 4.4 (Primzahlen) '''


''' Kapitel 4-Selbsttest-Aufgabe 4.5 (Zahlensumme) '''