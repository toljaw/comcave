#
# Listen
#

# Listen anlegen - Variante 1
l = list((1, 2, 3, 4, 5))                                   # Funktion

print("f-String Formatierung")
s = f'l: {l}\ttype(l): {type(l)}\tdir(l): {dir(l)}'
print(s)      #\t => Tabulator

print('\n\n%-Style Formatierung:\n')
s = 'l: %s, type(l): %s, dir(l): %s' % (l, type(l), dir(l))
print(s)

print('\n\nformat()-String Formatierung:\n')
s = 'l: {}, type(l): {}, dir(l): {}'.format(l, type(l), dir(l))
print(s)


# Listen anlegen - Variante 2
l2 = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

# Ausgabe einzelner Werte über den entsprechenden Index. Dieser beginnt bei 0, d.h. der maximalste Index, auf den wir uns beziehen können, entspricht der Länge einer Liste -1. Die Länge kann man dynamisch mit der Funktion len() messen.

n = len(l2)             # n enthält die Anzahl der Einträge von der Liste l2

print('\n\nAusgabe von l2 - Version 1')
print(l2[0])            # 1. Eintrag
print(l2[1])            # 2. Eintrag
print(l2[2])            # 3. Eintrag
print(l2[3])            # 4. Eintrag
print(l2[4])            # 5. Eintrag
print(l2[5])            # 6. Eintrag
print(l2[6])            # 7. Eintrag


print('\n\nAusgabe von l2 - Version 2')
# Wir geben das gleiche aus, nur mit jeweiligem Bezug auf die oben definierte Variable n
print(l2[n - 7])            # 1. Eintrag
print(l2[n - 6])            # 2. Eintrag
print(l2[n - 5])            # 3. Eintrag
print(l2[n - 4])            # 4. Eintrag
print(l2[n - 3])            # 5. Eintrag
print(l2[n - 2])            # 6. Eintrag
print(l2[n - 1])            # 7. Eintrag
