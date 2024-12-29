
#===============================================================================
# Kapitel 7 Funktionen definieren und aufrufen
#===============================================================================


'''
Aus der Mathematik kennen wir Funktionen.
Beispiel:
    f(x)=2x+3
Der Name der Funktion ist f.
Wir haben bereits Funktionen geschrieben:
  def f(x):
    print(2*x+3)
Wir können zwar das Resultat ausgeben, aber nicht direkt mit dem Result weiterrechnen.
Das wollen wir hier tun.



Lernziele:
- Funktionen definieren und aufrufen.
'''


'''
===============================================================================
Unterkapitel 7.1 Funktionen definieren
===============================================================================
''' 


'''
-------------------------------------------------------------------------------
Definition einer Funktion
-------------------------------------------------------------------------------
''' 

''' Beispiel 7.1: Lineare Funktion '''
# def f(x):
#    return 2*x+3

# y = f(4) * 5

''' Neue Regeln für den Aufbau von arithmetischen Ausdrücken
A6: Ein Funktionsaufruf f (Ausdruck) ist ein Ausdruck, dessen Wert der Rückgabewert der Funktion ist.


Funktionen sind wie normale Befehle.
Unterschied: sie geben mit Hilfe des Schlüsselwortes return einen Wert zurück.
'''


''' Aufgabe 7.1: Konstante Funktion (Diskussion) '''
# def q(x):
#     return 3

# print(q(1))
# print(q(10))

''' 
Entspricht der Funktion q(x)=3
'''

'''
-------------------------------------------------------------------------------
Funktionen mit mehreren Parametern
-------------------------------------------------------------------------------
''' 

''' Beispiel 7.2: Fläche eines Rechtecks '''
# def flaeche_rechteck(a, b):
#    return a*b

''' Verwendung der Funktion '''

# Fläche berechnen und speichern
# flaeche = flaeche_rechteck(3, 20)

# Fläche berechnen und ausgeben
# print(flaeche_rechteck(3, 20))

# Fläche berechnen und für einen Vergleich nutzen
# if flaeche_rechteck(3, 20) > 100:
#    print("Fläche > 100")

# Fläche berechnen und ...?recht
# flaeche_rechteck(3, 20)



''' Aufgabe 7.2: Umfang eines Rechtecks (bitte lösen) '''


''' Neue Konzepte und Begriffe
Eine Funktion funk wird wie folgt definiert:
  def funk(parameter1, paramenter2, paramenter3, ...)
    # Körper der Funktion
    return <Ausdruck>

Der Körper einer Funktion kann - wie ein Befehl - aus mehreren Zeilen bestehen.
Ein Aufruf
  y = funk(a1, a2, a3, ...)
liefert der Befehl return im Funktionskörper den Wert der Funktion zurück.
'''


''' Aufgabe 7.3: Index von (bitte lösen) '''


''' Aufgabe 7.4: Ist sortiert (bitte lösen) '''


''' Aufgabe 7.5: Binäre Suche (bitte lösen) '''


''' Was wir gelernt haben
Funktionen sind eine Verallgemeinerung von Befehlen.
Funktionen liefern zusätzlich - mit der return-Anweisung - einen Wert zurück.
'''


'''
===============================================================================
Unterkapitel 7.2 Funktionen aufrufen
===============================================================================
''' 

'''
-------------------------------------------------------------------------------
Einfacher Funktionsaufruf
-------------------------------------------------------------------------------
''' 

''' Beispiel 7.3: Einfacher Funktionsaufruf '''

# def f(x):
#    return 2*x+3

# print ( f(19) )

''' Ausdrucksbaum
    ^ 41
    |
  f(x)
    ^ 19
    | 
  19
'''


''' Aufgabe 7.6: Verdoppeln zeichnen (bitte lösen) '''


'''
-------------------------------------------------------------------------------
Funktionsaufruf als Teil eines grösseren Ausdrucks
-------------------------------------------------------------------------------
'''

