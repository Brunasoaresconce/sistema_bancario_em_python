menu = '''
[1]deposita 
[2]sacar
[3]extrato
[4]sair'''

saldo=500
limite=500
deposito=0
extrato=""
numero_saques=0
limite_de_saques=3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor=float(input("digite o valor que deseja deposita: "))

        if valor >= 0:
            saldo+=valor
            extrato+= f"deposito R${valor:.2f}\n"
        else:
            print("operção falhou")

            

    elif opcao == "2":
        valor=float(input("digite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo   

        excedeu_liminte = valor > limite

        excedeu_saques = numero_saques >=limite_de_saques
    

        if excedeu_liminte:
            print("não foi possivel realizar o saque pois não ha saldo o suficiente")
    
        elif excedeu_saldo:
            print( "não foi possivel realizar o saque pois seu saldo e insuficiente")

        elif excedeu_saques:
            print("não foi possivel realizar o saque pois seu numero de saque diario excedeu")

        elif valor>0:
            saldo -= valor
            extrato == f"saque no valor de  R${valor:.2f}"
            numero_saques +=1
        else:
            print("operação ecerrada")
    elif opcao == "3":
        print("\n=================extrato================")
        print("não foram realizadas movimentações"if not extrato else extrato)
        print(f"\nSaldo: R${saldo}")
        print("===========================================")
    elif opcao == "4":
        break
    else:
        print("numero invalido por favor digite novamente.")
