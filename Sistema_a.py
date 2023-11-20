import tkinter as tk
from tkinter import messagebox, simpledialog
from Sistema_p import catalogo
import datetime

# Criando uma lista vazia para armazenar os livros emprestados pelo aluno
livros_emprestados = []

# Solicitar empréstimo --------------------------------------------------------------------------------------------------------------------------------------------


def solicitar_emprestimo():
    

    # Perguntar se é aluno ou professor
    tipo_usuario = simpledialog.askstring("Solicitar Empréstimo", "Você é aluno ou professor?") 

    # usando a função  "simpledialog.askstring()" na qual vai abrir uma caixa de dialogo falando para o usuario inserir informações 
    
    # Definir o limite de empréstimos com base no tipo de usuário
    limite_emprestimos = 3 if tipo_usuario.lower() == "aluno" else 6
    
    # Abrindo outra caixa de dialogo 
    titulo_solicitado = simpledialog.askstring("Solicitar Empréstimo", "Insira o título do livro que deseja pegar:")
    
    # ira pecorrer cada livro dentro do loop catalogo
    for livro in catalogo:
         
        # ira verificar se o titulo do livro é igual ao titulo do livro que foi solicitado  e se o status desse livros estiver disponivel 
        if livro["titulo"] == titulo_solicitado and livro["status"] == "disponível":

            # ira verificar se o numero de livros emprestados for menor que o limite de emprestimos estabelecidos ele irar aprovar e mudar o status para "emprestado"
            if len(livros_emprestados) < limite_emprestimos:
                livros_emprestados.append(livro)
                livro["status"] = "emprestado"

                messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
                return True
            
    messagebox.showinfo("Erro", "Desculpe, não foi possível realizar o empréstimo.")
    return False


# Devolver livro ------------------------------------------------------------------------------------------------------------------------------------------------

def devolver_livro():
    # Perguntar se é aluno ou professor
    tipo_usuario = simpledialog.askstring("Devolver Livro", "Você é aluno ou professor?")
    
    # Definir o prazo de devolução com base no tipo de usuário
    prazo_devolucao = 5 if tipo_usuario.lower() == "aluno" else 10

    # abrindo uma caixa de dialogo perguntado qual livro o usuario quer devolver 

    titulo_devolvido = simpledialog.askstring("Devolver Livro", "Insira o título do livro que deseja devolver:")

    # Fazendo um loop que ira pecorrer cada livro dentro da lista_emprestados
    for livro in livros_emprestados:

        # Ira verificar se o titulo do livro atual do loop é igual ao titulo devolvido e se o status do livro é emprestado
        if livro["titulo"] == titulo_devolvido and livro["status"] == "emprestado":

            # se for verdadeiro ele irar remover o livro da lista de emprestado e ira mudar o status para disponivel
            livros_emprestados.remove(livro)
            livro["status"] = "disponível"
            messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
            
            # Se o usuário for um aluno, perguntar quantos dias ele ficou com o livro
            if tipo_usuario.lower() == "aluno":
                dias_emprestimo = simpledialog.askinteger("Devolver Livro", "Por quantos dias você ficou com o livro?")
                
                # Calcular a multa se o livro for devolvido atrasado
                dias_atraso = dias_emprestimo - prazo_devolucao
                if dias_atraso > 0:
                    multa = dias_atraso * 1  # A multa seja de 1 real por dia de atraso
                    messagebox.showinfo("Multa", "Você tem uma multa de R$ {} por devolução atrasada.".format(multa))
            
            return True
        
    messagebox.showinfo("Erro", "Desculpe, não foi possível realizar a devolução.")
    return False

# Pesquisar livros --------------------------------------------------------------------------------------------------------------------------------------------------


def pesquisa_livro():

    #criando uma caixa de dialogo para inserir as informações
    pesquisa = simpledialog.askstring("Pesquisar Livros", "Insira o título, autor ou ISBN do livro que deseja pesquisar:")

    # fazendo um loop onde vai percorre cada livro dentro do catalogo
    for livro in catalogo:

         # Ira verificar se o titulo do livro atual do loop é igual pesquisa ou o autor do livro ou a isbn do livro
        if livro["titulo"] == pesquisa or livro["autor"] == pesquisa or livro["isbn"] == pesquisa:

            # se for verdadeiro ele ira abrir uma caixa de mensagem flando o resultado da pesquisa 
            messagebox.showinfo("Resultado da Pesquisa", f"{livro['titulo']} por {livro['autor']} - ISBN: {livro['isbn']} - Status: {livro['status']}")
            return True
        
    # se nao ele irar abrir outra caixa de mensagem dizendo erro 
    messagebox.showinfo("Erro", "Desculpe, não foi possível encontrar o livro.")
    return False

# Janela principal ----------------------------------------------------------------------------------------------------------------------------------------------------

corf = '#808080'
corfu = '#000921'

root = tk.Tk()
root.geometry('300x350')
root.title('Sistema de Gerenciamento de Biblioteca')
root.configure(bg=corfu)

# Adicionando um titulo 

label = tk.Label(root, font=('Roboto 16 bold'), bg=corfu, fg='white',  text="Bem-vindo Aluno(a)!")
label.place(x=7, y=10)

# Adicionar um subtitulo

label = tk.Label(root, bg=corfu, fg='white', font=('Roboto 9 bold'), text="Escolha uma das opções:")
label.place(x=7, y=50)

# Adicionar o terceiro subtitulo 

label = tk.Label(root, bg=corfu, fg='white', font=('Roboto 8 '), text="Multa diária de R$1 por atraso na devolução do livro")
label.place(x=18, y=290)


# Adicionando o botao para solocitar emprestimo

button1 = tk.Button(root, text='Solicitar Empréstimo', command=solicitar_emprestimo, width=20)
button1.place(x=70, y=105)

# Adicionando um botão para Devolver livro

button2 = tk.Button(root, text='Devolver Livro', command=devolver_livro, width=20)
button2.place(x=70, y=145)

# Adicionando um botão para Pesquisar livros 

button3 = tk.Button(root, text='Pesquisar Livros', command=pesquisa_livro, width=20)
button3.place(x=70, y=185)

# Adicionar um botão para sair

button4 = tk.Button(root, text="Sair", command=root.destroy) # root.destroy fecha a janela principal quando clicado
button4.place(x=130, y=225)

root.mainloop()