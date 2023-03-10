import numpy

A = numpy.zeros((3,3))
B = numpy.zeros((3,1))
C = numpy.zeros ((3,1))
for i in range(3):
  for j in range(3):
    A[i,j]= int(input("Ingresa un numero para la posicion " + str(i) + "," + str(j) + ": "))

print("")
#for i in range(3):
  #for j in range(3):
    #print(" La posicion "+ str(i) + "," + str(j) +" es " + str(A[i,j]))

for i in range(3):
  for j in range(1):
    B[i,j]= int(input("Ingresa los numeros de la matriz solucion: " + str(i) + "," + str(j) + ": "))

AB = numpy.concatenate((A,B), axis=1)
ABC = numpy.copy(AB)

tamaño = numpy.shape(ABC)
n = tamaño[0]

print("")
print("\nLa matriz ingresada es:\n")
print(A)
print("\nLa Matriz Solucion es:\n")
print(B)
print("\nLa Matriz es: \n")
print(AB)
print("\nLa Matriz en diagonal 0 es: \n")



for i in range(0,n):
    pivote =  ABC[i,i]
    adelante = i+1
    for j in range(adelante,n):
      factor = ABC[j,i] / pivote
      for k in range(i,n+1):
        ABC[j,k] = ABC[j,k] - (factor) * ABC[i, k]

    
print( ABC,'\n')

print('Las incognitas son:\n')
Z = ABC[2,3] / ABC[2,2]
Y = (ABC[1,3] - ABC[1,2] * Z) / ABC[1,1]
X = (ABC[0,3] - (ABC[0,2] * Z) - (ABC[0,1] * Y)) / ABC[0,0]

C[0,0] = X
C[1,0] = Y
C[2,0] = Z

print (C)
