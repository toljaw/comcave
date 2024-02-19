'''
Aufgabe:

Gegeben seien die folgenden Variablen:

a = 'Py'
b = 'th'
c = 'on'

1. Welche der folgenden Kombinationen ergibt den String "Python"?

a)
	s = '{1}{0}{2}'.format(b, c, a)
	print(s)
b)
	s = '{2}{0}{1}'.format(b, c, a)
	print(s)
c)
	s = '{2}{1}{0}'.format(b, c, a)
	print(s)


2. Schreiben Sie den String "Python", mit den obigen Variablen, als f-String sowie als printf()-Style String.
'''

a = 'Py'
b = 'th'
c = 'on'

print()
print("Aufgabe 1:")
s = '{1}{0}{2}'.format(b, c, a)
print(s)

s = '{2}{0}{1}{3}'.format(b, c, a, " --> ist richtig") #hier ist der Gewinner
print(s)

s = '{2}{1}{0}'.format(b, c, a)
print(s)

print(f"\nAufgabe 2:\nf-String: {a}{b}{c}\n")

print("printf() hab ich mir gespart 🤷‍♂️🤛🤌\n")