from .core import Validador_de_cep

def run():
    testador = Validador_de_cep()

    while True:
        print("""
            1. Verificar CEP
            2. Sair""")
        try:
            escolha = int(input("Entrada: "))
            if escolha == 1:
                try:
                    cep = int(input("Entrada: "))
                    dados = testador.verificar_cep_na_api(cep)
                    if dados == "Invalido":
                        print("CEP invalido!")
                    elif dados:
                        print("CEP Valido!")
                        testador.imprimir_cep(dados)
                    else:
                        print("CEP invalido!")
                except ValueError:
                    print("Digite apenas números!")
            if escolha == 2:
                break
            else:
                print("Escolha invalida!")           
        except ValueError:
            print("Digite apenas números!")


