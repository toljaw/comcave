'''
Aufgaben:

Definieren Sie die folgende Liste:
'''

num_list = [10, -90, 1001, 43, -800]


'''
1. Messen Sie die Länge der Liste mit der Funktion len() und geben Sie diese, mit verschiedenen Möglichkeiten
Strings zu formatieren (%, f-String, format()), aus.
'''
num_list_laenge = len(num_list)
print(f"\nElementanzahl der Liste 'num_list': {num_list_laenge}\n")

'''
2. Geben Sie die einzelnen Werte von num_list aus, indem Sie den zugehörigen Index referenzieren.
'''
print(num_list[-1])
print(num_list[-2])
print(num_list[-3])
print(num_list[-4])
print(num_list[-5])
print()

'''
3. Erstellen Sie zunächst eine leere Liste mit dem Namen: num_list_geordnet und ermitteln
Sie mit der Funktion type(), ob es sich auch wirklich um eine Liste handelt.
'''
num_list_geordnet = []
print(f"Bei der Variable 'num_list_geordnet' handelt es sich um den Typ {type(num_list_geordnet)}")
print()

'''
4. Fügen Sie nun, zu der in 3. erstellten Liste die Werte von num_list nach und nach mit
der Methode append() so hinzu, dass die Liste num_list_geordnet die Werte von num_list in
aufsteigender Reihenfolge enthält.
''' 
num_list_geordnet = []
num_list_geordnet.append(num_list[4])
num_list_geordnet.append(num_list[1])
num_list_geordnet.append(num_list[0])
num_list_geordnet.append(num_list[3])
num_list_geordnet.append(num_list[2])
print(f"'num_list_geordnet' wurde manuell mit Methode '.append()' soriert und enthält folgende Elemente: {num_list_geordnet}")
print()

'''
5. Erstellen Sie eine weitere Liste num_list_geordnet_2, wo Sie bei Erstellung der Liste direkt
die, nach der Reihenfolge, geordneten Indizes von num_list zuweisen.
'''
num_list_geordnet_2 = num_list
num_list_geordnet_2.sort()

print(f"'num_list_geordnet_2' wurde mit der Methode '.sort()' automatisch sortiert und enthält folgende Elemente: {num_list_geordnet_2}\n")