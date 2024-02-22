import pymongo

m = 0
n = 0
R = 0

def menu():
    escolha = str(input("Deseja realizar alguma operação?\n[ S ] - Sim\n[ N ] - Não\nEscolha: ")).upper()
    if (escolha == "S"):
        op = int(input("Qual operação você deseja fazer?\n[ 1 ] - Soma\n[ 2 ] - Substração\nEscolha: "))
        m = int(input("Digite um número: "))
        n = int(input("Digite outro número: "))
        if op == 1:
            R = m + n
        else:
            R = m - n
            
        print("\nResultado: ", R)
        menu()
    else:
        return
   
print("OPERAÇÕES\n")    
menu()

