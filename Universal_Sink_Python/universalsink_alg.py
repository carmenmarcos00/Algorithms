
#Author: Carmen Marcos Sánchez de la Blanca
#Date: May-2020


##DETERMINE IF THERE IS AN UNIVERSAL SINK IN A GRAPH:


#Main Function: Complexity O(n)
#Testing: det_sumidero_universal(([0,1,1],[0,0,1],[0,0,0]))
def det_sumidero_universal(A):
  
  ##Call aux. function
  set=det_vertice(A)
  ##Pop the node
  vertice =set.pop()
  
  #Make sure the row of the matrix that matches the node has all the components = 0
  for i in range (len(A)):
    if A[vertice][i] ==1:
      
      ##Case no universal sink
      print("No hay un sumidero universal")
      return
  ##Case universal sink
  print("Hay un sumidero universal")
  print(vertice)


##Aux. function Complexity: O(n)
def det_vertice(A):

  #Set of nodes of the graph
  set_vertices= set(range(len(A)))

  #Create a variable with same value as the node with higher value of the set
  i=len(set_vertices) -1

  #Create a value with same value as the node with lower value of the set: 0
  j=0


  #While there is more than one node on the set:

  #(Al tomar j el valor 0 e i el valor mayor posible, nunca va a presentar errores de OutOfBound)
  while len(set_vertices)>1:

    #Remove i if the entry is 1
    if A[i][j] == 1:
      set_vertices.remove(i)
      #Actualize var i
      i = i -1

    #Remove j if the entry is 0
    else:
      set_vertices.remove(j)
      #Actualize j
      j= j+1
  return set_vertices
