# criar dois botoes
import customtkinter
import sqlite3


db_principal = sqlite3.connect('usuarios.db')

cursor = db_principal.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        cpf TEXT NOT NULL                        
    );
""")
db_principal.commit()
app = customtkinter.CTk()
app.geometry("500x300")
app.title("Página de Login")

def pagina_registrar():
    app2.mainloop()
    
    

def registrar():
    nome_result = nome2.get()
    email_result = email2.get()
    senha_result = senha2.get()
    cpf_result = cpf2.get()
    cursor.execute("INSERT INTO Usuarios VALUES (?,?,?,?)", (nome_result,email_result,senha_result,cpf_result))
    db_principal.commit()
    app2.destroy()

def login():
    email_result = email.get()
    senha_result = senha.get()
    cursor.execute("""
        SELECT * FROM Usuarios
        WHERE (email = ? AND senha = ?)
    """, (email_result,senha_result))
    VerifyLogin = cursor.fetchone()
    try:
        if(email_result in VerifyLogin and senha_result in VerifyLogin):
            print('Acesso Confirmado!')
        else:
            pass
    except:
        print('Acesso Negado!')

#app1
texto = customtkinter.CTkLabel(app,text='Fazer Login')
email = customtkinter.CTkEntry(app,placeholder_text='Email')
senha = customtkinter.CTkEntry(app,placeholder_text='Senha',show='*')
botao_login = customtkinter.CTkButton(app,text='Login',command=login)
botao_registrar = customtkinter.CTkButton(app,text='Registrar-se',command=pagina_registrar)
texto.pack(padx=10,pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao_login.pack(padx=10,pady=10)
botao_registrar.pack(padx=10,pady=10)

#app2
app2 = customtkinter.CTk()
app2.geometry("500x300")
app2.title("Página de Cadastro")
texto2 = customtkinter.CTkLabel(app2,text='Registrar')
nome2 = customtkinter.CTkEntry(app2,placeholder_text='Nome')
email2 = customtkinter.CTkEntry(app2,placeholder_text='Email')
senha2 = customtkinter.CTkEntry(app2,placeholder_text='Senha',show='*')
cpf2 = customtkinter.CTkEntry(app2,placeholder_text='CPF')
botao_registrar2 = customtkinter.CTkButton(app2,text='Se Registrar',command=registrar)
texto2.pack(padx=10,pady=10)
nome2.pack(padx=10,pady=10)
email2.pack(padx=10, pady=10)
senha2.pack(padx=10, pady=10)
cpf2.pack(padx=10,pady=10)
botao_registrar2.pack(padx=10,pady=10)


app.mainloop()
