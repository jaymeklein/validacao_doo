from tkinter import *

class gui:
    janela_cliente = False
    janela_veiculo = False
    janela_vendedor = False
    lista_clientes = []
    
    
    def iniciar_janela_clientes(self) -> None:
        if not self.janela_cliente:
            self.janela_cliente = True
            janela_clientes = Toplevel()
            janela_clientes.protocol("WM_DELETE_WINDOW",
                                    lambda: self.fechar(janela_clientes,
                                                        'cliente'))
            janela_clientes.geometry('300x200')
            janela_clientes.title('Clientes')
            janela_clientes.resizable(width=False, height=False)
            
            Label(janela_clientes, text='Lista de Clientes').pack(anchor='w')
            listbox = Listbox(janela_clientes)
            listbox.pack(anchor='w')
            
            entry = Entry(janela_clientes)
            entry.pack(anchor='e')
                       
            valor = entry.get()
            
            adicionar_cliente = Button(janela_clientes, text='Adicionar Cliente',
                                       command=lambda: self.adicionar_no_listbox(listbox,
                                                                                 entry.get()))
            adicionar_cliente.pack(anchor='se')


    
    def fechar(self, janela: Toplevel, nome_janela:str) -> None:
        if nome_janela == 'cliente':
            self.janela_cliente = False
        
        elif nome_janela == 'veiculo':
            self.janela_veiculo = False
            
        elif nome_janela == 'vendedor':
            self.janela_vendedor = False
            
        janela.destroy()
        
    def iniciar(self) -> None:
        
        root = Tk()
        root.title('')
        root.geometry('400x150')
        root.resizable(width=False, height=False)
        padding = {'ipadx': 10, 'ipady': 15}
        
        Label(root, text="Eu tenho um número entre 1 e 1000, você pode adivinhá-lo?").pack(**padding)
        
        botao_iniciar = Button(root, text='Iniciar', width=30,
                                command=self.iniciar_janela_clientes)
        botao_iniciar.pack(**padding)
        
        root.mainloop()
    
    

if __name__ == '__main__':
    gui().iniciar()
    