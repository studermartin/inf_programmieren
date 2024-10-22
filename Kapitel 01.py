'''
===============================================================================
Kapitel 1 Die ersten Programme und Schleifen
===============================================================================
'''

'''
Programmiersprache: Eine einfache, klar definierte Sprache, die der Computer versteht, hier TigerJython, ein Dialog von Python.
Programmieren: Das Schreiben einer folge von Befehlen in einer Programmiersprache.
Befehle: Analog zu einer natürlichen Sprache besteht eine Programmiersprache aus Wörtern, hier Befehlen.
Programm: Ein grammatikalisch korrekter Text in einer Programmiersprache, die eine Tätigkeit beschreibt.

Lernziel: Wir schreiben erste einfache Programme.
'''



'''
===============================================================================
Unterkapitel 1.1 Zeichnen mit der Turtle 
===============================================================================
''' 


''' Beispiel 1.1 '''

#from gturtle import *
#        
#makeTurtle()
#forward(150)
#right(90)



''' Konzepte und Begriffe
Steuerung der Turtle:
- forward(<Anzahl Pixel>): Vorwärtsgehen. Mit forward(150) geht die Turtle 150 Pixel nach vorne.
- back(<Anzahl Pixel>): Rückwärtsgehen.
- left(<Winkel>): Nach links drehen. Mit left(120) dreht sich die Turtle um 120 Grad nach links.
- right(<Winkel>): Nach rechts drehen. Mit right(90) dreht sich die Turtle um 90 Grad nach recht.
- Eine Folge von Befehlen in einer Programmiersprache bezeichnen wir als Programm. 
  Beim Aufschreiben in TigerJython enthält jede Zeile genau einen Befehl.
  Die vier vorgestellten Befehle bestehen aus zwei Teilen. 
  Zuerst kommt der Befehlsname (forward, back, left, right), danach in Klammern der Parameterwert.
  Der Befehlsname bestimmt die Tätigkeit und der Parameter beschreibt den Umfang der Tätigkeit.
'''


''' Beispiel 1.2: Gleichseitiges Dreieck mit Seitenlänge 150 '''

#from gturtle import *
#
#makeTurtle()
#forward(150) 
#right(120) 
#forward(150) 
#right(120) 
#forward(150) 
#right(120) 



''' Aufgabe 1.1: Diskussion '''



''' Aufgabe 1.2: Rechteck der Grösse 200x100 (Lösen Sie die Aufgabe) '''



''' Konzepte und Begriffe
Mit Farben arbeiten:
- setPenColor(<Farbe>): Stiftfarbe angeben. Nach setPenColor("green") zeichnet die Turtle beispielsweise in Grün weiter.
  Farben in Englisch in Anführungszeichen: "yellow", "red", "green" usw.
- Ein Parameter muss nicht unbedingt eine Zahl sein. Ein Parameter ist ein Wert und kann wie beim Befehl setPenColor ein Text sein.
  Python erkennt Text daran, dass er in Anführungszeichen (" ") steht.
- setPenWidth(<Stiftbreite>): Festlegen der Stiftbreite. Die Stiftbreite wird in Pixel angegeben. 
  Mit setPenWidth(3) zeichnet der Stift 3 Pixel breit.
'''


''' Beispiel 1.3: Gleichseitiges Dreieck mit unterschiedlich farbigen Seiten '''

#from gturtle import *
#
#makeTurtle()
#setPenWidth(5)
#setPenColor("yellow")
#forward(100)
#left(120)
#setPenColor("red")
#forward(100)
#left(120)
#setPenColor("blue")
#forward(100)
#left(120)



'''
===============================================================================
Unterkapitel 1.2 Einfache Schleifen
===============================================================================
'''


''' Beispiel 1.4: Dreieck Zeichnen (Nutzung von Schleifen) '''

#from gturtle import *
#
#makeTurtle()
#forward(100)
#left(120)
#forward(100)
#left(120)
#forward(100)
#left(120)



