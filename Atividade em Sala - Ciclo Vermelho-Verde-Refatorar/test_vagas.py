"""
PLANO (10 min)
Casos a testar:
  - Vaga livre comum: aluno e funcionário podem estacionar
  - Vaga reservada a funcionários: aluno não pode, funcionário pode
  - Vaga ocupada: ninguém pode, mesmo que reservada
Padrão escolhido: Strategy. As três variações são regras de decisão
diferentes para a mesma pergunta; Strategy remove a duplicação de condicionais
entre pode_estacionar() e mensagem() e permite novas regras sem alterar Vaga.
IA: Usei IA (Claude) para sugerir os casos de teste, a implementação inicial
com condicionais (fase green) e o refactor para Strategy; revisei o código
gerado, executei a suíte em cada fase e conduzi os commits manualmente.
"""
import pytest
from vagas import Vaga


def test_aluno_pode_estacionar_em_vaga_livre_comum():
    vaga = Vaga(tipo="comum")
    assert vaga.pode_estacionar("aluno") is True
    assert vaga.mensagem("aluno") == "Vaga disponível"


def test_aluno_nao_pode_estacionar_em_vaga_reservada():
    vaga = Vaga(tipo="reservada")
    assert vaga.pode_estacionar("aluno") is False
    assert vaga.mensagem("aluno") == "Vaga reservada para funcionários"


def test_funcionario_pode_estacionar_em_vaga_reservada():
    vaga = Vaga(tipo="reservada")
    assert vaga.pode_estacionar("funcionario") is True


@pytest.mark.parametrize("tipo", ["comum", "reservada"])
@pytest.mark.parametrize("usuario", ["aluno", "funcionario"])
def test_ninguem_estaciona_em_vaga_ocupada(tipo, usuario):
    vaga = Vaga(tipo=tipo, ocupada=True)
    assert vaga.pode_estacionar(usuario) is False
    assert vaga.mensagem(usuario) == "Vaga ocupada"
