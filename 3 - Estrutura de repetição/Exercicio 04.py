#Pais a cresce 3% ao ano com população menor, 80000 * (3/100) = 2400 habitantes por ano
#Pais b cresce 1.5% ao ano com população maior, 200000 * (1,5/100) = 3000 habitantes por ano


pop_a = 80000    #população A
pop_b = 200000   #população B
taxa_a = 1.03    #taxa A
taxa_b = 1.015   #taxa B
ano = 0          #anos gastos
while pop_a <= pop_b:
    print(f'######## População no ano {ano}')
    print(f'A população de A: {pop_a}')
    print(f'A população de B: {pop_b}')
    pop_a = int(pop_a * taxa_a)  #Multiplicar população pela taxa de crescimento
    pop_b = int(pop_b * taxa_b)
    pop_b = int(pop_b)
    ano += 1                     #Sempre adicionar mais um ano até obter o resultado necessário

if pop_a > pop_b:
     print(f'No ano {ano},a população de a superou a população de b.') #Printar os resultados obtidos