''' Konzepte und Begriffe
- repeat <Anzahl>: repeat ist eine strukturierte Anweisung und diese Struktur wird als grammatische Regel angesehen.
  Nach der repeat Anweisung wird zuerst die Anzahl Wiederholungen angegeben, gefolgt von einem Doppelpunkt.
  In den nächsten Zeilen folgt nach rechts eingerückt ein Programm (eine Folge von Anweisungen).
  Die ganze Struktur nennen wir eine Schleife.
  Das eingerückte Programm nennen wir den Körper der Schleife.
  Der Computer erkennt das Ende des Körpers der Schleife dadurch, dass die nächste Anweisung nicht mehr eingerückt ist.
'''


''' Beispiel 1.5: Regelmässiges Sechseck zeichnen (Anwendung von Schleifen) '''

#from gturtle import *
#
#makeTurtle()
#repeat 6:
#    forward(100)
#    right(360 / 6)



''' Aufgabe 1.8: Regelmässige Vielecke (Lösen Sie die Aufgabe)
a) 11 Ecken, 50 Pixel Seitenlänge
'''



'''
--- Thema: Die Turtle bewegen ohne zu zeichnen ---
'''


''' Beispiel 1.6 '''

#from gturtle import *
#
#makeTurtle()
#repeat 25:
#    forward(5)
#    penUp()
#    forward(5)
#    penDown()



''' Aufgabe 1.9: Diskussion '''



''' Beispiel 1.7: Stern '''

#from gturtle import *
#
#makeTurtle()
#repeat 8:
#    forward(100)
#    backward(100)
#    right(360/8)



''' Aufgabe 1.13: Treppenstufen (Bitte lösen)'''



''' Aufgabe 1.14: Was macht dieses Programm (Bitte lösen)'''
#from gturtle import *
#
#makeTurtle()
#repeat 10:
#    forward(200)
#    backward(200)
#    right(90)
#    forward(1)
#    left(90




'''
===============================================================================
Unterkapitel 1.3 Kreise zeichnen und Schleifen in Schleifen legen
===============================================================================
'''

''' Beispiel 1.8: Vieleck mit 360 Ecken (=Kreis) '''

#from gturtle import *
#
#makeTurtle()
#repeat 360:
#    forward(2)
#    right(1)

    

''' Beispiel 1.9: Blütenblatt '''

#from gturtle import *
#
#makeTurtle()
#left(60)
#repeat 120:
#    forward(3)
#    right(1)
#right(60)
#repeat 120:
#    forward(3)
#    right(1)
#right(60)
#right(60)



''' Beispiel 1.10: Blüte (Schleifen in Schleifen) '''

#from gturtle import *
#
#makeTurtle()
#left(30)
#repeat 4:
#    repeat 60:
#        forward(3)
#        right(1)
#    right(120)
#    repeat 60:
#        forward(3)
#        right(1)
#    right(120)
#    right(360 / 4)    



''' Aufgabe 1.19 (Diskussion '''

''' Aufgabe 1.18: Blume (Bitte lösen)'''




'''
===============================================================================
Unterkapitel 1.4 Programme, die mit Texten arbeiten
===============================================================================
'''



''' Konzepte und Begriffe
- Datentyp Zahl:
  Dieser Datentyp beinhaltet ganze Zahlen und Kommazahlen. 
  Für die ganzen Zahlen verwenden wir die Bezeichung Integer.
  In Python wird wird die Kurform int benutzt.
  Für Kommazahlen verwenden wir die Bezeichung Float.
  In Python wird sie mit float bezeichnet.
- Datentyp Text:
  Texte stehen immer in Anführungszeichen. 
  Dadurch sieht der Computer sofort, dass es sich um einen Text handelt.
  Wir nennen diesen Datentyp String.
  In Python werden Strings mit str bezeichnet.
'''



''' Beispiel 1.11: Ausgaben '''

#print("Was machst du?\nIch programmiere.")