''' Beispiel 7.4: Transformation von Funktion '''
# def f(x):
#    return 2*x+3

# def f_transformiert(x, skalierung, verschiebung):
#    return verschiebung + f(x) * skalierung


''' Ausdrucksbaum für den Ausdruck "verschiebung + f(x) * skalierung" in der return-Anweisung
            ^ 
            |
            +
        ^       ^
      /           \\
verschiebung      *
                ^   ^
              /       \\
            f(x)  skalierung
              ^   
              |
              x
'''

''' Aufgabe 7.7: Ausdrucksbaum f_transformiert (Diskussion) '''
# print(f_transformiert(10,2,100))



'''
-------------------------------------------------------------------------------
Funktionsaufruf als Argument eines Funktionsaufrufs
-------------------------------------------------------------------------------
'''

''' Beispiel 7.5:  '''
''' 
Paramenterwerte einer Funktion sind auch Ausdrücke, können also auch Funktionsaufrufe nutzen.
'''

# def f(x):
#    return 2*x+3

# print(16 - f(2+19)/3)

''' Ausdrucksbaum für den Parameter der print-Funktion 

                ^ 
                | 1
                -
            ^       ^
      16 /           \\ 15
        16            /
                    ^   ^
               45 /       \\ 3
                f(x)      3
                  ^ 
                  | 21
                  +
                ^   ^
             2 /      \\ 19
              2       19
'''


'''
-------------------------------------------------------------------------------
Funktionen mit mehreren Argumenten
-------------------------------------------------------------------------------
'''

''' Beispiel 7.6:  '''
''' 
Ausdrucksbaum für den Ausdruck rechteck_flaeche(3,20) > 100 aus Beispiel 7.2
                ^ 
                | false
                >
            ^       ^
      60  /           \\ 100
rechteck_flaeche(a,b)   100   
       ^   ^
    3 /      \\ 20
      3       20
'''



''' Aufgabe 7.8: Funktion ohne Parameter (Bitte lesen) '''


''' Aufgabe 7.9: PI-Berechnung (Bitte lösen) '''



''' Was wir gelernt haben
Funktionen können in Ausdrücken verwendet werden.
Die Funktionen werden aufgerufen, wenn der Ausdruck ausgewertet wird.
'''


'''
===============================================================================
Unterkapitel 7.3 Eingebaute Funktionen verwenden
===============================================================================
''' 



''' Neue Konzepte und Begriffe
Bereits geschriebene Funktionen kann man in Modulen zusammenfassen und wiederverwenden.
Wir kennen bereits ein Modul: gturtle
Um Funktionen zu nutzen braucht es folgende Anweisungen:
  from module import *
Importiert alle Definitionen aus einem Modul.
  from module import <Funktion>
Importiert nur eine Funktion.
'''


'''
-------------------------------------------------------------------------------
Eine Sinus-Kurve zeichnen
-------------------------------------------------------------------------------
''' 

# from math import *

# print("sin(0):", sin(0))
# print("cos(0):", cos(0))
# print("tan(0):", tan(0))


''' Beispiel 7.7: sinus-Kurve zeichnen '''
'''
Variante 1: mit gturtle
Variante 2: mit gpanel
- Punkte, Striche und Kreise kann man an vordefinierten Koordinaten zeichnen
- Koordinatensystem (ungleich Pixel)

Die Funktionen zur Zeichenfläche erstellen sind:
- makeGPanel:
- title
- drawGrid

'''


# from math import * 
# from gpanel import * 

# # Zeichenfläche erstellen
# minX = -pi
# maxX = pi
# minY = -1
# maxY = 1
# horizTicks = 4
# vertTicks = 2

# makeGPanel(minX, maxX, minY, maxY)
# title("sin (x)")
# drawGrid(minX, maxX, minY, maxY, horizTicks, vertTicks, "grey")

# # Sinus zeichnen
# segmente = 8
# x = minX 
# altX = x
# setColor("red")
# lineWidth(2)

