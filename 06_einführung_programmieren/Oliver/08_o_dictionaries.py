#
# Dictionaries
#

d1 = {}              # Händische Zuweisung eines leeren Dictionaries
d2 = dict()          # Das gleiche wie bei d1, nur über den Konstruktor der Klasse

# Messung des Typs von d1 und d2
print(type(d1))
print(type(d2))

d3 = {'vorname': 'Sharon', 'nachname': 'Tate'}
d4 = dict({'vorname': 'Vincent', 'nachname': 'Price'})

print()
# Einfache Ausgabe von d3 bzw. d4
print(d3)
print(d4)

print()
# Wenn wir einzelne Bestandteile eines dictionaries auslesen wollen, können wir dies machen, wenn wir uns auf
# den entsprechenden key beziehen, d.h. der Index ist der Key.
print(f"{d3['vorname']}, {d3['nachname']}")
print(f"{d4['vorname']}, {d4['nachname']}")


# Es ist möglich, einem leeren Dictionary, wie d1 und d2 ein key:value-Paar hinzuzufügen.
d1['vorname'] = 'Gene'
d1['nachname'] = 'Hackman'
print(f"{d1['vorname']} {d1['nachname']}")

# Die einem dict zur Verfügung stehenden Funktionen kann man - wie bei den anderen Typen auch - mit dir() auslesen.

print()
print(dir(d1))

# Mit entsprechenden Funktionen/Methoden kann man ausgewählte Aspekte eines dicts auslesen bzw. ansteuern.

# Nur die keys erhalten wir mit keys():
print()
print(d1.keys())

# Nur die Values erhalten wir mit values():
print(d1.values())

# Keys und values kann man mit items() auslesen:
print(d1.items())

# d4 ändert seinen Namen komplett
d4['vorname'] = 'Jimmy'
d4['nachname'] = 'Stewart'
print(d4)

# Wir erstellen nun eine Liste, die ihrerseits aus verschiedenen dictionaries besteht.

personen_liste = [d1, d3, d4]

# Wenn wir also nun die obige Liste haben und Informationen von d3 auslesen wollen, müssen wir den enstprechenden Listenindex an dieser Stelle nehmen.
print(personen_liste[1])                # entspricht d3

# Wenn wir den Vornamen vom 2ten Eintrag haben wollen, nehmen wir aus Sicht der Liste den Index 1 und sprechen beim resultierenden dict den gewünschten Key an.
vn = 'vorname'
print(personen_liste[1][vn])

print()
# Wir lassen einen for-Loop über das dict d1 laufen.
for x in d1:
    print(x)

# Mit der letzten Information können wir das dictionary auch dynamisch ansteuern indem wir x als Index von d1 annehmen.
print()
for x in d1:
    print(d1[x])                      # print(d1[x], end="\n")

print()
for x in d1:
    print(f'{x} => {d1[x]}')

# Um jedes einzelne Dictionary aus der obigen personen_liste auslesen zu können, sollte folgendes durchführbar sein:
# 1. Betrachte mit for jeden einzelnen Eintrag von personen_liste
# 2. Betrachte mit einem seperaten for jedes Dictionary, dass an der entsprechenden Listenposition hinterlegt ist.
print()
for person in personen_liste:                    # [d1, d3, d4]
    for key in person:                            # k = key, p = dict aus personen_list
        print(key, ' => ', person[key], end="\t")  # k = key, p[k] = value
    print()

# Alternative Variante das obige zu generieren:
print()
for person in personen_liste:
    for key, value in person.items():
        print(key, ' => ', value, end='\t')
    print()
