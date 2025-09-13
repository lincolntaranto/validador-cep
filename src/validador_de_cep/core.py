import json
import requests

class Validador_de_cep():
    def __init__(self) -> None:
        pass

    def verificar_cep_na_api(self, cep):

        """
        Verifica a validade de um CEP consultando a API ViaCEP.

        Args:
            cep (int): O CEP a ser verificado.

        Returns:
            dict: Um dicionário com os dados do CEP caso seja válido.
            str: Retorna "Invalido" se o CEP não existir.
            None: Retorna None em caso de erro na requisição à API.
        """

        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()
            if "erro" in dados:
                return "Invalido"
            else:
                return dados
        except requests.exceptions.RequestException as e:
            print(f"Erro ao chamar API: {e}")
            return None
    
    def imprimir_cep(self, cep):

        """
        Imprime as informações do CEP fornecido.

        Args:
            cep (dict): Um dicionário contendo os dados do CEP retornados pela API ViaCEP.

        Returns:
            None
        """
        
        print(f"Cep: {cep["cep"]}")
        print(f"Logradouro: {cep["logradouro"]}")
        print(f"Complemento: {cep["complemento"]}")
        print(f"Bairro: {cep["bairro"]}")
        print(f"UF: {cep["uf"]}")
        print(f"Estado: {cep["estado"]}")


def main():
    teste = Validador_de_cep()
    cep = int(input("Entrada: "))
    dados = teste.verificar_cep_na_api(cep)
    if dados == "Invalido":
        print("CEP invalido!")
    elif dados:
        print("CEP Valido!")
        teste.imprimir_cep(dados)
    else:
        print("CEP invalido!")

if __name__ == "__main__":
    main()