import datetime

class Paciente:
    def __init__(self, nome, nascimento, altura, peso, genero, id=None):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.altura = altura
        self.peso = peso
        self.genero = genero

    def calcular_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))
        return idade

    def calcular_imc(self):
        return self.peso / (self.altura * self.altura)

    def calcular_tmb(self):
        idade = self.calcular_idade()
        altura_cm = self.altura * 100
        if self.genero == 'M':
            return (10 * self.peso) + (6.25 * altura_cm) - (5 * idade) + 5
        else:
            return (10 * self.peso) + (6.25 * altura_cm) - (5 * idade) - 161
