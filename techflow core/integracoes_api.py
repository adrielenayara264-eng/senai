
# TECHFLOW CORE - INTEGRACOES COM APIS EXTERNAS

import urllib.request
import json


def consultar_cep(cep):
    """Consulta um CEP utilizando a API ViaCEP."""

    cep = ''.join(c for c in str(cep) if c.isdigit())

    if len(cep) != 8:
        print("Erro: CEP deve conter 8 números.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        with urllib.request.urlopen(url, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))

        if dados.get("erro"):
            print("CEP não encontrado.")
            return None

        print("\n--- ENDEREÇO ENCONTRADO ---")
        print(f"CEP: {dados.get('cep')}")
        print(f"Logradouro: {dados.get('logradouro')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')}")
        print(f"Estado: {dados.get('uf')}")

        return dados

    except Exception as erro:
        print(f"Erro ao consultar ViaCEP: {erro}")
        return None


def consultar_cotacao_dolar():
    """Consulta a cotação atual do dólar pela AwesomeAPI."""

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        with urllib.request.urlopen(url, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))

        cotacao = dados["USDBRL"]

        print("\n--- COTAÇÃO DO DÓLAR ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Compra: R$ {cotacao['bid']}")
        print(f"Venda: R$ {cotacao['ask']}")
        print(f"Variação: {cotacao['pctChange']}%")

        return cotacao

    except Exception as erro:
        print(f"Erro ao consultar AwesomeAPI: {erro}")
        return None
