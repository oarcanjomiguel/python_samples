import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
delta = (b**2) - (4*a*c)
if(delta >= 0):
	x1 = (-1*b + math.sqrt(delta)) / (2*a)
	x2 = (-1*b - math.sqrt(delta)) / (2*a)
	if(delta == 0):
		print("x1 e x2:",x1)
	else:
		print("x1:", x1)
		print("x2:", x2)
else:
	print("raízes imaginárias")