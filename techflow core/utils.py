
import os


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """Exibe o cabeçalho principal do sistema."""
    print("=" * 40)
    print("       SISTEMA TECHFLOW CORE")
    print("=" * 40)


def validar_texto(texto):
    """Verifica se o texto não está vazio."""
    return isinstance(texto, str) and bool(texto.strip())


def validar_prioridade(prioridade):
    """Verifica se a prioridade informada é válida."""
    prioridades_validas = ["baixa", "normal", "alta", "urgente"]

    return (
        isinstance(prioridade, str)
        and prioridade.strip().lower() in prioridades_validas
    )


def formatar_cep(cep):
    """Formata o CEP no padrão 00000-000."""
    numeros = ''.join(
        caractere for caractere in str(cep)
        if caractere.isdigit()
    )

    if len(numeros) != 8:
        return None

    return f"{numeros[:5]}-{numeros[5:]}"