# repeat segmente + 1:
#     y = sin(x) 
#     if altX != x: 
#         line(altX, altY, x, y)
#     altX = x
#     altY = y
#     x = x + (maxX -minX) / segmente



''' Aufgabe 7.10 Verdoppelung der Anzahl Segmente (Diskussion) '''
'''
Frage:
- Verdopple die Anzahl der Segmente (ändere den Wert, der der Variablen segmente zugewiesen wird). 
Sieht die Kurve damit eher wie eine Sinus-Kurve aus? Warum ist das so?
'''

''' Aufgabe 7.11 Halbierung der Anzahl Segmente (Diskussion) '''
'''
- Halbiere die Anzahl der Segmente (ändere den Wert, der der Variablen segmente zugewiesen wird). 
Wie sieht die Kurve nun aus?

'''
''' Aufgabe 7.12 Programm (Gruppendiskussion) '''
'''
Fragen:
- Wenn wir segmente Segmente zeichnen wollen, warum wird die repeat-Schleife (segmente + I)-mal ausgeführt?
- Was ist der Zweck von altX und altY? 
- Und warum benötigen wir die if-Anweisung?
- Das Programm in Beispiel 7.7 zeichnet eine Kurve der Funktion sin(x) Sie können sin(x) durch beliebige andere Funktionen ersetzen. Versuchen Sie es mit cos(x) , tan(x) oder auch sin(x*x).
'''


'''
-------------------------------------------------------------------------------
Die Turtle überwachen
-------------------------------------------------------------------------------
''' 

''' Weglassen '''


'''
-------------------------------------------------------------------------------
Quadratische Gleichungen
-------------------------------------------------------------------------------
''' 

''' Beispiel 7.9 '''

''' 
Wir möchten eine Funktion schreiben, die die Lösung einer quadratischen Gleichung zurückgibt:
  ax^2+bx+c=0
Wir kennen die abc-Formel:
  D = b^2-4ac
  x_1/2 = (-b+-sqrt(D))/2a
'''

# def loese_quadratische_gleichung(a, b, c):
  # Diskriminante D gemäss b^2-4ac berechnen

  # Falls D>0:
  #   Zwei Lösungen: x_1/2 = (-b+-sqrt(D))/2a

  # Falls D==0:
  #   Eine Lösung: x=-b/2a

  # Falls D<0:
  #   Keine Lösung
  
# def loese_quadratische_gleichung(a, b, c):
#   d = b*b-4*a*c
#   if d>0:
#     x1 = (-b+sqrt(d))/(2*a)
#     x2 = (-b-sqrt(d))/(2*a)
#   elif d==0:
#     x = -b/(2*a)
#   else:
#     pass

# def loese_quadratische_gleichung(a, b, c):
#   d = b*b-4*a*c
#   if d>0:
#     x1 = (-b+sqrt(d))/(2*a)
#     x2 = (-b-sqrt(d))/(2*a)
#     return [x1, x2]
#   elif d==0:
#     x = -b/(2*a)
#     return [x]
#   else:
#     return []

# print(loese_quadratische_gleichung(1,0,0))
# print(loese_quadratische_gleichung(2,5,3))


''' Aufgabe 7.13 Polynom berechnen (Bitte lösen) '''



''' Was wir gelernt haben
Python bietet viele eingebaute Funktionen, die sich einfach verwenden lassen.
Diese Funktionen befinden sich in Modulen. 
Um die in den Modulen definierten Funktionen zu verwenden, muss die import-Anweisung verwendet werden.
'''


'''
===============================================================================
Unterkapitel 7.4 Zusammenfassung
===============================================================================
''' 



# ----- =====- ---- - 






''' Aufgabe 6.2: Gleichwertige Ausdrücke (Diskussion) '''
#print(3 - 2 + 1)
#print(3 - (2 + 1))
#print((3 -2) + 1)

''' Aufgabe 6.3: Gleichwertige Ausdrücke (Diskussion) '''
#print(- - 2)
#print(2)
#print(+ 2)


