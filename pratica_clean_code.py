
# Constantes do sistema
PRIORIDADE_URGENTE = 3
PRIORIDADE_NORMAL = 2
PRIORIDADE_BAIXA = 1

PRAZO_URGENTE = 1
PRAZO_NORMAL = 3


def calcular_prioridade_e_prazo(tipo_prioridade, dias_prazo):
    if tipo_prioridade == "urgente":
        prioridade = PRIORIDADE_URGENTE
    elif tipo_prioridade == "normal":
        prioridade = PRIORIDADE_NORMAL
    else:
        prioridade = PRIORIDADE_BAIXA

    if dias_prazo <= PRAZO_URGENTE:
        prazo = "Hoje"
    elif dias_prazo <= PRAZO_NORMAL:
        prazo = "Em até 3 dias"
    else:
        prazo = "Mais de 3 dias"

    return prioridade, prazo


# Lista de chamados
chamados = [
    ("urgente", 1),
    ("normal", 3),
    ("baixa", 5)
]


# Exibição dos resultados
for chamado in chamados:
    tipo_prioridade, dias_prazo = chamado

    prioridade, prazo = calcular_prioridade_e_prazo(
        tipo_prioridade,
        dias_prazo
    )

    print(f"Prioridade: {prioridade} | Prazo: {prazo}")
