"""
PLANO (Passo 1)

Problema: calculadora de frete para uma loja virtual.

Casos que serão testados:
  1. Modalidade "economico": R$ 5,00 fixos + R$ 2,00 por kg.
  2. Modalidade "expresso":   R$ 15,00 fixos + R$ 3,50 por kg.
  3. Modalidade "retirada":   frete sempre R$ 0,00.
  4. Peso inválido (zero ou negativo) levanta ValueError.
  5. Modalidade desconhecida levanta ValueError.

Padrão de projeto escolhido: Strategy.
Por quê: cada modalidade é uma regra de cálculo diferente e intercambiável.
Na fase verde usarei if/elif; na refatoração cada regra vira uma estratégia,
permitindo adicionar modalidades sem modificar o código existente
(princípio Aberto/Fechado).

Tempo por fase (120 min):
  - Plano:            10 min
  - Red:               8 min
  - Green:             7 min  
  - Refactor:         30 min
  - Autoavaliação:    10 min
  - Folga/envio:      15 min

Uso de IA:Usei o Claude para sugerir a estrutura dos testes
e revisar a refatoração; o código e os commits foram feitos por mim.
"""
import pytest

from frete import calcular_frete


def test_frete_economico_cobra_fixo_mais_valor_por_kg():
    assert calcular_frete("economico", 2) == pytest.approx(9.00)


def test_frete_expresso_cobra_fixo_mais_valor_por_kg():
    assert calcular_frete("expresso", 2) == pytest.approx(22.00)


def test_frete_retirada_e_sempre_gratuito():
    assert calcular_frete("retirada", 10) == pytest.approx(0.00)


@pytest.mark.parametrize("peso", [0, -1])
def test_peso_invalido_levanta_erro(peso):
    with pytest.raises(ValueError):
        calcular_frete("economico", peso)


def test_modalidade_desconhecida_levanta_erro():
    with pytest.raises(ValueError):
        calcular_frete("teletransporte", 1)