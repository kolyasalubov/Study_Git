a=int(input("Input the number a="))
b=int(input("Input the number b="))
if a <= b:
    min, max = a, b
else:
    min, max = b, a

st="The number a={0} is minimal number, the number b={1} is maximum number".format(min, max)
print(st)