'''
-------------------------------------------------------------------------------
Logische Ausdrücke
-------------------------------------------------------------------------------
''' 

''' Einleitung 
- Arithmetische Ausdrücke sind nur eine Form von Ausdrücken.
'''

''' Aufgabe 6.4 (Diskussion) 
Die Bedingung einer if-Anweisung oder einer while-Schleife sind ebenfalls ein Ausdruck.
- Welche möglichen Werte erhält man bei der Auswertung?
- Was sind die Typen dieser Werte?
'''
#if x<0:
#    print("x ist negativ")
    
#i = 10
#while i>0:
#    print(i)
#    i = i - 1

''' 
Typ: Logische Ausdrücke (boolesche Audrücke)
Werte: True, False
'''

''' Beispiel 6.2 '''
#def reagiere_auf_temperatur(zu_kalt, zu_heiss):
#    if zu_kalt:
#        print("Wir sollten heizen")
#    if zu_heiss:
#        print("Wir sollten die Kälteanlage einschalten")
#    if zu_heiss or zu_kalt:
#        print("Wir braucheh Energie :-(")
#    if (not zu_heiss) and (not zu_kalt):
#        print("Genau richtig!")
#    if zu_heiss and zu_kalt:
#        print("Das kann doch nicht sein...sind wir krank?")
#
#reagiere_auf_temperatur(True, False)


''' Regeln für den Aufbau von logischen Ausdrücken
L1: Logische Werte True und False sind logische Ausdrücke.
L2: Eine Boolesche Variable ist ein logischer Ausdruck.
- Beispiel: zu_heiss
L3: not, gefolgt von einem logischen Ausdruck, ist ein logischer Ausdruck
- Beispiel: not zu_heiss
L4: Ein logischer Ausdruck, gefolgt von einem logischen Operator (and oder or), 
gefolgt von einem logischen Ausdruck, ist wieder ein logischer Ausdruck
- Beispiel: zu_heiss and zu_kalt
L5: Ein logischer Ausdruck in Klammern ist ein logischer Ausdruck.
- Beispiel: (zu_heiss oder zu_kalt)

Beispiele:
- not True
'''


''' Aufgabe 6.5: gültige Logische Ausdrücke (bitte lösen) '''


''' Aufgabe 6.6: wahre logische Ausdrücke (bitte lösen) '''


''' Neue Konzepte und Begriffe
Logische Ausdrücke sind ähnlich wie arithmetische Ausdrücke aufgebaut. 
Statt mit Zahlen arbeitet man mit den logischen Werten True und False.
Die verwendeten Operatoren sind die binären and und or und der unäre Operator not.

Anders als die arithmetischen Operatoren stellt man die logischen Operatoren nicht mit Sonderzeichen (+, - usw.)
sondern mit einem Wort dar (and, or, not).
'''


'''
-------------------------------------------------------------------------------
Text-Ausdrücke
-------------------------------------------------------------------------------
''' 

''' Einleitung
Neben arithmetischen und logischen gibt es noch Text-Ausdrücke.
Wenn man einen Text-Ausdruck auswertet, erhält man einen Text.
'''

''' Beispiel 6.3 '''
#def zeichne_muster(laenge):
#    oben  = "*" + "v" * laenge + "*\n"
#    mitte = ">" + "o" * laenge + "<\n"
#    unten = "*" + "^" * laenge + "*\n"
#    print(oben + mitte + unten)
#    
#zeichne_muster(5)
    
''' Regeln für den Aufbau von Text-Ausdrücken
T1: Ein Text ist ein Text-Ausdrücke.
- Beispiel: "Hallo"
T2: Eine Variable, die einen Text speichert, ist ein Text-Ausdruck.
- Beispiel: name
T3: Ein Text-Ausdruck, gefolgt von einem +, gefolgt von einem Textausdruck, ist ein Text-Ausdruck
- Beispiel: "Hallo " + "Welt"
T4: Ein Text-Ausdruck, gefolgt von einem *, gefolgt von einer Zahl, ist ein Text-Ausdruck
- Beispiel: "Hallo" * 2
T5: Ein Text-Ausdruck in Klammern ist ein Text-Ausdruck.
- Beispiel: ("Hallo")
'''


