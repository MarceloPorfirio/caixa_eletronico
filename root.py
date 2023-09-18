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

class MinhaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Caixa Eletrônico")
        self.root.geometry('900x600')

        # Carregue a imagem de fundo usando PIL
        bg_image = Image.open("Caixa-Eletronico.jpg")
        bg_image = bg_image.resize((900, 600), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Widgets por cima da imagem
        self.frame = tk.Frame(self.root, width=430, height=190, background='white')
        self.frame.place(relx=0.12, rely=0.15)

        self.saldo_disponivel_label = tk.Label(self.root, text="Saldo disponível: 0")
        self.saldo_disponivel_label.pack()

        valor_label = tk.Label(self.frame, text="Digite o valor e execute a ação desejada:", font=('Roboto', 12))
        valor_label.place(relx=0.12, rely=0.05)

        self.valor_entry = tk.Entry(self.frame)
        self.valor_entry.place(relx=0.12, rely=0.2, relwidth=0.75, relheight=0.2)

        depositar_button = tk.Button(self.root, text="Deposito", command=self.depositar, font=('Roboto', 16))
        depositar_button.place(relx=0.67, rely=0.15, relwidth=0.202, relheight=0.06)

        sacar_button = tk.Button(self.root, text="Saque", command=self.sacar, font=('Roboto', 16))
        sacar_button.place(relx=0.67, rely=0.224, relwidth=0.202, relheight=0.06)

        ver_saldo_button = tk.Button(self.root, text="Consultar \n Saldo", command=self.ver_saldo, font=('Roboto', 16))
        ver_saldo_button.place(relx=0.67, rely=0.292, relheight=0.12, relwidth=0.202)

        self.saldo_label = tk.Label(self.root, text="Seu saldo atual é: 0")
        self.saldo_label.pack()

        self.cx = CaixaEletronico()

    def depositar(self):
        valor = float(self.valor_entry.get())
        mensagem = self.cx.depositar(valor)
        self.saldo_label.config(text=mensagem)
        messagebox.showinfo("Sucesso", "Depósito realizado com sucesso. Confira seu novo saldo.")
        self.update_saldo_display()
        self.valor_entry.delete(0, tk.END)  # Limpa o conteúdo do Entry

    def sacar(self):
        valor = float(self.valor_entry.get())
        sucesso, mensagem = self.cx.sacar(valor)
        if sucesso:
            self.saldo_label.config(text=mensagem)
            messagebox.showinfo("Sucesso", "Saque realizado com sucesso. Confira seu novo saldo.")
            self.update_saldo_display()
            self.valor_entry.delete(0, tk.END)  # Limpa o conteúdo do Entry
        else:
            messagebox.showerror("Erro", mensagem)

    def ver_saldo(self):
        saldo = self.cx.VerSaldo()
        self.saldo_label.config(text=f"Seu saldo atual é: {saldo}")

    def update_saldo_display(self):
        saldo_atual = self.cx.VerSaldo()
        self.saldo_disponivel_label.config(text=f"Saldo disponível: {saldo_atual}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MinhaApp(root)
    root.mainloop()
