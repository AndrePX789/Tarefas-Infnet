nome =input("Qual seu nome?\n")
idade = int(input(f"Olá {nome}, informe, por favor, a sua idade:\n"))

if idade < 16:
    print(nome,", você ainda não é eleitor.")

if idade >= 16 and idade <18:
    print(nome,", você é eleitor facultativo.")

if idade >= 18:
    print(nome,", vocé é eleitor obrigatório.")
