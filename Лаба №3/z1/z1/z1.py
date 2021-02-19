from random import randint
import sys
x = int(input('Введите количество раз '))
c=0
v=0
if x>0:
	for i in range(1, x+1):
		b = randint(1,101)
		if b>50:
			c+=1
		else:
			v+=1
print(c, 'раз(а) выпала Решка')
print(v, 'раз(а) выпал Орел')
if x<0 or x==0:
	print('Неправильно введены данные!')
