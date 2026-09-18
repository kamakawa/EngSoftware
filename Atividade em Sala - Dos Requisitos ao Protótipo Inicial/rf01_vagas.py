def visualizar_vagas_disponiveis():
    """Implementa o RF01: visualização das vagas disponíveis."""

    # Dados simulados apenas para o protótipo.
    # O mecanismo real de obtenção das vagas ainda não foi definido pelo cliente.
    vagas = {
        "A01": "disponível",
        "A02": "ocupada",
        "A03": "disponível",
        "A04": "ocupada",
        "A05": "disponível",
    }

    disponiveis = [vaga for vaga, status in vagas.items()
                   if status == "disponível"]

    if disponiveis:
        print(f"Vagas disponíveis: {', '.join(disponiveis)}")
    else:
        print("Não há vagas disponíveis.")
