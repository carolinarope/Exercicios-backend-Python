# - Criar 4 funções: soma(a,b), subtracao(a,b), multiplicacao(a,b), divisao(a,b)
# 
# - Cada função retorna o resultado
# 
# - Menu: escolher operação → pedir 2 números → mostrar resultado
# 
# - Validar divisão por zero (tentar dividir por 0 deve mostrar erro)

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b


print('--- CALCULADORA ---')

def menu ():

    while True:

        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Insira uma opção: ").strip()

        if opcao == "5":

            print('Encerrando Calculadora...')
            break

        if opcao in ["1","2","3","4"]:    

            a = int(input("Digite um número: ").strip())
            b = int(input("Digite outro número: ").strip()) 

            if opcao == "1":

                resultado = soma(a,b)
                print(f'O resultado de {a} + {b}: {resultado} ')
            
            elif opcao == "2":

                resultado = subtracao(a, b)
                print(f'O resultado de {a} - {b} é: {resultado}')

            elif opcao == "3":

                resultado = multiplicacao(a, b)
                print(f'O resultado de {a} * {b} é: {resultado}')
                
            elif opcao == "4":

                resultado = divisao(a, b)
                print(f'O resultado de {a} / {b} é: {resultado}')

        else:
           
           print("\033[31mOpção inválida! Tente novamente.\033[m")
           
         
menu()