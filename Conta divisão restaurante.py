pessoas = int(input("Informe o núemro de pessoas:\n"))
valor = float(input("Informe o valor da conta:\n"))

print("Valor total da conta: ", valor)
print("Valor total com a taxa de severviço: ", valor*1.1)
print("Cada pessoa deverá pagar",((valor*1.1)/pessoas))



