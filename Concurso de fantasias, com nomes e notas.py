nomes = []
notas = []

for i in range(10):
#"NomesL"
    nomesl, notasl = input("Informe o nome do participante e sua nota, seprados por vírgula e sem espaço.\n").split(",")
    nomes.append(nomesl)
    notas.append(int(notasl))

index = 0
maior_nota = 0
index_maior_nota = 0
for i in notas:
    if i > maior_nota:
        maior_nota = i
        index_maior_nota = index
    index += 1
    
print(f"O vencedor é {nomes[index_maior_nota]} com a nota {notas[index_maior_nota]}")
