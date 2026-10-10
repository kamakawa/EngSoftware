class Vaga:
    def __init__(self, tipo, ocupada=False):
        self.tipo = tipo
        self.ocupada = ocupada

    def pode_estacionar(self, usuario):
        if self.ocupada:
            return False
        if self.tipo == "reservada":
            return usuario == "funcionario"
        return True

    def mensagem(self, usuario):
        if self.ocupada:
            return "Vaga ocupada"
        if self.tipo == "reservada" and usuario != "funcionario":
            return "Vaga reservada para funcionários"
        return "Vaga disponível"
