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
    
    def adicionar_no_listbox(self, listbox, valor) -> None:
        index = len(listbox)
        listbox.insert(index+1, valor)
    
        
    def inciar_janela_veiculos(self) -> None:
        if not self.janela_veiculo:
            self.janela_veiculo = True
            janela_veiculos = Toplevel()
            janela_veiculos.protocol("WM_DELETE_WINDOW",
                                     lambda: self.fechar(janela_veiculos,
                                                         'veiculo'))
            janela_veiculos.geometry('300x200')
            janela_veiculos.title('Veículos')
            janela_veiculos.resizable(width=False, height=False)
        
    def iniciar_janela_vendedores(self) -> None:
        if not self.janela_vendedor:
            self.janela_vendedor = True
            janela_vendedores = Toplevel()
            janela_vendedores.protocol("WM_DELETE_WINDOW",
                                       lambda: self.fechar(janela_vendedores,
                                                           'vendedor'))
            janela_vendedores.geometry('300x200')
            janela_vendedores.title('Vendedores')
            janela_vendedores.resizable(width=False, height=False)
    
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
        root.title('Menu Principal')
        root.geometry('300x200')
        root.resizable(width=False, height=False)
        padding = {'ipadx': 10, 'ipady': 10}
        
        Label(root, text="Menu Principal").pack(**padding)
        
        botao_clientes = Button(root, text='Clientes', width=30,
                                command=self.iniciar_janela_clientes)
        botao_clientes.pack(**padding)
        
        botao_veiculos = Button(root, text='Veículos', width=30,
                                command=self.inciar_janela_veiculos)
        botao_veiculos.pack(**padding)
        
        botao_vendedores = Button(root, text='Vendedores', width=30,
                                  command=self.iniciar_janela_vendedores)
        botao_vendedores.pack(**padding)
        
        root.mainloop()
    
    

if __name__ == '__main__':
    gui().iniciar()
    