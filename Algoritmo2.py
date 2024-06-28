import random as rd
import matplotlib.pyplot as plt

def generar_valores(escala, notas, n, sub_n):

    cant_partes = 3
    lista = []
    lista_f = []

    for _ in range(cant_partes):

        parte = []
        buc1 = []
        buc2 = []
        buc3 = []
        lista_buc = []
        long_buc1 = 4
        long_buc2 = 4
        long_buc3 = 4

        buc1.append(notas[escala[0]])

        for _ in range(long_buc1 - 1):
            buc1.append(notas[escala[rd.randint(0, 4)]])
        lista_buc.append(buc1)
    
        for _ in range(long_buc2):
            buc2.append(notas[escala[rd.randint(0, 4)]])
        lista_buc.append(buc2)

        for _ in range(long_buc3):
            buc3.append(notas[escala[rd.randint(0, len(escala) - 1)]])
        lista_buc.append(buc3)

        for _ in range(n//sub_n):
            for i in lista_buc[rd.randint(0, len(lista_buc) - 1)]:
                parte.append(i)
        
        lista.append(parte)
    
    for _ in range(sub_n):
        lista_f.append(lista[rd.randint(0, len(lista) - 1)])

    return lista_f

metrica = []
esc = [0, 2, 4, 5, 7, 9, 11]
escM = [0, 2, 3, 5, 7, 9, 10]
indice_notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
notas = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']

valores = generar_valores(esc, indice_notas, 32, 8)

print(valores)

#metrica = list(range(1, len(valores) + 1))

#plt.scatter(metrica, valores)
#plt.yticks(range(len(notas)), notas)
#plt.show()





