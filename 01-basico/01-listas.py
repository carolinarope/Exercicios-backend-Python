#  Criar lista com 5 nomes
nomes = ["Beatriz","Marcela","João","Bernardo","Maria"]
print("Lista de nomes:", nomes)

# 2. Acessar 1º e último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]
print("Primeiro nome:", primeiro_nome)  
print("Último nome:", ultimo_nome)


# 3. Adicionar 2 nomes
nomes.append("Julia")
nomes.append("Camila")
print("Após adicionar:", nomes)


# 4. Remover 1 nome
nomes.remove("Marcela")
print("Lista de nomes atualizada após remoção de Marcela:", nomes)

# 5. Calcular tamanho da lista
tamanho_lista = len(nomes)
print("Tamanho da lista:", tamanho_lista)


# 6. Verificar se "Maria" está na lista
if "Maria" in nomes:
    print("A Maria está na lista!")
else:
    print("A Maria não está na lista.")


# 7. Ordenar alfabeticamente
nomes.sort()
print("Lista de nomes ordenada:", nomes)

