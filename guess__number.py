#Aqui importamos as bibliotecas random(para gerar o número aleatório) e math(para as operações matemáticas):
import random
import math

print("Algoritimo desenvolvido para a brincadeira adivinhe o número")

#Definindo as variáveis input dos limites entre o número:
menor = int(input("Digite o limite do menor número:- "))  
maior = int(input("Digite o limite do maior número:- ")) 
 
 #Aqui utilizamos a função randint que é uma função em Python que gera um valor aleatório entre dois valores inteiros: 
x = random.randint(menor, maior)

print("\n\tVocê tem apenas ", round(math.log(maior - menor + 1, 2))," chances de acertar o inteiro!\n")
 
 
contador = 0

while contador < math.log(maior - menor + 1, 2):
    contador += 1
     
     
    adivinhe = int(input("Adivinhe o número:- ")) 
     
    
    if x == adivinhe:  
       print("Parabéns você adivinhou em ", contador, " tentativas")
       
       break
    elif x > adivinhe:
       print("Número muito pequeno!")
    elif x < adivinhe:
       print("Número muito grande!")
 
if contador >= math.log(maior - menor + 1, 2):
   print("\nO número é %d"%x)
   print("\tMais sorte da próxima vez!")