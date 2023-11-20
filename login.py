import tkinter as tk
from tkinter import messagebox
import subprocess

# -----------------------------------------------------------------------   BACK - END ------------------------------------------------------------------------------------------

# Função para verificar o nome de usuário e a senha

def verificar_login():

# Verificar se o usuário e senha do ALUNO ESTÃO CERTOS --------------------------------------------

    if usuario.get() == 'zezin' and senha.get() == '12345':
        messagebox.showinfo(title="Login Info", message="Login bem sucedido!")

        # Fechar a janela de login
        janela.destroy()

        # Abrir o novo sistema
        subprocess.call(["python", "Sistema_a.py"])

    else:
         messagebox.showinfo(title="Login Info", message="Nome ou senha incorretos!")


# ----------------------------------------------------------------------- fRONT - END ------------------------------------------------------------------------------------------

# Criando a janela ----------------------------------------

cor1 = '#000921'  # azul escuro
cor2 = '#808080' # cinza suave

janela = tk.Tk()
janela.title("Login de Usuário")
janela.geometry("300x200")
janela.configure(bg=cor1)

# Criar variáveis para o nome de usuário e a senha ------------------------------

usuario = tk.StringVar()
senha = tk.StringVar()

# Criar os campos de entrada para o nome de usuário e a senha ---------------------------------------------------------

tk.Label(janela, text="Nome de usuário", font=('Roboto 10 bold'), height=2, bg=cor1, fg='white').pack()
tk.Entry(janela, textvariable=usuario).pack()

tk.Label(janela, text="Senha", font=('Roboto 10 bold'), height=2, bg=cor1, fg='white').pack()
tk.Entry(janela, textvariable=senha, show='*').pack() # o '' foi usado para mascara a senha e aparecer somente o *

# Criar o botão de login que chama a função verificar_login -----------------------------------------------------------

tk.Button(janela, text="Entrar",font=('Roboto 10 bold'), bg=cor1, fg= 'white', command=verificar_login).pack(pady=20)

janela.mainloop()