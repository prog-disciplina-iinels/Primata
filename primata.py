from numpy import random as rd 

habituacao = 0

som = 0
lado = 0

agua = 0
tentativa = 0

tempo = 0

while(not habituado):
   habituado = rd.randint(2)

print("O animal está habituado")
distancia = 30
aproximacao = 0

for i in range(20):
   
   aproximacao = rd.randint(0, 31)
   
   if aproximacao > 30 or aproximacao < 0:
      continue
   
   distancia -= aproximacao
   
   if distancia == 0:
      agua = 0.5
      print("O animal toca a barra")
      break

print("O animal está pronto para a proxima etapa")
agua = 0
tentativa = 0

for i in range(50):

   som = rd.randint(2)
   lado = rd.randint(2)
   
   if((som and lado) or (not som and not lado)):
      agua += 0.5

print("O animal recebeu %i ml de água" %agua)
tempo = int(input("Duração da última etapa (em minutos)? "))

if(tempo >= 30):
   print("O animal conseguiu realizar todas as etapas")
else: 
   print("O animal não terminou a última etapa em tempo hábil")
   
