import tkinter as tk
from PIL import Image, ImageTk

def erro(msg):
    janela = tk.Toplevel()
    janela.title("Erro")
    tk.Label(janela, text=msg, fg="red").pack(padx=20, pady=10)
    tk.Button(janela, text="OK", command=janela.destroy).pack(pady=5)

def info(msg):
    janela = tk.Toplevel()
    janela.title("Info")
    tk.Label(janela, text=msg, fg="green").pack(padx=20, pady=10)
    tk.Button(janela, text="OK", command=janela.destroy).pack(pady=5)

def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()

def cadastrar_usuario():
    nome_usuario = entry_usuario.get()
    senha = entry_senha.get()

    if nome_usuario == "" or senha == "":
        erro("Por favor, preencha todos os campos.")
        return

    arquivo = open("cadastro_usuarios.txt", "a")
    arquivo.write("Usuário: " + nome_usuario + ", Senha: " + senha + "\n")
    arquivo.close()

    info("Cadastro realizado com sucesso!")
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

    tela_login()

def login_usuario():
    nome_usuario = entry_login_usuario.get()
    senha = entry_login_senha.get()

    if nome_usuario == "" or senha == "":
        erro("Por favor, preencha todos os campos.")
        return

    arquivo = open("cadastro_usuarios.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    encontrado = False
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        partes = linha.split(", ")
        if len(partes) == 2:
            usuario_salvo = partes[0].split(": ")[1]
            senha_salva = partes[1].split(": ")[1].strip()
            if nome_usuario == usuario_salvo and senha == senha_salva:
                encontrado = True
                break
        i += 1

    if encontrado:
        info("Login realizado com sucesso!")
        tela_principal()
    else:
        erro("Usuário ou senha inválidos.")

def tela_principal():
    limpar_tela()
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    imagem = Image.open("imagem.png")
    imagem = imagem.resize((1200, 700))
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_img = tk.Label(frame, image=imagem_tk)
    label_img.image = imagem_tk
    label_img.pack(pady=10)

    label_boas_vindas = tk.Label(frame, text="Bem-vindo à Tela Principal!", font=("Arial", 16))
    label_boas_vindas.pack(pady=10)

def tela_login():
    limpar_tela()
    global entry_login_usuario, entry_login_senha
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Nome de Usuário:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(frame, text="Senha:").grid(row=1, column=0, padx=10, pady=5)

    entry_login_usuario = tk.Entry(frame)
    entry_login_usuario.grid(row=0, column=1, padx=10, pady=5)
    entry_login_senha = tk.Entry(frame, show="*")
    entry_login_senha.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(frame, text="Login", command=login_usuario).grid(row=2, columnspan=2, pady=10)

def tela_cadastro():
    limpar_tela()
    global entry_usuario, entry_senha
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Nome de Usuário:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(frame, text="Senha:").grid(row=1, column=0, padx=10, pady=5)

    entry_usuario = tk.Entry(frame)
    entry_usuario.grid(row=0, column=1, padx=10, pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(frame, text="Cadastrar", command=cadastrar_usuario).grid(row=2, columnspan=2, pady=10)

root = tk.Tk()
root.title("Cadastro e Login")
tela_cadastro()
root.mainloop()