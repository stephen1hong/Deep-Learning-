import numpy as np
# write a function that takes as input a list of numbers 
# and return the list of vlaues given by the softmax functions
def softmax(L):
  sum=0
  for i in range(len(L)):
    sum +=np.exp(L[i]) 
  v=[]
  for i in range(Len(L)):
    v.append(np.exp(L[i])/sum)
  return v
