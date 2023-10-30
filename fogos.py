# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
print ("Os fogos iniciam em: ")
contagem= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for fogos in contagem:
    time.sleep(1)     
    print (fogos)
print("FELIZ ANO NOVO!!!")