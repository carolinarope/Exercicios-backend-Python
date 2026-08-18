class Cliente:
    def __init__(self, id_cliente, nome, email, telefone):
        self.id = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        return (
        f"ID: {self.id}\n"
        f"Nome: {self.nome}\n"
        f"Email: {self.email}\n"
        f"Telefone: {self.telefone}"
    )

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone
        print(f"Telefone atualizado para: {self.telefone}")

c1 = Cliente(1, "Carolina", "carolina@gmail.com", "99999999")
c2 = Cliente(2, "Amanda", "amanda@gmail.com", "88888888")
c3 = Cliente(3, "Bruna", "bruna@gmail.com", "77777777")


print(c1.exibir_dados())
print()
print(c2.exibir_dados())
print()
print(c3.exibir_dados())
print()


c1.atualizar_telefone("99999998")
print()
print(c1.exibir_dados())
print()
print(c2.exibir_dados())