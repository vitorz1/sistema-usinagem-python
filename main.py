from core import SistemaUsinagem
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    sistema = SistemaUsinagem()

    while True:
        print("\n" + "="*30 )
        print(" SISTEMA DE USINAGEM V1.0 ")
        print("="*30)
        print("1. Novo Pedido / Entrada. ")
        print("2. Visualizar Produção. ")
        print("3. Excluir Pedido. ")
        print("4. Editar Pedido. ")
        print("5. Sair. ")

        opcao = input("\n Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("--- CADASTRO DE PEDIDO ---")
            cliente = input("Nome do Cliente: ")
            peca = input("Nome da Peça: ")
            qtd = int(input("Quantidade: "))
            maquina = input("Máquina Responsável: ")
            status = input("Digite o Status: ")

            sistema.cadastrar_pedido(cliente, peca, qtd, maquina, status)
            input("\nPressione Enter para continuar...")
            limpar_tela()

        elif opcao == "2":
            limpar_tela()
            print("--- ORDENS EM PRODUÇÃO ---")
            producao = sistema.visualizar_producao()

            if not producao:
                print("\nNenhum pedido em produção no momento. ")
            
            else:
                
                print(f"\n{'ID':<4} | {'Cliente':<12} | {'Peça':<25} | {'Qtd':<6} | {'Máquina':<12} | {'Status'}")
                print("-" * 90)

                for p in producao:
                     
                    id_p    = str(p[0])
                    cliente = str(p[1]) 
                    peca    = str(p[2]) 
                    qtd     = str(p[3])
                    maquina = str(p[4]) if p[4] else "TC 116"
                    status  = str(p[5]) if len(p) > 5 else "Pendente"

                    print(f"{id_p:<4} | {cliente:<12} | {peca:<25} | {qtd:<6} | {maquina:<12} | {status:<15}")
            
            input("\nPressione Enter para voltar ao menu... ")
            limpar_tela()

        elif opcao == "3":
            limpar_tela()
            print("--- EXCLUIR PEDIDO ---")

            producao = sistema.visualizar_producao()
            if not producao:
                print("\nNão há pedidos para excluir. ")

            else:
                id_excluir = input("Digite o ID do pedido que deseja apagar: ")
                confirmar = input(f"Tem certeza que deseja excluir o pedido{id_excluir}? (s/n): ")
                if confirmar.lower() == 's':
                    sistema.deletar_pedido(id_excluir)

            input("\nPressione ENTER para voltar ao menu... ")
            limpar_tela()

        elif opcao == "4":
            limpar_tela()
            print("---EDITAR PEDIDO---")

            id_p = input("Digite o ID do pedido que deseja editar: ")

            print("\nDeixe em branco para não alterar ou digite o novo valor: ")
            nova_maquina = input("Nova Máquina Responsável: ")
            novo_status  = input("Novo Status (Pendente/Em andamento/Concluído): ")

            sistema.atualizar_pedido(id_p, nova_maquina, novo_status)

            input("\nPressione ENTER para continuar...")
            limpar_tela()

        elif opcao == "5":
            print("Saindo do Sistema... Até logo")
            break

if __name__ == "__main__":

    menu_principal()