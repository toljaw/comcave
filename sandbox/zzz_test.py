'''
import random
studentList = ["Muhamed", "Kirill", "Fabio", "Arijan", "Peter", "Masuda", "Anatoli"]
randomStudent = studentList[random.randint(0, 6)]
print(randomStudent)
'''

liste1 = [1,2,2,3,4,5]

liste1.append(34)
liste1.append(False)
liste1.append("STARK")

dict1 = {
    "Fabio": "ok",
    "Kirill": "ok"
}

print(liste1)
print(dict1)

ersterInput = input("Was geht? ")

print(ersterInput)
print(dict1.get("Fabio"))
