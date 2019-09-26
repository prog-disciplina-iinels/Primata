from numpy import random as rd
def Habituado(habituado = 1):
    return True if habituado == 1 else False

def EtapaUm(habituado, aproximacaoTotal):
    
    agua = 0
     
   if (aprox > 30) or (aprox < 0):
            print("Valor de distancia inválido")
        return False
    else:
        distancia = 30
        distancia =distancia -  aprox
        if distancia == 0:
            agua = 0.5
            print("O animal toca a barra")
            
   
    return [agua, True]
    if(not Habituado(habituado)):
        print("O animal não está habituado")
      return False
   def Etapa2(habituado, som, lado,aprox, minut):
              agua = 0.0
          if len(som) != len(lado):
            print("As listas devem ter tamanhos iguais")
        return False
         if(not Habituado(habituado)):
            print("O animal não está habituado")
        return False
         if(EtapaUm(habituado, aprox)):
              for i in range(len(som)):
                if((som[i] and lado[i]) or (not som[i] and not lado[i])):
                agua=agua +0.5
             if(minut >= 30):
                print("O animal realizou todas as fases")
            return True
              else:
            print("O animal não realizou a última fase no tempo hábil")
                