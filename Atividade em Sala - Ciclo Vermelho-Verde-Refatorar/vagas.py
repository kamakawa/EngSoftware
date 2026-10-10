"""
PADRÃO: Strategy
  Context           -> Vaga
  Strategy          -> RegraVaga (interface)
  ConcreteStrategy  -> RegraVagaLivre, RegraVagaReservada, RegraVagaOcupada
"""
from abc import ABC, abstractmethod


class RegraVaga(ABC):
    @abstractmethod
    def pode_estacionar(self, usuario): ...

    @abstractmethod
    def mensagem(self, usuario): ...


class RegraVagaLivre(RegraVaga):
    def pode_estacionar(self, usuario):
        return True

    def mensagem(self, usuario):
        return "Vaga disponível"


class RegraVagaReservada(RegraVaga):
    def pode_estacionar(self, usuario):
        return usuario == "funcionario"

    def mensagem(self, usuario):
        if self.pode_estacionar(usuario):
            return "Vaga disponível"
        return "Vaga reservada para funcionários"


class RegraVagaOcupada(RegraVaga):
    def pode_estacionar(self, usuario):
        return False

    def mensagem(self, usuario):
        return "Vaga ocupada"


class Vaga:
    def __init__(self, tipo, ocupada=False):
        self.tipo = tipo
        self.ocupada = ocupada

    def _regra(self):
        if self.ocupada:
            return RegraVagaOcupada()
        if self.tipo == "reservada":
            return RegraVagaReservada()
        return RegraVagaLivre()

    def pode_estacionar(self, usuario):
        return self._regra().pode_estacionar(usuario)

    def mensagem(self, usuario):
        return self._regra().mensagem(usuario)


# AUTOAVALIAÇÃO
# - Critérios atingidos:
#   1) Plano no topo do teste: casos, padrão, tempos e uso de IA preenchidos. Atingido.
#   2) Três commits, um por fase (red, green, refactor): atingido, com a
#      autoavaliação incluída no commit de refactor (opção A sugerida no roteiro).
#   3) Commit red contém só o teste (e o .gitignore), sem vagas.py: atingido.
#   4) Padrão nomeado no topo do arquivo (Context -> Vaga, Strategy -> RegraVaga,
#      ConcreteStrategy -> RegraVagaLivre/Reservada/Ocupada): atingido.
#   5) resultado_testes.txt gerado com "7 passed": atingido.
# - O que mudou entre a fase verde e a refatorada:
#   Na fase verde, pode_estacionar() e mensagem() repetiam a mesma lógica de
#   if/else para decidir o comportamento de cada tipo de vaga. Na refatoração,
#   essa lógica foi dividida em classes de regra (RegraVagaLivre,
#   RegraVagaReservada, RegraVagaOcupada), e a Vaga passou a apenas escolher
#   qual regra usar (_regra()) e delegar a ela. Os testes não mudaram, só a
#   estrutura interna.
# - Parte que deu mais trabalho:
#   Entender o padrão Strategy, principalmente a diferença entre a classe
#   abstrata RegraVaga (o "contrato" que toda regra precisa seguir) e as
#   classes concretas que implementam cada comportamento, e por que isso é
#   melhor do que simplesmente manter os ifs dentro de Vaga.
# - Uso de IA:
#   Ajudou a estruturar o roteiro (plano, fases red/green/refactor), a sugerir
#   os casos de teste e o código da versão com Strategy, além de executar os
#   comandos de pytest e git nesta sessão. Atrapalhou em alguns pontos que
#   precisaram de atenção manual: por exemplo, ao limpar o __pycache__ para a
#   fase red, a IA quase removeu arquivos .pyc que já estavam versionados no
#   repositório (de outros módulos do projeto) e precisou restaurá-los antes
#   de continuar — ou seja, mesmo usando IA, foi preciso revisar cada git
#   status antes de confirmar um commit.
