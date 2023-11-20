import tkinter as tk
from tkinter import messagebox

# Criar uma lista vazia para armazenar os livros
catalogo = []

# Adicionar livros -------------------------------------------------------------------------------------------


def adicionar_livro(): # Função adicionar livros

    # Criar uma subjanela janela para adicionar livros

    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x350")
    newWindow.title("Adicionar livros")
    newWindow.configure(bg=corf)

    # Pedir ao bibliotecario para inserir detalhes do livro

    # Titulo 
    tk.Label(newWindow, bg=corf, fg='white', text="Título:").pack()  # Adicionando o rótulo 'Título'
    titulo = tk.Entry(newWindow) # adicionar a caixa para escrever dentro
    titulo.pack()

    # Autor 
    tk.Label(newWindow, bg=corf, fg='white', text="Autor:").pack()  # Adicionando o rótulo 'Autor'
    autor = tk.Entry(newWindow) 
    autor.pack()

    #ISBN
    tk.Label(newWindow, bg= corf, fg='white', text="ISBN:").pack()  # Adicionando o rótulo 'ISBN'
    isbn = tk.Entry(newWindow)
    isbn.pack()

    #Status
    tk.Label(newWindow, bg= corf, fg='white', text="Status:").pack()  # Adicionando o rótulo 'Status'
    status = tk.Entry(newWindow) # criando a caixa de texto
    status.pack()

    # Criando outra função na qual vai armazenar as informações colocadas acima 
    def armazenar_info():

        # Criando um dicionário para armazenar as informações do livro

        livro = {"titulo": titulo.get(), "autor": autor.get(),"isbn": isbn.get(), "status": status.get()}

        # Adicionando o dicionario "livro" a lista "catálogo"

        catalogo.append(livro)

        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
        newWindow.destroy()
    
    # adicionando o botao para confirmar as informaçoes adicionadas 
    submit_button = tk.Button(newWindow, text="Registrar", command=armazenar_info)
    submit_button.place(x=120, y=185)

# Remover livros ----------------------------------------------------------------------------------------------------


def remover_livro():

    # Criar uma nova janela
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x200")
    newWindow.title("Remover livros")
    newWindow.configure(bg=corf)

    # Pedir ao bibliotecário para inserir detalhes do livro

    tk.Label(newWindow, bg= corf, fg='white', text="Digite o nome do livro").pack() # Adiciona o rótulo 'Digite o nome do livro'
    titulo = tk.Entry(newWindow) # criar a caixa de texto
    titulo.pack()

    def procura_remover():

        # Procurar o livro no catálogo

        for livro in catalogo: # fazendo um loop onde vai percorre cada livro dentro do catalogo

            # Ira verificar se o título do livro atual no loop é igual ao título que foi fornecido no dicionario
            if livro["titulo"] == titulo.get(): 

                # Remover o livro do catálogo
                catalogo.remove(livro)
                messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
                break
        else:
            messagebox.showinfo("Erro", "Livro não encontrado no catálogo.")
        newWindow.destroy()
   
    # adicionando um botao para remover o livro no catalogo
    submit_button = tk.Button(newWindow, text="Remover", command=procura_remover)
    submit_button.place(x=120,y=50)
    

# Verificar status de um livro -----------------------------------------------------------------------


def status_livro():

    # Criar uma nova janela
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x350")
    newWindow.title("Verificar status dos livros")
    newWindow.configure(bg=corf)

    # Fazendo um loop onde vai pecorrer o catalogo onde i é o índice que começa em 1 e livro é o valor de cada item na lista.

    for i, livro in enumerate(catalogo, start=1): # usando uma função "enumerate" onde indica que a contagem do índice deve começar em 1.
        label = tk.Label(newWindow, bg=corf, fg= 'white', text=f"{i}. {livro['titulo']} por {livro['autor']} - Status: {livro['status']}")
        label.pack()


# Janela principal --------------------------------------------------------------------------

corf = '#808080' # cinza claro 

root = tk.Tk()
root.geometry("300x350")
root.title("Biblioteca")
root.configure(bg=corf)

# Adicionar uma título

label = tk.Label(root, font=('Roboto 16 bold'), bg=corf, fg='white',  text="Bem-vindo bibliotecario(a)!")
label.place(x=7, y=10)

# Adicionar um subtitulo

label = tk.Label(root, bg=corf, fg='white', font=('Roboto 9 bold'), text="Escolha uma das opçoes:")
label.place(x=7, y=50)

# Botões

button1 = tk.Button(root, text="Adicionar livros", command=adicionar_livro, width=20)
button1.place(x=70, y=105)

button2 = tk.Button(root, text="Remover livros", command=remover_livro, width=20)
button2.place(x=70, y=145)

button3 = tk.Button(root, text="Verificar status dos livros", command=status_livro, width=20)
button3.place(x=70, y=185)

# Adicionar um botão para sair
button4 = tk.Button(root, text="Sair", command=root.destroy) # root.destroy fecha a janela principal quando clicado
button4.place(x=130, y=225)

root.mainloop()