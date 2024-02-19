'''
Gegeben sei das folgende tuple t:
'''

t = (1, 20, 30)

'''
Aufgaben:


1. Lesen Sie den ersten, zur Verfügung stehenden, Index von t aus.
'''
print(f"\nDas erste Element des Tuple's 't' ist: {t[0]}\n")

'''
2. Versuchen Sie diesen Wert auf 10 zu ändern.
'''
# t.remove(0)     #tuples kann man nicht verändern. Aßerdem haben sie nur die Methoden '.count()' und '.index()'... 
# print(t)

# del(t[0])       #TypeError: 'tuple' object doesn't support item deletion
# print(t)        

'''
3. Konvertieren Sie das Tuple nun in eine Liste mit der Funktion list().
'''
l = list(t)

'''
4. Lesen Sie die in 3. erstellte Liste nun aus und ändern Sie daraufhin den ersten Index auf 10.
'''
print(f"Die Liste 'l' sieht so aus: {l}")
print()
l.pop(0)
l.insert(0,10)
print(f"Das erste Element (hier '1') wurde mit '10' ersetzt.\nJetzt sieht die Liste so aus: {l}\n")

'''
5. Konvertieren Sie die Liste nun zurück in das Tuple mit dem Namen t unter verwendung der Funktion tuple().
'''
t = tuple(l)
print(f"Der geänderte Tuple 't' sieht jetzt so aus: {t}\n")
t = (50,20.66)
print(t)