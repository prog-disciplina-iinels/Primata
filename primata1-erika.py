habituado = bool(input("O animal está habituado?: "))
print(input("quantas vezes tocou a barra?: "))
som1= bool(input("som1 emitido?: "))
som2= bool(input("som2 emitido? e tocou  barra direita?: "))
if(habituado==True):
    aprox=30
    print(input("quanto se aproximou?"))
    if(aprox < 30):
     print ("0.5L para o animal")
else:
     print("nao esta habituado")
if(barra>=20):
  print("o animal passou para a proxima etapa")
if(som1==True):
 print("liberar 0.5L de agua")
 else:
     print("nao liberar nada")
if (som2==True and barradireita==True):
    print ("liberar 0.5 agua")