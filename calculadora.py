def calculadora():
    print("Calculadora do Póvoas")
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")
    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            return

        if escolha == '1':
            resultado = num1 + num2
            operacao = "+"
        elif escolha == '2':
            resultado = num1 - num2
            operacao = "-"
        elif escolha == '3':
            resultado = num1 * num2
            operacao = "*"
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                return
            resultado = num1 / num2
            operacao = "/"

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
    else:
        print("Opção inválida. Por favor, selecione 1, 2, 3 ou 4.")

# Executa a calculadora
calculadora()