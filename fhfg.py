verif= []
s=0
i=0
cli=0
p=0
editar=0
while True:
    try:
        while True:

            print("1-Cadastrar o usuario")
            print("2-listar")
            print("3-Editar")
            print("4-Excluir")
            print("0-sair")
            p=int(input('Escolha 1,2,3,4 ou 0: ')) 
            if p==1:
               verif.append(input('Cadastre:'))
               s+=1
            elif p==3:
                if(verif._len_()==0):
                    print("não a nada na lista")
                try:
                    editar=int(input("Digite o numero do cadastro a ser editado"))
                    editar=editar-1
                    verif[editar]=input("Digite o usuario a ser cadastrado")
                except (ValueError,IndexError):
                    print("Erro! porfavor Digite um numero E um numero referente a um cadastro existente \n\n")
            elif p==0:
                break
            elif p==2:
                if(verif.__len__g()==0):
                    print("não a nada na lista")
                for i in range(0,len(verif)):
                    cli= cli+1
                    print("Cadastro",cli," :")
                    print(verif[i])
            elif p==4:
                if(verif.__len__()==0):
                    print("não a nada na lista Para ser excluido")
                else:
                    print("\n\nDigite um desses numeros a frente do nome cadastro pra ser excluido")
                    for j in range(0,s):
                        print( "cadastro",j,verif[j])
                    try:
                        excl=int(input("Digite o numero do cadastro a ser excluido"))-1
                        del verif[excl]
                        print("Excluido com sucesso")
                    except ValueError:
                        print("Numero invalido")

            else:
                print("Digite o numero 1,2 ou 3")
        break
    except ValueError:
        print('Digite somente uma das opções a seguir:  a opção 1,2,3,4 ou 0')