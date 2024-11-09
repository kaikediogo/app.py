def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        selecao = input("Digite o número da operação (1/2/3/4): ")

        if selecao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if selecao == '1':
                print(f"{num1} + {num2} = {soma(num1, num2)}")
            elif selecao == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")
            elif selecao == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
            elif selecao == '4':
                print(f"{num1} / {num2} = {divisao(num1, num2)}")

            outra = input("Deseja realizar outra operação? (sim/não): ")
            if outra.lower() != 'sim':
                break
        else:
            print("Seleção inválida. Por favor, escolha novamente.")

calculadora()
