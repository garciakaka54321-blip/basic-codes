import random
sorte = int(input('Digite um numero de 1 a 10: '))
numero = random.randint(1, 10)
if sorte == numero:
    print('Parabéns você acertou o número!')
else:
    print (f'VOcê errou o número, o número correto era: {numero}')
    