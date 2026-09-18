def visualizar_vagas_disponiveis():
    
    """Implementa o RF01: visualização das vagas disponíveis."""
    """ N1 — Disponibilidade de vagas
        Os alunos têm dificuldade para saber onde existem vagas disponíveis, principalmente
        durante o horário de pico da manhã.
        Trecho relacionado: “é muito difícil saber onde há vagas disponíveis, principalmente durante
        o horário de pico da manhã”"""
        
    # Dados simulados apenas para o protótipo
    # O mecanismo real de obtenção das vagas ainda não foi definido pelo cliente
    # Pretendo gastar uns 10 minutos
    # Pretendo usar a IA apenas para quando travar no código 
    
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
