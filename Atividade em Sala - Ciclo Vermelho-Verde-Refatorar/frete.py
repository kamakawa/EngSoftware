"""
Calculadora de frete (versão refatorada)

PADRÃO DE PROJETO: Strategy

Participantes, nomeados conforme o domínio:
  - Strategy (interface):      EstrategiaFrete
        Define o contrato calcular(peso_kg)
  - ConcreteStrategies:        FreteEconomico, FreteExpresso, FreteRetirada
        Cada uma implementa uma regra de cálculo de frete
  - Context:                   CalculadoraFrete
        Recebe a modalidade, escolhe a estratégia correspondente e
        delega o cálculo a ela

Por que Strategy aqui: o if/elif da fase verde misturava todas as regras
em uma função. Agora cada modalidade fica isolada e novas modalidades
entram registrando uma nova classe, sem modificar as existentes
"""
from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):
    """Strategy: contrato comum a todas as modalidades de frete."""

    @abstractmethod
    def calcular(self, peso_kg):
        ...


class FreteEconomico(EstrategiaFrete):
    """ConcreteStrategy: R$ 5,00 fixos + R$ 2,00 por kg"""

    def calcular(self, peso_kg):
        return 5.00 + 2.00 * peso_kg


class FreteExpresso(EstrategiaFrete):
    """ConcreteStrategy: R$ 15,00 fixos + R$ 3,50 por kg"""

    def calcular(self, peso_kg):
        return 15.00 + 3.50 * peso_kg


class FreteRetirada(EstrategiaFrete):
    """ConcreteStrategy: retirada na loja, sem custo"""

    def calcular(self, peso_kg):
        return 0.00


class CalculadoraFrete:
    """Context: escolhe a estrategia pela modalidade e delega o cálculo"""

    def __init__(self):
        self._estrategias = {
            "economico": FreteEconomico(),
            "expresso": FreteExpresso(),
            "retirada": FreteRetirada(),
        }

    def calcular(self, modalidade, peso_kg):
        if peso_kg <= 0:
            raise ValueError("O peso deve ser maior que zero")
        estrategia = self._estrategias.get(modalidade)
        if estrategia is None:
            raise ValueError(f"Modalidade desconhecida: {modalidade}")
        return estrategia.calcular(peso_kg)


def calcular_frete(modalidade, peso_kg):
    """Função de fachada: mantém a API usada pelos testes"""
    return CalculadoraFrete().calcular(modalidade, peso_kg)