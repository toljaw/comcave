"""
Aufgabe:

Gegeben sei der folgende String:
"""

s = "8791"

"""
Überlegen Sie, wie eine Vorschrift aussehen könnte die prüft, ob es sich dabei um einen String handelt,
der eine Dezimalzahl (10er-Zahl) darstellt. Eine grundlegende herangehensweise könnte so aussehen, dass
jede Komponente des Strings so geprüft wird, ob diese im Bereich "0" bis "9" liegt. Dazu könnte man bspw.
das logische AND nutzen. Schreiben Sie die Logik des Algorithmus zunächst in Pseudocode (Artikel) auf.
"""
dez_liste = []

for n in range(0, 10):
    dez_liste.append(str(n))

dezimal = True

for c in s:
    if c not in dez_liste:
        dezimal = False

if dezimal == True:
    print("\nDer String 's' stellt eine reine Dezimalzahl dar.\n")
else:
    print("\nDer String 's' stellt keine reine Dezimalzahl dar.\n")
    