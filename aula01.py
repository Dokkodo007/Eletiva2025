# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Entrada do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (obesidade mórbida)")
