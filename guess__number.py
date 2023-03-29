import random
import math
print("Algoritimo desenvolvido para a brincadeira adivinhe o número")
lower = int(input("Digite o limite do menor número:- ")) 
 
upper = int(input("Digite o limite do maior número:- "))  
 
x = random.randint(lower, upper)
print("\n\tVocê tem apenas ", round(math.log(upper - lower + 1, 2))," chances de acertar o inteiro!\n")
 
 
count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1
     
     
    guess = int(input("Adivinhe o número:- ")) 
     
    
    if x == guess:  
       print("Parabéns você adivinhou em ", count, " tentativas")
       
       break
    elif x > guess:
       print("Número muito pequeno!")
    elif x < guess:
       print("Número muito grande!")
 
if count >= math.log(upper - lower + 1, 2):
   print("\nO número é %d"%x)
   print("\tMais sorte da próxima vez!")