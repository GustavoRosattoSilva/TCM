h1 = float(input("Digite o h do Fluido quente:\n"))
h2 = float(input("Digite o h do Fluido frio:\n"))
temp1 = float(input("Digite a temperatura do Fluido quente:\n"))
temp2 = float(input("Digite o temperatura do Fluido frio:\n"))
n = int(input("Digite de materiais da parede:\n"))
k = []
l = []
rcont = []

for i in range(1,n+1):
	print('Digite o k do material ' + str(i) + ':')
	b = float(input())
	k.append(b)
	print('Digite a espessura do material ' + str(i) + ':')
	jh = float(input())
	l.append(jh)

for i in range(1,n):
	print('Digite a resistencia de contato ' + str(i) + ':')
	jbs = float(input())
	rcont.append(jbs)

h1 = 1/h1
h2 = 1/h2

for x in range(0, len(k)):
	k[x] = l[x]/k[x]

dt = temp1 - temp2
resis = []
resis.append(h1)
i = 0

while k != []:
	if i%2 == 0:
		resis.append(k.pop(0))
	else:
		resis.append(rcont.pop(0))
	i+=1

resis.append(h2)
req = sum(resis)
q = dt/req
temperatura = [temp1]

for x in range(0,2*n):
	temperatura.append(temperatura[len(temperatura)-1] - resis[x]*q)

temperatura.append(temp2)
print(resis)
print('fluxo igual: ' + str(q))
print(temperatura)
