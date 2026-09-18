# ATIVIDADE EM SALA - DOS REQUISITOS AO PROTÓTIPO INICIAL
#
# PLANO (5 minutos)
# Requisitos escolhidos:
# 1. RF01 - Visualização das vagas disponíveis
# 2. RF03 - Identificação das vagas reservadas
#
# Ordem de implementação:
# - RF01: 25 minutos
# - RF03: 25 minutos
#
# Os dois requisitos foram escolhidos porque permitem demonstrar o comportamento
# principal do aplicativo sem depender de sensores, banco de dados ou interface gráfica.
#
# Uso de IA:
# - A IA foi utilizada como apoio para estruturar o código, separar cada requisito
#   em seu próprio arquivo e revisar a aderência aos critérios da atividade.
# - A implementação foi revisada para não assumir decisões que o cliente não definiu.

from rf01_vagas import visualizar_vagas_disponiveis
from rf03_reservadas import identificar_vagas_reservadas


def main():
    print("=" * 55)
    print("PROTÓTIPO - ESTACIONAMENTO DO CAMPUS")
    print("=" * 55)

    # RF01
    print("\n[RF01] Visualização das vagas disponíveis")
    visualizar_vagas_disponiveis()

    # RF03
    print("\n[RF03] Identificação das vagas reservadas")
    identificar_vagas_reservadas()

    print("\n" + "=" * 55)
    print("Protótipo executado com sucesso.")
    print("=" * 55)


if __name__ == "__main__":
    main()


# AUTOAVALIAÇÃO (5 minutos)
#
# Critérios atingidos:
# 1. Lista dos requisitos implementados: SIM.
# 2. Cada requisito possui função própria em arquivo separado: SIM.
# 3. Existe um único ponto de entrada (main.py): SIM.
# 4. Histórico com pelo menos três commits: a realizar no Git conforme as etapas.
# 5. README com explicação, requisitos e execução: SIM.
# 6. Protótipo executa sem erro e apresenta no terminal o resultado de cada requisito: SIM.
#
# Requisito mais difícil:
# RF03 foi o mais difícil de traduzir porque o cliente disse que o sistema deveria
# ajudar a evitar o uso das vagas reservadas, mas não definiu se haveria bloqueio,
# notificação ou outra ação. Por isso, o protótipo apenas identifica as vagas
# reservadas, sem assumir um mecanismo adicional.
#
# Uso de IA:
# A IA ajudou na organização da estrutura do protótipo e na revisão dos critérios.
# Foi necessário revisar as sugestões para evitar decisões técnicas não informadas
# pelo cliente, especialmente sobre sensores, banco de dados e notificações.
