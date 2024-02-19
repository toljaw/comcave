#
# Arithmetische Operatoren
#

n1 = 35
n2 = -50

# Addition
erg = n1 + n2       # In erg ist die Summe von n1 und n2
print('{} + {} = {}'.format(n1, n2, erg))

# Subtraktion
erg = n1 - n2       # In erg ist die Differenz von n1 und n2
print('{} - {} = {}'.format(n1, n2, erg))

# Multiplikation
erg = n1 * n2       # In erg ist das Produkt von n1 und n2
print('{} * {} = {}'.format(n1, n2, erg))

# Division
erg = n1 / n2       # In erg ist der Quotient von n1 und n2
print('{} / {} = {}'.format(n1, n2, erg))

n2 = 50
# Ganzzahldivision
erg = n2 // n1      # In erg der Ganzzahlanteil der Division n2 / n1
print('{} // {} = {}'.format(n2, n1, erg))


# Der Modulo-Operator %
erg = n2 % n1       # In erg der Rest der Division n2 / n1
print('{} % {} = {}'.format(n2, n1, erg))


n1 = 5
n2 = 3
# Potenzierung: 5^3 = 5 * 5 * 5
erg = n1 ** n2          # In erg ist das Ergebnis von 5^3
print('{} ** {} = {}'.format(n2, n1, erg))


#
# Kurzhandschreibweisen
#
print("*"*5 + " Kurzhandschreibweisen " + "*"*5)
n1 = 10
n2 = 30

n1 += n2                # n1 = n1 + n2
print("n1 = n1 + n2: {}".format(n1))

n1 -= n2                # n1 = n1 - n2
print("n1 = n1 - n2: {}".format(n1))
