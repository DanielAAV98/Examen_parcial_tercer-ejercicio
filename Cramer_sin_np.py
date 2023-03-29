Num_ecua=int(input("Introduce la cantidad de ecuaciones: "))
print();
Matriz=[];
Igualaciones=[];

def deter3x3(M=[]):
    Suma=M[0][0]*(M[1][1]*M[2][2]-(M[1][2]*M[2][1]))-M[0][1]*(M[1][0]*M[2][2]-(M[1][2]*M[2][0]))+M[0][2]*(M[1][0]*M[2][1]-(M[1][1]*M[2][0])) 
    return Suma;

def deter2x2(M=[]):
    Suma=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return Suma;   
    
for i in range (0, Num_ecua):
    fila=list(map(float,input("Introduzca los coeficientes de los terminos, coloqué 0 si no esta el termino: ").split()));
    Igualaciones.append(float(input("Introduzca la igualacion ecuacion: ")));
    Matriz.append(fila);
    print();
    print("Ecuación",i+1, end=": ");
    for j in range(0,len(fila)):
        print("X"+str(j),str(fila[j])+" ",end="");
        if (not(len(fila)==j+1)):
            print("+ ",end="");
    print("=", Igualaciones[i]);
    print();
cramer=[];
print("A =",end="");
for j in range (0,Num_ecua):
    for h in range (0,len(Matriz[0])):
        if h==0:
            print("\t|\t"+str(Matriz[j][h]), end="");
        elif h==len(Matriz[0])-1:
            print("\t"+str(Matriz[j][h]), end="\t|");
        else:
             print("\t"+str(Matriz[j][h]), end="");
        if j==0:
            cramer.append(h);
    print();
print();
print("B =",end="");
for i in range (0, len(Igualaciones)):
        print("\t|\t",Igualaciones[i],"\t|")
Matriz_cramer=[];
for h in cramer:
    Matriz_N=[]
    for j in range (0,Num_ecua):
        fila=[]
        for i in range (0,len(Matriz[0])):
            if h==i:
                fila.append(Igualaciones[j]);
            else:
                fila.append(Matriz[j][i]);
        Matriz_N.append(fila)
    Matriz_cramer.append(Matriz_N)
    x=0;
try:
    if (len(Matriz)==3):
        for i in cramer:
            x=deter3x3(Matriz_cramer[i])/deter3x3(Matriz);
            print("X"+str(i),"=",x)
                  
    if (len(Matriz)==2):
        for i in cramer:
            x=deter2x2(Matriz_cramer[i])/deter2x2(Matriz);
            print("X"+str(i),"=",x)
except:
            print("No tiene solución")
    
    