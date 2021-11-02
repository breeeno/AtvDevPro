
pop_a = float(input('A população do país A é de '))    #população A
pop_b = float(input('A população do país B é de '))  #população B
taxa_a = float(input('A taxa de crescimento do país A é de '))    #taxa A
taxa_b = float(input('A taxa de crescimento do país B é de '))   #taxa B
ano = 0          #anos gastos
while pop_a <= pop_b:
    pop_a += round(pop_a * taxa_a)/100  #Multiplicar população pela taxa de crescimento
    pop_b += round(pop_b * taxa_b)/100
    ano += 1                     #Sempre adicionar mais um ano até obter o resultado necessário

if pop_a > pop_b:
     print(f'No ano {ano},a população de A superou a população de B.') #Printar os resultados obtidos
     print(f'A população de A será de {pop_a}')
     print(f'A população de B será de {pop_b}')