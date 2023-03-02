from tkinter import *
from tkinter import NS
from sys import exit
from jogo import JogoInterface
from tkinter import messagebox

class gui:
    janela_chute = False
    janela_erro = False

        
    def iniciar(self) -> None:
        self.root = root = Tk()
        root.title('')
        root.geometry('400x150')
        root.resizable(width=False, height=False)
        padding = {'ipadx': 10, 'ipady': 15}
        
        Label(root, text="Eu tenho um número entre 1 e 1000, você pode adivinhá-lo?").pack(**padding)
        
        botao_iniciar = Button(root, text='Iniciar', width=30,
                                command=self.iniciar_janela_inicio)
        self.jogo = JogoInterface()
        botao_iniciar.pack(**padding)
        
        root.mainloop()
    
    def iniciar_janela_inicio(self) -> None:
        if not self.janela_chute:
            padding = {'ipadx': 10, 'ipady': 15}
            
            self.janela_chute = True
            self.jogo.tentativas = 0
            self.jogo.gerar_numero_aleatorio()

            self.janela_inicio = janela_inicio = Toplevel()
            janela_inicio.protocol("WM_DELETE_WINDOW",
                                    lambda: self.fechar(janela_inicio,
                                                        'chute'))
            janela_inicio.geometry('300x300')
            janela_inicio.resizable(width=False, height=False)
            
            l = Label(janela_inicio, text='Entre com seu chute:')
            l.place(relx=0.5, rely=0.15, anchor=CENTER)
            
            self.chute_entry = chute_entry = Entry(janela_inicio, justify='center')
            chute_entry.place(relx=0.5, rely=0.24, anchor=CENTER)
            
            self.texto_resultado = Label(janela_inicio, text="")
            
            self.chutar = chutar = Button(janela_inicio, text='Chutar!',
                                       command=lambda: self.validar_chute(chute_entry.get()))
            chutar.place(relx=0.5, rely=0.35, anchor=CENTER)
    
    def fechar(self, janela: Toplevel, nome_janela:str) -> None:
        if nome_janela == 'chute':
            self.janela_chute = False
        
        elif nome_janela == 'erro':
            self.janela_erro = False
            
        janela.destroy()
    
    def validar_chute(self, valor_chute:str) -> None:
        print(self.jogo.numero)
        
        if not self.janela_erro:
            self.jogo.incrementar_tentativas()
            self.chute_entry["state"] = "normal"
            self.chutar["state"] = "normal"
            
            try:
                valor_chute = int(valor_chute)
                
            except ValueError:
                if not self.janela_erro:
                    messagebox.showerror("", "Valor Inválido!")
                return
            
            if valor_chute > self.jogo.numero and valor_chute <= 1000:
                self.janela_inicio.configure(background='red')
                self.texto_resultado.config(text="O número correto está abaixo!")
                self.texto_resultado.place(relx=0.5, rely=0.48, anchor=CENTER)
                
            elif valor_chute < self.jogo.numero and valor_chute >= 0:
                self.janela_inicio.configure(background='blue')
                self.texto_resultado.config(text="O número correto está acima!")
                self.texto_resultado.place(relx=0.5, rely=0.48, anchor=CENTER)
            
            elif valor_chute == self.jogo.numero:
                self.janela_inicio.configure(background='green')
                self.chute_entry["state"] = "disabled"
                self.chutar["state"] = "disabled"
                self.texto_resultado.config(text="Parabéns, você acertou!")
                self.texto_resultado.place(relx=0.5, rely=0.48, anchor=CENTER)
                
                texto_tentativas = Label(self.janela_inicio,
                                         text=f"Tentativas: {self.jogo.tentativas}")
                texto_tentativas.place(relx=0.5, rely=0.57, anchor=CENTER)
                
                botao_sair = Button(self.janela_inicio,
                                    text="Sair",
                                    command=lambda: self.sair())
                botao_sair.place(relx=0.1, rely=0.9, anchor=SW)
                
                botao_novamente = Button(self.janela_inicio,
                                         text="Jogar Novamente",
                                         command=lambda: self.jogar_novamente())
                botao_novamente.place(relx=0.9, rely=0.9, anchor=SE)
                
            else:
                messagebox.showerror("", "Valor Inválido!")
    
    def jogar_novamente(self) -> None:
        self.janela_erro = False
        self.janela_chute = False
        self.janela_inicio.destroy()
    
    def sair(self) -> None:
        exit()
        

if __name__ == '__main__':
    gui().iniciar()
    