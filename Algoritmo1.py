import random as rd
import matplotlib.pyplot as plt

def generar_valores(escala, notas, hom, n):

    lista = []
    lista_f = []

    buc1 = []
    buc2 = []
    buc3 = []
    lista_buc = []
    long_buc1 = 4
    long_buc2 = 4
    long_buc3 = 4

    buc1.append(notas[escala[0]])

    for i in range(long_buc1 - 1):
        buc1.append(notas[escala[rd.randint(0, 4)]])
    lista_buc.append(buc1)
    
    for i in range(long_buc2):
        buc2.append(notas[escala[rd.randint(0, 4)]])
    lista_buc.append(buc2)

    for i in range(long_buc3):
        buc3.append(notas[escala[rd.randint(0, len(escala) - 1)]])
    lista_buc.append(buc3)

    for i in range(hom):
        lista.insert(rd.randint(0, n - 1), rd.choice(lista_buc))
    
    for i in range(n - hom):
        lista_rand = []
        for _ in range(4):
            lista_rand.append(notas[escala[rd.randint(0, len(escala) - 1)]])
        lista.insert(rd.randint(0, len(lista) - 1), lista_rand)

    for i in lista:
        for j in i:
            lista_f.append(j)

    print('\n', buc1, '\n', buc2, '\n', buc3, '\n',)

    return lista_f

tiempo = []
esc = [0, 2, 4, 5, 7, 9, 11]
escM = [0, 2, 3, 5, 7, 9, 10]
indice_notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
notas = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']

valores = generar_valores(esc, indice_notas, 12, 16)
print(valores)

tiempo = list(range(1, len(valores) + 1))

plt.scatter(tiempo, valores)
plt.yticks(range(len(notas)), notas)
plt.show()