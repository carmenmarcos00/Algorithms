#Mayo-2020
#Realizado por Carmen Marcos Sánchez de la Blanca
#Prueba: ej2_practica('ej_pts_01.txt')

#Importamos la funcioón para hacer la raiz cuadrada de la librería math
from math import sqrt

#Función principal
def ej2_practica(fichero):

  #Leo el fichero
  x_datos,y_datos = leefich(fichero)


  #Inicializo variables
  distancia_min = 1000000.000

  #Gestión de errores si me pasan menos de 2 puntos
  if(len(x_datos)<2):
    return (distancia_min)

  for i in range(len(x_datos)):
    #Cogemos el primer punto
    x1 = x_datos[i]
    y1 = y_datos[i]
    for j in range(i+1,len(x_datos)):

      #Si i es distinto que j. Si no la distancia sería 0, cogeriamos 2 veces el mismo punto
      if i!=j:
        #Cogemos el segundo punto
        x2 = x_datos[j]
        y2 = y_datos[j]

       #Fórmula para calcular la distancia entre 2 puntos
        distancia= sqrt((x1 - x2)**2 + (y1 - y2)**2)

        #En caso de que la distancia recién calculada sea menor se actualiza la variable
        if distancia < distancia_min:
          distancia_min = distancia
  #Tras la ejecución mostramos por pantalla la distancia minima
  print('dist:',distancia_min)


#Función para leer el fichero
def leefich(fichero):
  #Abrimos el fichero "ej_pts_01.txt" leerle
  leefichero = open(fichero, 'r')
  x_datos = []                #  Creamos una lista para la primera columna, coordenadas x
  y_datos = []                #  Creamos una lista para la segunda columna, coordenadas y
  lineas = leefichero.readlines() # Leemos el fichero línea a línea
  #Elimino la primera línea leída, no es un punto
  lineas.pop(0)

  for linea in lineas:
    x, y = linea.split()     # Se separa las 2 columnasdos columnas
    x_datos.append(float(x)) # Añado el elemento x a la lista x_datos
    y_datos.append(float(y)) # Añado el elemento y a la lista y_datos

  leefichero.close()
  return x_datos, y_datos
