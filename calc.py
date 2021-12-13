import re

print("Bem-vindo a super calculadora")
print("Digite 'sair ' para sair\n")

run =True
prev=0
def perfMath():
    global run
    global prev
    equa = input("introduza o nr: ")
    if equa == 'sair':
         run = False
    else: 
        prev = eval(equa)
        print("o nr introduzido foi", prev)

while run:
    perfMath()



    '''import re

# calculadora melhorada nao aceita a entrada de espacoes e nem de letras somento numeros 

print("Bem-Vindo a super calculadora".title())
print("digite ' sair ' quando desejar sair da calc\n".title())

run=True

while run:

    def fun_math():
        global run
        global prev
    equal = input("introduza o valor: ".title())
   
    if equal == 'sair':
        run = False
    else:
        equal =re.sub( '[a-zA-Z,.:()" "]', '',equal)
        print(" Ate a proxima idiota")
        
        prev = eval(equal)
        print("O Resultado e", prev)
'''
