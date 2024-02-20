"""
1
#Definiere eine Funktion zur Berechnung des Mittelwertes zweier Zahlen. 
"""

# n1 = 14 
# n2 = 20 

# def  mittel(a,b):
#     '''Beschreibung blub blub...'''
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
# n= 100


# def sumA(n):
#     summe = 0
#     hilfszahl = 1
#     while hilfszahl < n + 1:
#         summe = summe + hilfszahl
#         hilfszahl += 1
#     return summe


# def sumB(n):
#     summe = 0
#     hilfszahl = 1
#     while True:
#         summe = summe + hilfszahl
#         hilfszahl += 1
#         if hilfszahl == 101:
#             break
#     return summe


# def sumC(n):
#     summe = 0
#     for i in range(0,101):
#         summe += i
#     return summe

# print ('kopfgesteuert:', sumA (n) ) 

# print ('fußgesteuert:', sumB (n) ) 

# print ('Zählschleife:', sumC (n) ) 


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
import time 

n=5000   # Summe 1 bis 5000  

dummy =0 

#Funktionen:
def sumA (n): 
    summe = 0 
    hilfszahl=1 

    while hilfszahl <= n: 
        summe += hilfszahl 
        hilfszahl +=1 
    return summe 


def sumB(n):
    summe = 0
    hilfszahl = 1
    while True:
        summe = summe + hilfszahl
        hilfszahl += 1
        if hilfszahl == n+1:
            break
    return summe


def sumC(n):
    summe = 0
    for i in range(0,n+1):
        summe += i
    return summe


#Messungen:
startA = time.time() 

for j in range (10000):     # 10000 mal Berechnung wiederholen 
    dummy = sumA(n) 

endA = time.time() 
dauerA = endA - startA 
print ('Variante A:', dauerA, ' sec') 


startB = time.time() 

for j in range (10000):     # 10000 mal Berechnung wiederholen 
    dummy = sumB(n) 

endB = time.time() 
dauerB = endB - startB 
print ('Variante B:', dauerB, ' sec') 


startC = time.time() 

for j in range (10000):     # 10000 mal Berechnung wiederholen 
    dummy = sumC(n) 


endC = time.time() 
dauerC = endC - startC 
print ('Variante C:', dauerC, ' sec') 


'''
Die Messung aus der 3. Aufgabe führt zum folgenden Ranking:

🥇  Variante C: 1.6409039497375488  sec
🥈  Variante A: 2.1161859035491943  sec
🥉  Variante B: 2.8371880054473877  sec
'''
