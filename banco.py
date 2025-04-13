def main():
    # Configurações iniciais
    saldo = 0.0
    limite_por_saque = 500.0
    extrato = []
    saques_realizados = 0
    LIMITE_SAQUES_DIARIOS = 3

    # Menu do sistema
    def exibir_menu():
        print("\n" + "=" * 30)
        print(" MENU PRINCIPAL ".center(30, "="))
        print("=" * 30)
        print("[D] Depositar")
        print("[S] Sacar")
        print("[E] Extrato")
        print("[Q] Sair")
        print("=" * 30)

    # Loop principal do sistema
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").lower()

        # Opção de Depósito
        if opcao == "d":
            try:
                valor = float(input("Valor do depósito: R$ "))
                if valor > 0:
                    saldo += valor
                    extrato.append(f"Depósito: +R$ {valor:.2f}")
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Valor inválido! O depósito deve ser positivo.")
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

        # Opção de Saque
        elif opcao == "s":
            # Verifica se ainda há saques disponíveis
            if saques_realizados >= LIMITE_SAQUES_DIARIOS:
                print("Limite diário de saques atingido (3 saques por dia).")
                continue

            try:
                valor = float(input("Valor do saque: R$ "))

                if valor <= 0:
                    print("Valor inválido! O saque deve ser positivo.")
                elif valor > saldo:
                    print("Saldo insuficiente para realizar o saque.")
                elif valor > limite_por_saque:
                    print(f"Limite por saque excedido (R$ {limite_por_saque:.2f}).")
                else:
                    saldo -= valor
                    extrato.append(f"Saque:    -R$ {valor:.2f}")
                    saques_realizados += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    print(f"Saques restantes hoje: {LIMITE_SAQUES_DIARIOS - saques_realizados}")
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

        # Opção de Extrato
        elif opcao == "e":
            print("\n" + "=" * 30)
            print(" EXTRATO BANCÁRIO ".center(30, "="))
            print("=" * 30)
            
            if not extrato:
                print("Nenhuma movimentação realizada.")
            else:
                for movimento in extrato:
                    print(movimento)
            
            print("\n" + "-" * 30)
            print(f"SALDO ATUAL: R$ {saldo:.2f}".rjust(30))
            print("=" * 30)

        # Opção de Sair
        elif opcao == "q":
            print("\nObrigado por usar nosso sistema bancário!")
            break

        # Opção inválida
        else:
            print("Opção inválida! Por favor, escolha uma opção do menu.")

if __name__ == "__main__":
    main()