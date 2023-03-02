from random import randint


class Jogo:
    tentativas = 0
    numero = 0
    

class JogoInterface(Jogo):
    def gerar_numero_aleatorio(cls) -> None:
        cls.numero = randint(1, 1000)
    
    def incrementar_tentativas(cls) -> None:
        cls.tentativas += 1 