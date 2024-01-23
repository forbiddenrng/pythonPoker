def mergeSort(lista):
  if len(lista)<=1:
    return lista
  
  middleIndex = len(lista)//2
  leftList=lista[:middleIndex]
  rightList=lista[middleIndex:]

  leftList=mergeSort(leftList)
  rightList=mergeSort(rightList)

  return merge(leftList, rightList)


def merge(lista1, lista2):
  output=[]
  index1, index2= 0,0 

  while index1<len(lista1) and index2 < len(lista2):
    if lista1[index1][0][0] < lista2[index2][0][0]:
      output.append(lista1[index1])
      index1+=1
    else:
      output.append(lista2[index2])
      index2+=1

  if index1==len(lista1):
    output.extend(lista2[index2:])
  elif index2==len(lista2):
    output.extend(lista1[index1:])  
  
  return output


