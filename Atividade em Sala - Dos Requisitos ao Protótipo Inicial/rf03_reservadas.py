def identificar_vagas_reservadas():
    """Implementa o RF03: identificação das vagas reservadas para funcionários."""

    # Dados simulados apenas para o protótipo.
    vagas = {
        "A01": "aluno",
        "A02": "funcionário",
        "A03": "aluno",
        "B01": "funcionário",
        "B02": "aluno",
    }

    reservadas = [
        vaga for vaga, tipo in vagas.items()
        if tipo == "funcionário"
    ]

    if reservadas:
        print(f"Vagas reservadas para funcionários: {', '.join(reservadas)}")
        print("Essas vagas não devem ser consideradas vagas comuns para alunos.")
    else:
        print("Não há vagas reservadas cadastradas.")
