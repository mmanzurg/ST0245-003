import sys
from time import time
sys.setrecursionlimit(1000000000)
def secMax(str1,str2):
  if len(str1)==0 or len(str2)==0:
    return 0
  if str1[len(str1)-1]==str2[len(str2)-1]:
    return 1 + secMax(str1[:len(str1)-1], str2[:len(str2)-1])
  return max(secMax(str1[:len(str1)-1], str2), secMax(str1, str2[:len(str2)-1]))

start = time()
(secMax("abcdgh", "aedfhr"))
final=time()-start
print(final)
start = time()
(secMax("axyt", "ayzx"))
final=time()-start
print(final)
start = time()
(secMax("abcdgh", "aedfhr"))
final=time()-start
print(final)
start = time()
(secMax("aggtab", "gxtxayb"))
final=time()-start
print(final)
start = time()
(secMax("axyt", "ayzx"))
final=time()-start
print(final)
start=time()
(secMax("gctagcgt","aaagcata"))
final=time()-start
print(final)
start = time()
(secMax("gatgttaag","ccctagaca"))
final=time()-start
print(final)
start = time()
(secMax("ttaagatgagc","ccgcaggcaca"))
final=time()-start
print(final)
start = time()
(secMax("gc","ta"))
final=time()-start
print(final)
start=time()
(secMax("taaa","cata"))

final=time()-start
print(final)
start=time()
(secMax("ttaagatgagcg","ccgcaggcacat"))

final=time()-start
print(final)
start=time()
(secMax("ttaagatgagcgg","ccgcaggcacata"))

final=time()-start
print(final)
start=time()
(secMax("ttaagatgagcggt","ccgcaggcacatag"))

final=time()-start
print(final)
start=time()
(secMax("aggtab", "gxtxayb"))

final=time()-start
print(final)
start=time()
(secMax("aggtab", "gxtxayb"))

final=time()-start
print(final)
start=time()
(secMax("aggtabt","gxtxaybg"))

final=time()-start
print(final)
start=time()
(secMax("gctagcgt","ccctagac"))

final=time()-start
print(final)
start=time()
(secMax("axytt", "ayzxy"))

final=time()-start
print(final)
start = time()
(secMax("gcg","taa"))
start = time()
(secMax("gcgg","taat"))
final = time()-start
print(final)

def area(n):
    if(n<=2):
      return n
    return area(n-1) + area(n-2)

def tiempo():
   for i in range(20, 40):
     inicio = time()
     area(i)
     tiempo = time() - inicio
     print(tiempo)
