"""
1
#Definiere eine Funktion zur Berechnung des Mittelwertes zweier Zahlen. 
"""

# n1 = 14 
# n2 = 20 

# def  mittel(a,b):
#     ergebnis = (a+b)/2
#     return ergebnis 


# print (mittel(n1,n2)) 

"""
2
Schau dir Aufgabe 6 von Tag 5 an und Aufgabe 7. 
Du findest dort 3 Varianten zur Summenberechnung. 

Erstelle drei Funktionen  sumA (kopfgesteuert), sumB(fußgesteuert), sumC (Zählschleife). 

Eingabe jeder Funktion :  die ganze Zahl n 

Ausgabe jeder Funktion: die Summe von 1 bis n 

so sieht dein main-Abschnitt aus: 

n= 100 

# Definition der verschiedenen Funktionen 

# main - Hauptcode 

print ('kopfgesteuert:', sumA (n) ) 

print ('fußgesteuert:', sumB (n) ) 

print ('Zählschleife:', sumC (n) ) 

Hinweis: du kannst die obigen Code-Zeilen rauskopieren….in deine  IDE 
"""


"""
3
Welche der Varianten aus Aufgabe 2 ist am schnellsten? 
Wie kannst du das ermitteln ? 
Hinweis: Zeitmessung….. 

Vorlage des PythonCodes:: 

import time 

n=5000   # Summe 1 bis 5000  

dummy =0 

def sumA (n): 
    summe = 0 
    hilfszahl=1 

    while hilfszahl <= n: 
        summe += hilfszahl 
        hilfszahl +=1 
    return summe 

startA = time.time() 

for j in range (10000):     # 10000 mal Berechnung wiederholen 
    dummy = sumA(n) 

endA = time.time() 
dauerA = endA - startA 
print ('Variante A:', dauerA, ' sec') 

Erweitere die Zeitmessung um sumB() und um SumC(). 

Welche Variante ist am schnellsten? 
"""