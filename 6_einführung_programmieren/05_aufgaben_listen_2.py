'''
Aufgaben:

Gegeben sei die folgende Liste:
'''

l = [42, 109, -30]
print(f"\nDie Liste 'l' sieht so aus: {l}\n")


'''
1. Recherchieren Sie die Arbeitsweise der Methoden insert() und append() und zeigen Sie, an einem
selbst gewählten Beispiel, wie die Methode insert() in die Methode append() überführt werden kann.
'''
l.insert(1,666)
print(f"Durch die Methode 'insert' kann man Elemente (hier '666') in die gewünschte Position (hier Index 1) der Liste einfügen.\nDie geänderte Liste 'l' sieht folgenderweise aus: {l}\n")

l.append(555)
print(f"Durch die Methode 'append' kann man Elemente (hier '555') an das Ende der Liste einfügen.\nDie geänderte Liste 'l' sieht folgenderweise aus: {l}\n")

l.insert(len(l),444)
print(f"Wenn man mit Hilfe der Methode 'insert' anstelle des Index's die Listenlänge verwendet, erhält man immer den Index des letzten Elements +1. Damit kann man Elemente (hier '444') an das Ende der Liste einfügen.\nDie geänderte Liste 'l' sieht folgenderweise aus: {l}\n")

'''
2. Die Methode pop() löscht das letzte Element einer Liste. Entwickeln Sie eine Idee, wie dies alternativ
mit dem Schlüsselwort del umgesetzt werden kann.
'''
l.pop()
print(f"Durch die Methode 'pop' wird das letzte Element (hier '444') der liste gelöscht.\nDie neue Liste 'l' sieht so aus: {l}\n")
del(l[len(l)-1])
print(f"Man kann ebenso das Schlüsselwort 'del' verwenden. Für den Index wird die Länge der Liste - 1 verwendet (Zählung der Elemente fängt bei 0 an).\nDie neue Liste (hier wurde das '555' gelöscht) sieht so aus: {l}\n")