''' Beispiele '''
#print("True or False")
#print("True" or "False")


''' Aufgabe 6.8: gültige Text-Ausdrücke (Bitte lösen) '''


''' Neue Konzepte und Begriffe
Neben den arithmetischen und logischen Ausdrücke gibt es auch Text-Ausdrücke, 
mit denen sich Texte zu komplexen Text-Ausdrücken kombiniert werden können:
- Der binäre Operator + kann zwei Texte zusammenhängen.
- Der binäre Operator * kombiniert einen Text mit einer Zahl, um den Text entsprechend oft zu wiederholen. 

Es kann verwirren, dass die Darstellung dieser zwei Operatoren (+ und *) genau die gleichen sind
wie die der arithmetischen Operatoren für die Addition und Multiplikation.
Je nach dem ob die Operanden Texte oder Zahlen sind, verhalten sich die Operatoren anders.
'''

''' Aufgabe 6.10: Gültige Ausdrücke mit + und * (Bitte lösen) '''



'''
-------------------------------------------------------------------------------
Ausdrücke im Allgemeine
-------------------------------------------------------------------------------
'''

''' Einleitung
Wir haben einige, aber noch nicht alle Regeln kennengelernt.
'''

''' Beispiel 6.4: Toleranz prüfen '''

#def nahe_ziel(x, ziel, toleranz):
#    if (x >= ziel-toleranz) and (x <= ziel+toleranz):
#        print("Die Position ist nahe am Ziel.")
#    else:
#        print("Ziel verfehlt.")
#
#nahe_ziel(3, 5, 1)

''' Erläuterung
Der Ausdruck 
    (x >= ziel-toleranz) and (x <= ziel+toleranz)
lässt sich mit keiner bekannten Regel erstellt. Es fehlen die Operatoren >= und <=.
Wir sprechen von relationalen Operatoren, Operatoren die zwei Werte miteinander vergleichen und als Ergebnis einen logischen Wert True oder False zurückgeben.

Mit relationalen Operatoren kann man also aus arithmetischen Ausdrücken einen logischen Ausdruck bauen:
R1: Ein arithmetischer Ausdruck, gefolgt von einem relationen Operator (<, <=, >, >=, ==, !=) gefolgt von einem arithmetischen Operator ergibt einen logischen Operator.
- Beispiel: alter < 21

Hinweis:
Eine Bedingung lässt sich oft unterschiedlich ausdrücken:
  a < 10
  10 > a

'''

''' Neue Konzepte und Begriffe
Beim Programmieren muss man ein zusätzliches Problem in Betracht ziehen, 
das wir hier nicht detailliert vorstellen.
Für Zahlen mit vielen Nachkommastellen arbeitet der Computer mit gerundeten Werten.
Dadurch erhält man als Resultat oft nur Näherungswerte. 
Dies kann jedoch dazu führen, dass man beim Vergleich von Zahlen falsche logische Werte erhält
'''

''' Aufgabe 6.11: äquivalente Ausdrücke mit relationalen Operatoren (Bitte lösen) '''


''' Mit den relationalen Operatoren kann man auch Texte oder logische Ausdrücke vergleichen
R2: Ein Text-Ausdruck, gefolgt von einem relationalen Vergleichs-Operator (==, !=, <, >), gefolgt von einem Text-Ausdruck ergibt einen logische Ausdruck.
- Beispiel: name = "Jim"
R3: Ein logischer Ausdruck, gefolgt von einem der relationalen Vergleichs-Operatoren == oder  !=, gefolgt von einem logischen Ausdruck ergibt einen logische Ausdruck.
- Beispiel: darf_auto_fahren = True
'''


''' Aufgabe 6.12: äquivalente Ausdrücke (Bitte lösen) '''

