#!/usr/bin/env python
# coding: utf-8

# # Primatas
#     Entradas:
#         -habituado: indicar se o animal está ou não habituado
#          type:bool
#         -aproximacaoTotal: quanto foi a aproximação do animal em relação à barra
#          type:int
#         -listaSom: lista com os sons escutados pelo animal. Valores de cada elemento: 1, equivalendo ao som 1 ou 0 equivalendo ao som 2
#         -type:list
#         -listaLado: lista com os lados escolhidos pelo animal. Valores de cada elemento: 1, equivalendo ao lado Esquerdo ou 0 equivalendo ao lado direito
#         -type:list
#     Saídas:
#         True - o experiemento foi um sucesso
#         False - ocorreu algum erro durante a execução do mesmo

from numpy import random as rd

def EstaHabituado(habituado = 1):
    return True if habituado == 1 else False

def PrimeiraEtapa(habituado, aproximacaoTotal):
    
    agua = 0
    
    if(not EstaHabituado(habituado)):
        print("O animal não está habituado")
        return False
    
    if (aproximacaoTotal > 30) or (aproximacaoTotal < 0):
        print("Valor de aproximação inválido")
        return False
    else:
        distancia = 30
        distancia -= aproximacaoTotal
        
        if distancia == 0:
            agua = 0.5
            print("O animal toca a barra")
            
            return [agua, True]
    return [agua, True]

def SegundaEtapa(habituado, aproximacaoTotal, listaSom, listaLado, tempo):
    
    agua = 0.0
    
    if(not EstaHabituado(habituado)):
        print("O animal não está habituado")
        return False
    
    if len(listaSom) != len(listaLado):
        print("As listas precisam ter o mesmo tamanho")
        return False
    if(PrimeiraEtapa(habituado, aproximacaoTotal)[1]):
        for i in range(len(listaSom)):
            if((listaSom[i] and listaLado[i]) or (not listaSom[i] and not listaLado[i])):
                agua += 0.5
                
        print("O animal recebeu %i ml de água" %agua)
        if(tempo >= 30):
            print("O animal conseguiu realizar todas as etapas")
            return True
        else:
            print("O animal não terminou a última etapa em tempo hábil")
            


# ### Exemplo de execução

SegundaEtapa(1, 30, [1, 1, 1], [1, 1, 1], 50)

