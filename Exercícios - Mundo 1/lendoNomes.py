name = str(input("Digite seu nome:\n "))
print("Nome maiúsculo:", name.upper())
print("Nome minúsculo:", name.lower())
print("Quantidade de letras do nome:", len(name.replace(" ", "")))
dividido = name.split()
print("Quantidade de letras do primeiro nome:", len(dividido[0]))
