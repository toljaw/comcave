'''
511
Gib alle ganzen Zahlen von 1 bis 10 aus.
'''
# for zahl in range(1,11):
#     print(zahl)


'''
512
Gib alle Dezimalzahlen zwischen 0 und 1 aus mit einer Schrittweite von 0.1 .
'''
# for zahl in range(0,11):
#     print(zahl/10)


'''
513
Gib jede dritte Zahl zwischen 1 und 20 aus. 
'''
# for zahl in range(3,21, 3):
#     print(zahl)


'''
514
Gib Zahlen  zwischen -30 und 30 aus. Es soll aber nur jede vierte Zahl sein. 
Ausgabe: 

-30 -26 -22 -18 -14 -10 -6 -2 2 6 10 14 18 22 26 30 

Hinweis: Ausgabe hintereinander: 

print ( ….. , end=" ") # Leerzeichen als String hinter end= 
'''
# for zahl in range(-30,31,4):
#     print(zahl, end=" ")


'''
515
Betrachte alle Zahlen zwischen 1 und 100 (1 und 100 eingeschlossen). 
Ist eine Zahl durch 8 teilbar, so gib diese Zahl aus. 
Ist eine Zahl durch 12 teilbar, so gib diese Zahl aus. 

Hinweis: Ausgabe hintereinander: 

print ( ….. , end=" ") # Leerzeichen als String hinter end= 
'''
# for zahl in range(1,101):
#     if zahl % 8 == 0 or zahl % 12 == 0:
#         print(zahl, end=" ")


'''
521
Zähle einen Wert mit ganzen Zahlen von 1 bis 200 aufwärts. Gib dafür eine Schrittweite ein oder setze eine Variable. Benutze keine for-Anweisung. 
'''
# schrittweite = 10
# zahl = 1
# zählen = True

# while zählen:
#     print(zahl)
#     zahl += schrittweite
#     if zahl > 200:
#         zählen = False


'''
522
Bestimme eine Schrittweite. Zähle einen Wert mit ganzen Zahlen von 0 aufwärts bis 199. Ist der Wert 199 erreicht oder überschritten, so zähle den Wert mit der Schrittweite wieder abwärts bis 0 oder weniger erreicht ist. 
'''
# schrittweite = 11
# zahl = 0
# zählen = True

# while zählen:
#     print(zahl)
#     zahl += schrittweite
#     if zahl >= 199:
#         schrittweite *= -1
#     if zahl <= 0:
#         print(zahl)
#         zählen = False


'''
523
Mache den Code aus CC-522 zu einer Endlosschleife. (Abbruch ist dann mit CTRL-C möglich!) 
'''
# schrittweite = 11
# zahl = 0
# zählen = True

# while zählen:
#     print(zahl)
#     zahl += schrittweite
#     if zahl >= 199:
#         schrittweite *= -1
#     if zahl <= 0:
#         print(zahl)
#         #zählen = False