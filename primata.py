from random import randint
habituacao = bool(input("O animal está habituado: "))

som = 0
lado = 0

agua = 0
tentativa = 0

tempo = 0
tentativa1 = 0

while(not habituado):
       habituado = bool(2)

print("O animal se encontra habituado")
aprox = 30
dist1 = 0

for i in range(20):
       
   aproximacao = randint(0, 31)
   
   if aproximacao > 30 or aproximacao < 0:
      continue

    aprox = aprox - dist1
if aprox == 0:
      agua = 0.5
      print("O animal tocou a barra")
      break
print("O animal pasa para a proxima fase")

agua = 0
tentativa = 0

for i in range(50):

   som = randint(2)
   lado = randint(2)
   if(som and lado):
    agua += 0.5
   if (not som and not lado)):
    agua += 0.5   

    print("O animal recebeu "%agua" ml de água")
minut = int(input("Tempo da última etapa (minutos)? "))
if(minut >= 30):
       print("O animal  realizou todas as fases")
else: 
   print("O animal não realizou a última fase no tempo hábil")