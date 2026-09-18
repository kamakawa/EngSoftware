# ATIVIDADE EM SALA - DOS REQUISITOS AO PROTÓTIPO INICIAL
#
# Requisitos escolhidos:
# 1. RF01 - Visualização das vagas disponíveis
# 2. RF03 - Identificação das vagas reservadas

from rf01_vagas import visualizar_vagas_disponiveis
from rf04_reservadas import identificar_vagas_reservadas

def main():
    print("Atividade em Sala - Dos Requisitos ao Protótipo Inicial")
    print("Aluno: Eric Kamakawa")

    # RF01
    print("\nRF01 - Visualização das vagas disponíveis")
    visualizar_vagas_disponiveis()

    # RF03
    print("\nRF04 - Identificação das vagas reservadas")
    identificar_vagas_reservadas()

    print("Protótipo executado com sucesso.")


if __name__ == "__main__":
    main()

