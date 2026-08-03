# Sistema de login básico
usuarios = {
    "carolina": "senha123",
    "admin": "admin123"
}

email = input("Email: ")
senha = input("Senha: ")

if email in usuarios and usuarios[email] == senha:
    print("Login realizado com sucesso!")
else:
    print("Email ou senha incorretos")
    