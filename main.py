# Importando pymongo
import pymongo

# Calculadora

# declaração das variáveis

numero1 = 0
numero2 = 0
resultado = 0

# função menu de opções das operações

def menu():
    escolha = str(input("Deseja realizar alguma operação?\n[ S ] - Sim\n[ N ] - Não\nEscolha: ")).upper()
    if (escolha == "S"):
        opcao = int(input("Qual operação você deseja fazer?\n[ 1 ] - Soma\n[ 2 ] - Substração\nEscolha: "))
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite outro número: "))
        if opcao == 1:
            resultado = numero1 + numero2 #soma
        else:
            resultado = numero1 - numero2 #subtração
            
        print("\nResultado: ", resultado) #retorno da operação escolhida
        menu()
    else:
        return
   
print("OPERAÇÕES\n")    
menu() #chamada do método

