'''
Nome: Clarissa Cruz
Data: 28/10/2027
Versão 1
'''
#Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante. 

letra = input('Digite uma letra: ') .strip().lower()

if letra in ('a', 'e', 'i', 'o', 'u'):
    print('Essa letra é uma vogal')
else:
    print ('Essa letra é uma consoante')