class Pessoa:

    data_nascimento: str = ''
    nome: str = ''
    cpf: str = ''

    def __init__(self, data_nascimento, nome, cpf) -> None:
        self.data_nascimento = data_nascimento
        self.nome = nome
        self.cpf = cpf
        pass

class Funcionario(Pessoa):

    data_admissao: str = ''
    salario: float = 0.0

    def __init__(self, data_nascimento, nome, cpf, data_admissao, salario) -> None:
        super().__init__(data_nascimento, nome, cpf)

        self.data_admissao = data_admissao
        self.salario = salario

class Cliente(Pessoa):

    ultima_visita: str = ''
    saldo: float = 0.0

    def __init__(self, data_nascimento, nome, cpf, ultima_visita, saldo) -> None:
        super().__init__(data_nascimento, nome, cpf)

        self.ultima_visita = ultima_visita
        self.saldo = saldo

p = Pessoa('08-04-2000', 'Fulano, 11111111111')
print(p)
    