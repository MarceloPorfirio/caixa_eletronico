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

# Funções para interagir com a interface gráfica
def depositar():
    valor = int(valor_entry.get())
    mensagem = cx.depositar(valor)
    saldo_label.config(text=mensagem)
    messagebox.showinfo("Sucesso", "Deposito realizado com sucesso. Confira seu novo saldo.")
    update_saldo_display()
    valor_entry.delete(0, tk.END)  # Limpa o conteúdo do Entry
def sacar():
    valor = int(valor_entry.get())
    sucesso, mensagem = cx.sacar(valor)
    if sucesso:
        saldo_label.config(text=mensagem)
        messagebox.showinfo("Sucesso", "Saque realizado com sucesso. Confira seu novo saldo.")
        update_saldo_display()
        valor_entry.delete(0, tk.END)  # Limpa o conteúdo do Entry
        
    else:
        messagebox.showerror("Erro", mensagem)

def update_saldo_display():
    saldo_atual = cx.VerSaldo()
    saldo_disponivel_label.config(text=f"Saldo disponível: {saldo_atual}")

def ver_saldo():
    saldo = cx.VerSaldo()
    saldo_label.config(text=f"Seu saldo atual é: {saldo}")

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
frame = tk.Frame(root,width=430,height=190)
frame.place(relx=0.12,rely=0.15)
saldo_disponivel_label = tk.Label(root, text="Saldo disponível: 0")
saldo_disponivel_label.pack()

valor_label = tk.Label(frame, text="Digite o valor e execute a ação desejada:",font=('Roboto',12))
valor_label.place(relx=0.12,rely=0.05)

valor_entry = tk.Entry(frame,font=('Roboto',12))
valor_entry.place(relx=0.12,rely=0.2,relheight=0.2,relwidth=0.65)

depositar_button = tk.Button(root, text="Deposito", command=depositar,font=('Roboto',16))
depositar_button.place(relx=0.67,rely=0.15,relwidth=0.202,relheight=0.06)

sacar_button = tk.Button(root, text="Saque", command=sacar,font=('Roboto',16))
sacar_button.place(relx=0.67,rely=0.224,relwidth=0.202,relheight=0.06)

ver_saldo_button = tk.Button(root, text="Consultar \n Saldo", command=ver_saldo,font=('Roboto',16))
ver_saldo_button.place(relx=0.67,rely=0.292,relheight=0.12,relwidth=0.202)

saldo_label = tk.Label(root, text="Seu saldo atual é: 0")
saldo_label.pack()

cx = CaixaEletronico()

root.mainloop()
