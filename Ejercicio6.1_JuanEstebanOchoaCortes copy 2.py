def negate(num):
   return -num


b= int(input()) ##(en la funcion original no pide ninguna variable)
neg_b= negate(b) ##(en la funcion original [neg_b = num] cuando deberia ser [=negate(b)])
print ("b: ", b, "negate_b: ", negate)


##
##


def large_num(num):
   res = (num>10000)
   return res   ##(en la funcion orignal no retorna ningun caracter o valor)
xde = large_num(b)
print ("b is big",xde)


