import requests
from urllib3 import request
import pytest
from unittest.mock import patch, Mock

from src.validador_de_cep.core import Validador_de_cep

def test_verificar_cep_na_api():

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"cep": "01001-000", "logradouro": "Praça da Sé"}

    with patch("src.validador_de_cep.core.requests.get", return_value = mock_response):
        testador = Validador_de_cep()
        resultado = testador.verificar_cep_na_api("01001000")
        assert isinstance(resultado, dict)

def test_verificar_cep_na_api_404():

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Erro 404")

    with patch("src.validador_de_cep.core.requests.get", return_value = mock_response):
        testador = Validador_de_cep()
        resultado = testador.verificar_cep_na_api("00000000")
        assert resultado is None

def test_verificar_cep_na_api_invalido():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"erro": "true"}

    with patch("src.validador_de_cep.core.requests.get", return_value = mock_response):
        testador = Validador_de_cep()
        resultado = testador.verificar_cep_na_api("11111111")
        assert resultado == "Invalido"