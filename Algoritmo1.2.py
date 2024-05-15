import random as rd
import matplotlib.pyplot as plt
import winsound
import time

def generar_valores(escala, notas, hom, n):

    lista = []
    lista_f = []

    buc1 = []
    buc2 = []
    buc3 = []
    list_buc = []

    long_buc1 = 4
    long_buc2 = 4
    long_buc3 = 4

    buc1.append(notas[escala[0]])

    for i in range(long_buc1 - 1):
        buc1.append(notas[escala[rd.randint(0, 4)]])
        i += 1
    list_buc.append(buc1)
    
    for i in range(long_buc2):
        buc2.append(notas[escala[rd.randint(0, 4)]])
        i += 1
    list_buc.append(buc2)

    for i in range(long_buc3):
        buc3.append(notas[escala[rd.randint(0, len(escala) - 1)]])
        i += 1
    list_buc.append(buc3)

    for i in range(hom):
        lista.insert(rd.randint(0, n - 1), rd.choice(list_buc))
        i += 1
    
    for i in range(n - hom):
        list_rand = []
        for _ in range(4):
            list_rand.append(notas[escala[rd.randint(0, len(escala) - 1)]])
        lista.insert(rd.randint(0, len(lista) - 1), list_rand)
        i += 1

    for i in lista:
        for j in i:
            lista_f.append(j)

    print('\n', buc1, '\n', buc2, '\n', buc3, '\n',)

    return lista_f

#def reproducir(lista):
#    for i in lista:
#        time.sleep(0.5)
#        winsound.PlaySound(r'C:\Users\crist\OneDrive\Escritorio\Universidad\Analisis\Proyecto 1\NOTAS\C4.wav', winsound.SND_FILENAME)

tiempo = []
esc = [0, 2, 4, 5, 7, 9, 11]
ecsM = [0, 2, 3, 5, 7, 9, 10]
#notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
notas = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']

valores = generar_valores(esc, notas, 22, 30)

for i in range(len(valores)):
    i += 1
    tiempo.append(i)

print(valores)
#reproducir(valores)

plt.scatter(tiempo, valores)
#lt.subplot().set_ylim(notas[0], notas[11])
plt.subplot().set_yticks(range(len(notas)))
plt.show()