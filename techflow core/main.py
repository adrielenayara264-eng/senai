
# TECHFLOW CORE - ARQUIVO PRINCIPAL

from gerenciador_demandas import menu
from utils import limpar_tela, exibir_cabecalho


def main():
    """Inicia o sistema TechFlow Core."""
    limpar_tela()
    exibir_cabecalho()
    menu()


if __name__ == "__main__":
    main()
