'''
Gegeben Sei die folgende Umsatzliste der ABC AG für ein Kalenderjahr:

abc_ag_umsaetze = [
    8000, 7000, 800,
    0, 12000, 5000,
    3500, 2700, 0
    1900, 2500, 9500
    ]


Aufgaben:

1. Erstellen Sie zunächst ein leeres Dictionary mit dem Namen: abc_ag_dict
Nutzen Sie hierzu wahlweise den dict()-Konstruktor oder auch die einfache
Zuweisung mittels {}.
'''
abc_ag_dict = {}

'''
2. Weisen Sie dem, eben erstellten, Dictionary einen key mit dem Namen:
"Firma" zu und geben Sie dem key den Wert: "ABC AG".
'''
abc_ag_dict = {
    "Firma": "ABC AG"
}
print(f"\nDie Dictionary 'abc_ag_dict' enthält folgende Keys und Values: {abc_ag_dict}\n")


'''
3. Legen Sie nun weitere Keys an, die den Monatsnamen oder einfachen Zahlen entsprechen,
die zugehörigen Werte stammen dabei aus der obigen Liste.

Bsp.:
abc_ag_dict['Januar'] = abc_ag_umsaetze[0]
abc_ag_dict['Feburar'] = abc_ag_umsaetze[1]
usw.
'''
abc_ag_umsaetze = [
    8000, 7000, 800,
    0, 12000, 5000,
    3500, 2700, 0,
    1900, 2500, 9500
    ]

monate = [              #für die Monate habe ich eine seperate Liste erstellt
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember",
    ]

dict_umsätze = dict(zip(monate, abc_ag_umsaetze))   #beide Listen wurden hier mit der Funktion 'zip()'zu einer Dictionary zusammengefügt
#print(dict_umsätze)

abc_ag_dict.update(dict_umsätze)                    #mit der Methode '.update()' wurden beide Dictionaries zusammengefügt
#print(abc_ag_dict.items())

for i in abc_ag_dict:                               #mit Hilfe der for-Schleife wurden hier Keys und Values ausgegeben
    print(f"{i}: {abc_ag_dict.get(i)}")
print()

"""
4. Führen Sie nun die folgenden Auswertungen durch und fügen Sie diese als key/value-Paare
dem dict hinzu.

Key:            Value:
Umsatz_Q1       Summe der Umsätze aus abc_ag_umsaetze[0] - abc_ag_umsaetze[2]
Umsatz_Q2       Summe der Umsätze aus abc_ag_umsaetze[3] - abc_ag_umsaetze[5]
Umsatz_Q3       Summe der Umsätze aus abc_ag_umsaetze[6] - abc_ag_umsaetze[8]
Umsatz_Q4       Summe der Umsätze aus abc_ag_umsaetze[9] - abc_ag_umsaetze[11]

Die kumulierten Umsätze können Sie wahlweise mit der Funktion sum() oder auch händisch berechnen.
Wenn Sie mit sum() arbeiten können Sie die Listenwerte geeignet slicen.
"""

umsatz_kum = [8000]

for i in range(11):
    umsatz_kum.append(umsatz_kum[i] + abc_ag_umsaetze[i+1])
    
print(umsatz_kum)
print()

#kommt evtl. später
"""
5. Geben Sie das dict nun aus.
"""