''' Konzepte und Begriffe
- print(Text): Der Befehl print("Hallo163") bewirkt, dass der Computer im Ausgabefenster den Text "Hallo163" ausgibt und dann im Ausgabefenster auf die nächste Zeile springt.
  Der Text, der ausgegeben werden soll, muss zwischen geraden Anführungszeichen (" ") stehen.
- \n: Innerhalb von Texten bewirkt die Zeichenfolge \n einen Zeilenumbruch im Ausgabefenster.
(Details zu print unter https://docs.python.org/2/reference/simple_stmts.html#the-print-statement)
'''



'''
--- Thema: Text wiederholen ---
'''


''' Beispiel 1.11: Ausgaben [Fortsetzung] (binary operator * performing a sequence repetition; binary operator + performing a concatenation'''

#print("Ich programmiere! Ich programmiere!")
#print("===================================")


''' Beispiel 1.12: Ausgaben [Fortsetzung] (binary operator * performing a sequence repetition; binary operator + performing a concatenation'''
#print("X     X")
#print(" X   X ")
#print("  X X  ")
#print("   X   ")


#print("X"   + " " * 5 + "X")
#print(" X"  + " " * 3 + "X")
#print("  X" + " " * 1 + "X")
#print("   X   ")



''' Aufgabe 1.20: Baum (Bitte lösen)'''



'''
===============================================================================
Programme, die rechnen
===============================================================================
'''



''' Beispiel 1.13: Berechne (163*3)-(77*4) '''

#print((163*3)-(77*4))



''' Aufgabe 1.22: Binäre mathematische Operatoren (Diskussion)'''



''' Beispiel 1.14: Berechne (163*3)-(77*4) '''
#print("14 * (19-8) = ")
#print(14 * (19-8))

#Besser
#print("14 * (19-8) = ", 14 * (19-8))



''' Konzepte und Begriffe
Unter einem Ausdruck verstehen wir einen arithmetischen Ausdruck oder einen Text. Für arithmetische Ausdrücke gilt:
- print(<Ausdruck1>, <Ausdruck2>, ...): Der Computer wertet zuerst jeden Ausdruck aus und gibt die Resultate anschliessend in einer Zeile im Ausgabefenster aus.
- <Zahl1> + <Zahl2>: Berechnet die Summe von Zahl1 und Zahl2.
- <Zahl1> - <Zahl2>: Berechnet die Differenz von Zahl1 und Zahl2.
- <Zahl1> * <Zahl2>: Berechnet das Produkt von Zahl1 und Zahl2.
- <Zahl1> / <Zahl2>: Berechnet die Division von Zahl1 und Zahl2.
- <Zahl1> // <Zahl2>: Berechnet die ganzzahlige Division von Zahl1 und Zahl2.
- <Zahl1> % <Zahl2>: Berechnet den Rest der ganzzahligen Division von Zahl1 und Zahl2.
- <Zahl> ** <n>: Berechnet die n-te Potenz von Zahl.
- sqrt(<Zahl>): Berechnet die Quadratwurzel von Zahl


Details:
- Binary Arithmetic Operations: https://docs.python.org/2/reference/expressions.html#binary-arithmetic-operations
- Operator Precedence: https://docs.python.org/2/reference/expressions.html#operator-precedence
- Function Evaluation (https://docs.python.org/2/reference/expressions.html#calls): "All argument expressions are evaluated before the call is attempted."
'''



''' Aufgabe 1.23: Ausdruck 4*4*4*4+1 berechnen und ausgeben (Bitte lösen)'''



''' Aufgabe 1.25: Rechteck mit Flächeninhalt 720 und erster Seite 48 Pixel (Bitte lösen)'''



''' Aufgabe 1.26: Haus (Bitte lösen)'''


''' Aufgabe 1.27: Gleichseitiges Dreieck (Bitte lösen)'''


''' Aufgabe 1.28: Haus mit roter Höhe (Bitte lösen)'''


