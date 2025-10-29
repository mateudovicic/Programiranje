"""
moja_lista = [10,20,30]

prvi_element = moja_lista[0]

print(prvi_element)

moja_lista.append(40)

print (moja_lista)

dio_liste = moja_lista[1:3]

print(dio_liste)

lista_voce = ["jabuka","banana","kruška"]
print(lista_voce[0])
lista_voce.append("naranca")
print(lista_voce)
"""
#2d liste
ormar = [
    ['majica','kapa','sal'],
    ['hlace','carape','remen'],
    ['jakna','cipele','cizme']
]
"""
print (f"hlace?{ormar[1][0]}")

print (ormar[0][1])
print (ormar[1][1])
print (ormar[2][1])

for odjeca in ormar:
    print(odjeca[1])

for redak in ormar:
    print(f"Sadržaj retka:{redak}")

    for element in redak:
      print(f"Element:{element}")

"""

def pronadji_broj (lista,broj):
    print(f"Tražim broj{broj}u listi {lista}")

    prekidac = False

    for element in lista:
        if element == broj:
            prekidac = True
            break
        else:
            prekidac = False

    if prekidac:
        print(f"Broj {broj} je na listi")
    else:
        print(f"Broj {broj} nije na listi")
          

lista= [10, 20, 30, 40, 50]
broj = 130
pronadji_broj (lista,broj)