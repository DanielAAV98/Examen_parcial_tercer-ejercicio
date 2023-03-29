import numpy as np
import math
Num_ecua=int(input("Introduce el número de coeficientes: "));
Num_ecua=3;
while True:
    Matriz =list(map(float,input("Introduzca los coeficientes: ").split()));
    Matriz=np.asarray(Matriz)
    Matriz=Matriz.reshape (Num_ecua,Num_ecua);
    opcion= input("es correcta: Si No: ");
    if (str.lower(opcion)=="si"):
        break;
while True:
    Igualaciones =list(map(float,input("Introduzca las igualaciones: ").split()));
    Igualaciones=np.asarray(Igualaciones)
    opcion= input("es correcta: Si No: ");
    if (str.lower(opcion)=="si"):
        break;
    
print("A =", end="");
for j in range (0,len(Matriz)):
    for h in range (0,len(Matriz[0])):
        if h==0:
            print("\t|\t"+str(Matriz[j][h]), end="");
        elif h==len(Matriz[0])-1:
            print("\t"+str(Matriz[j][h]), end="\t|");
        else:
             print("\t"+str(Matriz[j][h]), end="");
    print();
print("\nB =", end="");
for j in range (0,len(Matriz)):
    print("\t|\t"+str(Igualaciones[j])+"\t|");
Matriz_cramer=[];
for h in range (0,len(Matriz)):
    Matriz_N=[]
    for j in range (0,len(Matriz)):
        fila=[]
        for i in range (0,len(Matriz)):
            if h==i:
                fila.append(Igualaciones[j]);
            else:
                fila.append(Matriz[j][i]);
        Matriz_N.append(fila)
    Matriz_cramer.append(Matriz_N)
x=0;
for i in range(0,len(Matriz)):
    x=np.linalg.det(Matriz_cramer[i])/np.linalg.det(Matriz);
    print("X"+str(i)+" = "+str(x));
    
    