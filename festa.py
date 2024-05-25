def pessoa():
    nome = input("digite o seu nome :")
    print(f"Olá {nome}")
    return nome

def responsavel():
    adulto = input('você esta com um responsavel? s/n')
    return adulto

def maior_idade():
    try:
        idade = int(input("digite sua idade: "))
        if idade >= 18:
            print("pode entrar na festa")
        elif idade < 18 and idade >= 15 :
            print('menor de idade , só com responsavel')
            if responsavel() == "s":
                print("pode entrar na festa com o responsavel legal ")
            else:
                print('NÃO PODE ENTRAR NA FESTA ')
        elif idade <= 14 :
            print("NÃO PODE ENTRAR NA FESTA , MUITO NOVO")
            
    except ValueError:
        print("digite algo valido")

def festa():
    pessoa()
    maior_idade()
    

festa()

