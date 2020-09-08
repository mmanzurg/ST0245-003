def euclides(p,q,iteracciones=1):

    if p<q:
        p,q=p,q

    resto=p%q

    if resto==0:
        return (q,iteracciones)

    return euclides(q,resto,iteracciones+1)

p=60
q=48

comunDivisor,iteracciones=euclides(p,q)

print("El comun divisor de {} y {} es {}".format(p,q,comunDivisor))
print("Se ha encontrado en {} iteracciones".format(iteracciones))

def gcd_euclid(p, q):
    if (q==0):
        return p
    return gcd_euclid(q,p%q)


print(gcd_euclid(60, 48))

def Suma_grupo(start, nums, target):
    if (start>=len(nums)):
        return target==0;
    return Suma_grupo(start+1,nums, target-nums[start]) or Suma_grupo(start+1,nums,target)


print(Suma_grupo(0,[2, 4, 8],10))

def combinations(s):
    combinationsAux("",s)

def combinationsAux(base, t):
    if(t==""):
        print(base)
    else:
        combinationsAux(base + t[0], t[1:])
        combinationsAux(base, t[1:])
print(combinations("abcd"))
