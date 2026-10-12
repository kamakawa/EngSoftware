"""Calculadora de frete (versão verde: implementação direta com if/elif)."""


def calcular_frete(modalidade, peso_kg):
    if peso_kg <= 0:
        raise ValueError("O peso deve ser maior que zero.")

    if modalidade == "economico":
        return 5.00 + 2.00 * peso_kg
    elif modalidade == "expresso":
        return 15.00 + 3.50 * peso_kg
    elif modalidade == "retirada":
        return 0.00
    else:
        raise ValueError(f"Modalidade desconhecida: {modalidade}")