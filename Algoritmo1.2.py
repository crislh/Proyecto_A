import random as rd
import matplotlib.pyplot as plt
import winsound
import time

def generar_valores(escala, notas, n):

    lista = []

    ost1 = []
    ost2 = []
    ost3 = []
    list_ost = []

    long_ost1 = 4
    long_ost2 = 4
    long_ost3 = 4
    #long_ost1 = rd.randint(3, 4)
    #long_ost2 = rd.randint(3, 4)
    #long_ost3 = rd.randint(3, 4)

    ost1.append(notas[escala[0]])

    for i in range(long_ost1 - 1):
        ost1.append(notas[escala[rd.randint(0, 4)]])
        i += 1
    list_ost.append(ost1)
    
    for i in range(long_ost2):
        ost2.append(notas[escala[rd.randint(0, 4)]])
        i += 1
    list_ost.append(ost2)

    for i in range(long_ost3):
        ost3.append(notas[escala[rd.randint(0, len(escala) - 1)]])
        i += 1
    list_ost.append(ost3)

    for i in range(n):
        for j in rd.choice(list_ost):
            lista.append(j)
        i += 1

    return lista

def reproducir(lista):
    for i in lista:
        time.sleep(0.5)
        winsound.PlaySound(r'C:\Users\crist\OneDrive\Escritorio\Universidad\Análisis\Proyecto 1\NOTAS\C4.wav', winsound.SND_FILENAME)

tiempo = []
esc = [0, 2, 4, 5, 7, 9, 11]
#notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
notas = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']

valores = generar_valores(esc, notas, 12)

for i in range(len(valores)):
    i += 1
    tiempo.append(i)

print(valores)
#reproducir(valores)

plt.scatter(tiempo, valores)
plt.show()
