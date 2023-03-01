# -*- coding: utf-8 -*-
"""classes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cy3qbzz1AYZSsTNiBjhuNB8DlXqMsJPw
"""

class Pessoa:

    data_nascimento: str = ''
    nome: str = ''
    cpf: str = ''

    def __init__(self, data_nascimento, nome, cpf) -> None:
        self.data_nascimento = data_nascimento
        self.nome = nome
        self.cpf = cpf

    def __str__(self) -> str:
      return f'Nome: {self.nome}\n'\
             f'CPF: {self.cpf}\n'\
             f'Data de Nascimento: {self.data_nascimento}'

class Funcionario(Pessoa):

    data_admissao: str = ''
    salario: float = 0.0

    def __init__(self, data_nascimento, nome, cpf,
                 data_admissao, salario) -> None:
        super().__init__(data_nascimento, nome, cpf)
        self.data_admissao = data_admissao
        self.salario = salario
      
    def __str__(self) -> str:
      return f'Nome: {self.nome}\n'\
             f'CPF: {self.cpf}\n'\
             f'Data de Nascimento: {self.data_nascimento}\n'\
             f'Data Admissão: {self.data_admissao}\n'\
             f'Salário: {self.salario}'

class Cliente(Pessoa):

    ultima_visita: str = ''
    saldo: float = 0.0

    def __init__(self, data_nascimento, nome, cpf,
                 ultima_visita, saldo) -> None:
        super().__init__(data_nascimento, nome, cpf)
        self.ultima_visita = ultima_visita
        self.saldo = saldo
      
    def __str__(self) -> str:
      return f'Nome: {self.nome}\n'\
             f'CPF: {self.cpf}\n'\
             f'Data de Nascimento: {self.data_nascimento}\n'\
             f'Data Última Visita: {self.ultima_visita}\n'\
             f'Saldo: {self.saldo}'

p = Pessoa('08-04-2000', 'Fulano', '11111111111')
print(p)
print('\n')

f = Funcionario('08-04-2000', 'Fulano 2', '22222222222', '01-01-2022', 5000.0)
print(f)
print('\n')

class Veiculo:
  fabricante: str = ''
  ano_fabricacao: str = ''
  codigo_fabricante: int = 0

  def __init__(self, fabricante, ano_fabricacao, codigo_fabricante):
    self.fabricante = fabricante
    self.ano_fabricacao = ano_fabricacao
    self.codigo_fabricante = codigo_fabricante

class Carro(Veiculo):
  placa: str = ''
  modelo: str = ''
  cor: str = ''
  
  def __init__(self, fabricante, ano_fabricacao,
               codigo_fabricante, placa, modelo, cor):
    self.fabricante = fabricante
    self.ano_fabricacao = ano_fabricacao
    self.codigo_fabricante = codigo_fabricante
    self.placa = placa
    self.modelo = modelo
    self.cor = cor