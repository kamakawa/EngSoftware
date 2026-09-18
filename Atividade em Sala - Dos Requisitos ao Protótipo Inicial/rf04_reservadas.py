def identificar_vagas_reservadas():
    """Implementa o RF04: identificação das vagas reservadas para funcionários."""
    """ N4 — Vagas reservadas
        Alunos ocupam algumas vagas reservadas para funcionários, principalmente nas
        proximidades da biblioteca, e o cliente gostaria que o sistema ajudasse a evitar essa
        situação.
        Trecho relacionado: “os alunos às vezes estacionam em vagas reservadas para
        funcionários, principalmente perto da biblioteca”"""

    # Dados simulados apenas para o protótipo
    # Pretendo gastar 15 minutos
    # IA para tirar dúvidas
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