''' Neue Konzepte und Begriffe
Die relationalen Operatoren (z. B. <, <=, >, >=, ==, !=) vergleichen zwei Werte und produzieren entweder den Wert True oder False.

Die zwei Werte im Vergleich müssen vom gleichen Typ sein (beides Zahlen, beides logische Werte oder beides Texte).
'''



''' Aufgabe 6.13: Monte-Carlo-Methode (Bitte lösen) '''


'''
===============================================================================
Unterkapitel 6.2 Die Auswertung von Ausdrücken veranschaulichen
===============================================================================
''' 

'''
Um zu verstehen, wie der Computer einen Ausdruck auswertet, macht es Sinn, den Ausdruck in seine Bestandteile zu zerlegen. 
'''



'''
-------------------------------------------------------------------------------
Eine Addition
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.5 '''
''' Ausdruck 1 + 2 zeichnen 
- 1. Zerlegung
- 2. Auswertung
''' 

''' Neue Konzepte und Begriffe
In der Informatik besteht ein Baum aus sogenannten Knoten und Kanten.
Eine Kante als Linie verbindet zwei Knoten.

Einer der Knoten des Baumes wird als Wurzel gewählt.
Die Wurzel wird ganz oben gezeichnet.
Darunter wächst der Baum (visualisert durch Kanten) nach unten.

Ganz zuunterst sind die Knoten, die man Blätter nennt.
Aus den Blättern gehen keine Kanten mehr nach unten.

Alle Knoten - ausser den Blättern - werden innere Knoten genannt.
Wenn aus einem Knoten mehrere Kanten nach unten führen, sprechen wir von einer Verzweigung im Baum.
'''


'''
-------------------------------------------------------------------------------
Mehrere Operationen
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.5 '''
''' Ausdruck 5 + 2 -3 visualisieren
- Da der Ausdruck von links nach rechts ausgewerte wird, wird zuerst 5+2 gerechnet.
'''

''' Aufgabe 6.14 (Diskussion) '''


''' Aufgabe 6.15: Bäume '''


'''
-------------------------------------------------------------------------------
Unäre Operatoren
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.7 '''
''' Ausdruck 25 + -x visualisieren
- Unärer Operator -x hat nur eine Kante.
'''


''' Aufgabe 6.17: Zum Baum passender Ausdruck (Bitte lösen) '''


'''
-------------------------------------------------------------------------------
Punkt vor Strich
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.8 '''
''' Ausdruck 25 - k * k visualisieren
- Punkt vor Strich.
'''

'''
-------------------------------------------------------------------------------
"Grösser als" als eine Operation
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.9 '''
''' Ausdruck x + 2 > 15 visualisieren
- Punkt vor Strich vor Vergleich.
'''

''' Aufgabe 6.18: Zerlegung und Auswertung des Ausdrucks x + 3 > x - 3 (Bitte lösen) '''


'''
-------------------------------------------------------------------------------
Ausdrücke mit logischen Operatoren
-------------------------------------------------------------------------------
''' 

''' Beispiel 6.10 '''
''' Ausdruck not (True and (False or True)) visualisieren und auswerten.
- Punkt vor Strich vor Vergleich.
'''


''' Aufgabe 6.19: Zerlegung und Auswertung des Ausdrucks x<=maxi and x>=mini (Bitte lösen) '''

''' Aufgabe 6.21: Zerlegung und Auswertung es_regnet==True (Bitte lösen) '''

''' Was wir gelernt haben
Wir haben gelernt, Ausdrücke mit verschiedenen Operatoren 
(arithmetische: +, -, *, /; relationale: ==, !=, <, <=, >, >=; logische: and, or, not), 
mit Literalen (Zahlen, Textwerte und den Wahrheitswerten True und False) 
und mit Variablen (z. B. spalten, index) in Bäume zu zerlegen und auszuwerten.

Wir haben auch gelernt, das wir für bestimmte Aufgaben verschiedene äquivalente Ausdrücke verwenden kann.
'''
