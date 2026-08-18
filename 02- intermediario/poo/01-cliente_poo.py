class Cliente:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.email = ""
        self.telefone = ""
       
    def exibir_dados(self):
        return (
        f"ID: {self.id}\n"
        f"Nome: {self.nome}\n"
        f"Email: {self.email}\n"
        f"Telefone: {self.telefone}"
    )


c1= Cliente()
c1.id = 1
c1.nome = "Carolina"
c1.email = "carolina@gmail.com"
c1.telefone = "99999999"

c2= Cliente()
c2.id = 2
c2.nome = "Amanda"
c2.email = "amanda@gmail.com"
c2.telefone = "88888888"

c3= Cliente()
c3.id = 3
c3.nome = "Bruna"
c3.email = "bruna@gmail.com"
c3.telefone = "77777777"


print(c1.exibir_dados())
print(c2.exibir_dados())
print(c3.exibir_dados())