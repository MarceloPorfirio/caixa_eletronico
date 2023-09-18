import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CaixaEletronico():
    saldo = 0
    
    def VerSaldo(self):
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo < valor:
            return False, f'Saldo indisponível para saque, saldo disponível: {self.saldo}'
        else:
            self.saldo -= valor
            return True, f'Seu novo saldo é: {self.saldo}'
    
    def depositar(self, valor):
        self.saldo += valor
        return f'Seu novo saldo é: {self.saldo}'

def limpar_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def update_saldo_saque(saque):
    saldo_atual = cx.VerSaldo()
    if saldo_atual >= 0:
        saldo_pos_label.config(text=f"Seu saldo atual é: {saldo_atual}", fg="green")
    else:
        saldo_neg_label.config(text=f"Seu saldo atual é: {saldo_atual}", fg="red")
    
    deposito_label.config(text=f"Saque no valor de R$ {saque}.\nEfetuado com sucesso.")

def janela_saque():
    
    # Criação da nova janela
    janela = tk.Toplevel(root)
    janela.title("Saque")
    janela.geometry('300x150')

    # Label de instrução
    instrucao_label = tk.Label(janela, text="Digite o valor a ser sacado:")
    instrucao_label.pack()

    # Entry para inserir o valor do saque
    valor_entry = tk.Entry(janela)
    valor_entry.pack()

    def confirmar_saque():
       saldo_atual = cx.VerSaldo()
       valor = int(valor_entry.get())
       mensagem = cx.sacar(valor)
       if saldo_atual < valor:
           messagebox.showinfo("Saque", 'Saldo Insuficiente')
       else: 
            update_saldo_saque(valor)   
            valor_entry.delete(0, tk.END)
            janela.destroy()

        
    # Botão de confirmação de saque
    sacar_button = tk.Button(janela, text="Confirmar", command=confirmar_saque)
    sacar_button.pack()

     
def update_saldo_deposito(deposito):
    saldo_atual = cx.VerSaldo()
    if saldo_atual >= 0:
        saldo_pos_label.config(text=f"Seu saldo atual é: {saldo_atual}", fg="green")
    else:
        saldo_neg_label.config(text=f"Seu saldo atual é: {saldo_atual}", fg="red")
    
    deposito_label.config(text=f"Depósito no valor de R$ {deposito}.\nEfetuado com sucesso.")
# Deposito
def janela_deposito():
    
    # Criação da nova janela
    janela = tk.Toplevel(root)
    janela.title("Depósito")
    janela.geometry('300x150')
    
    # Label de instrução
    instrucao_label = tk.Label(janela, text="Digite o valor a ser depositado:")
    instrucao_label.pack()

    # Entry para inserir o valor do depósito
    valor_entry = tk.Entry(janela)
    valor_entry.pack()
    def confirmar_deposito():
        valor = int(valor_entry.get())
        mensagem = cx.depositar(valor)
        update_saldo_deposito(valor)
        valor_entry.delete(0, tk.END)
        janela.destroy()

    # Botão de confirmação de depósito
    depositar_button = tk.Button(janela, text="Confirmar", command=confirmar_deposito)
    depositar_button.pack()


            
# Configuração da interface gráfica
root = tk.Tk()
root.title("Simulador de Caixa Eletrônico")
root.geometry('900x600')

# Carregue a imagem de fundo usando PIL
bg_image = Image.open("Caixa-Eletronico.jpg")
bg_image = bg_image.resize((900, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Widgets por cima da imagem
frame = tk.Frame(root,width=430,height=190,background='white')
frame.place(relx=0.12,rely=0.15)

frame2 = tk.Frame(root,width=430,height=50,background='white')
frame2.place(relx=0.12,rely=0.615)

deposito_label = tk.Label(frame, text="",font=('Helvetica',14),bg='white')
deposito_label.place(relx=0.05,rely=0.02)

saldo_pos_label = tk.Label(frame2, text="",font=('Helvetica',14),bg='white',fg='green')
saldo_pos_label.place(relx=0.05,rely=0.02)

saldo_neg_label = tk.Label(frame2, text="",font=('Helvetica',14),bg='white',fg='red')
saldo_neg_label.place(relx=0.05,rely=0.02)



depositar_button = tk.Button(root, text="Deposito", command=janela_deposito,font=('Roboto',16))
depositar_button.place(relx=0.67,rely=0.15,relwidth=0.202,relheight=0.06)

sacar_button = tk.Button(root, text="Saque",command=janela_saque,font=('Roboto',16))
sacar_button.place(relx=0.67,rely=0.224,relwidth=0.202,relheight=0.06)

ver_saldo_button = tk.Button(root, text="Consultar \n Saldo",font=('Roboto',16))
ver_saldo_button.place(relx=0.67,rely=0.292,relheight=0.12,relwidth=0.202)



cx = CaixaEletronico()

root.mainloop()
