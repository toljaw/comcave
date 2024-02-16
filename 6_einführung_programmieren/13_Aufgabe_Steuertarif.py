import math
"""
Die deutsche Einkommensteuer wird nach § 32a aus dem Einkommensteuergesetz (EStG) berechnet:

§ 32a Einkommensteuertarif
(1) 1 Die tarifliche Einkommensteuer bemisst sich nach dem auf volle Euro abgerundeten zu versteuernden Einkommen. 2 Sie beträgt im Veranlagungszeitraum 2023 vorbehaltlich der §§ 32b, 32d, 34, 34a, 34b und 34c jeweils in Euro für zu versteuernde Einkommen

1.
    bis 10 908 Euro (Grundfreibetrag):
    0;
2.
    von 10 909 Euro bis 15 999 Euro:
    (979,18 · y + 1 400) · y;
3.
    von 16 000 Euro bis 62 809 Euro:
    (192,59 · z + 2 397) · z + 966,53;
4.
    von 62 810 Euro bis 277 825 Euro:
    0,42 · x – 9 972,98;
5.
    von 277 826 Euro an:
    0,45 · x – 18 307,73.

3 Die Größe „y“ ist ein Zehntausendstel des den Grundfreibetrag übersteigenden Teils des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens. 4 Die Größe „z“ ist ein Zehntausendstel des 15 999 Euro übersteigenden Teils des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens. 5 Die Größe „x“ ist das auf einen vollen Euro-Betrag abgerundete zu versteuernde Einkommen. 6 Der sich ergebende Steuerbetrag ist auf den nächsten vollen Euro-Betrag abzurunden.

Quelle: https://www.gesetze-im-internet.de/estg/__32a.html


Aufgabe:

Erstellen Sie ein Python-Skript, dass den die oben beschriebene Berechnung der Einkommensteuer implementiert. Testen Sie Ihren Code daraufhin mit einigen, selbst gewählten, Werten.
"""

zu_verst_eink = input("\nWie hoch war Ihr zu versteuerndes Einkommen in €? ")

x = math.floor(float(zu_verst_eink))
y = x/10000
z = (x-15999)/10000

if x <= 0:
    print("\nSie haben kein Einkommen erwirtschaftet und haben dem entsprechend keine Steuerabgaben.\n")
elif x <= 10908:
    print(f"\nIhr erwirtschaftetes Einkommen beträgt {x}€. Ihre Steuerabgaben betragen somit 0€. \n")
elif x <= 15999:
    print(f"\nIhr erwirtschaftetes Einkommen beträgt {x}€. Ihre Steuerabgaben betragen somit {round((979.18 * y + 1400) * y, 2)}€. \n")
elif x <= 62809:
    print(f"\nIhr erwirtschaftetes Einkommen beträgt {x}€. Ihre Steuerabgaben betragen somit {round((192.59 * z + 2397) * z + 966.53, 2)}€. \n")
elif x <= 277825:
    print(f"\nIhr erwirtschaftetes Einkommen beträgt {x}€. Ihre Steuerabgaben betragen somit {round(0.42 * x - 9972.98, 2)}€. \n")    #miese Nummer mit dem '-' als char in der Formel :P
else:
    print(f"\nIhr erwirtschaftetes Einkommen beträgt {x}€. Ihre Steuerabgaben betragen somit {round(0.45 * x - 18307.73, 2)}€. \n")

'''
Gestestet wird hier dur die Eingabe des Einkommens!!!
'''