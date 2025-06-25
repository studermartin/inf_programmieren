
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
# def f(x):
#     return 3

# print(f(1))
# print(f(10))

''' 
Entspricht der Funktion f(x)=3
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

# Fläche berechnen und ...?
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
''' Hinweis:
- Alle Elemente einer Liste mit einer repeat-Schleife durchgehen und falls gefunden, mit return den Index zurückgeben.
'''


''' Aufgabe 7.4: Ist sortiert (bitte lösen) '''
''' Hinweis: 
- Eine Liste ist sortiert, wenn alle nebeneinander stehenden Werte sortiert sind.
'''


''' Aufgabe 7.5: Binäre Suche (bitte lösen) '''
''' Hinweis: 
- Der Algorithmus für die binäre Suche kann einfach aus Beispiel 5.4 übernommen werden. Man muss die Algorithus "nur" in eine Funktion verpacken.
'''


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
- makeGPanel: Erstellt eine Zeichenfläche mit den angegebenen Koordinaten
- title: Setzt den Titel der Zeichenfläche
- drawGrid: Zeichnet ein Gitter auf der Zeichenfläche
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
# title("sin(x)")
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
''' Aufgabe 7.12 Programm (Gruppendiskussion, Abgabe im Teams) '''
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

''' Konzepte und Befehle (Bitte im Teams lösen) '''

''' Aufgaben (Bitte im Teams lösen) '''


