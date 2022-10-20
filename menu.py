import data


def menu():
    games = data.getData()
    exit = 0
    while(exit == 0):
        print("\nEscolha uma equipa:")
        for i, game in enumerate(games):
            print(f"{i} - {game['homeTeam']}")
        choice = int(input("Opção: "))
        print(f"\nEscolheu {games[choice]['homeTeam']}\n")
        print(
            f"O jogo é {games[choice]['homeTeam']} vs {games[choice]['awayTeam']}\n")
        print(f"O jogo começa às {games[choice]['commenceTime']}\n")
        print("Escolha uma chave:")
        for i in range(0, len(games[choice]['bookmakers'])):
            print(f"{i} - {games[choice]['bookmakers'][i]['key']}")
        chave = int(input("Chave: "))
        print(f"\nEscolheu {games[choice]['bookmakers'][chave]['key']}\n")
        print("Escolha um mercado:")
        for i in range(0, len(games[choice]['bookmakers'][chave]['markets'])):
            print(
                f"{i} - {games[choice]['bookmakers'][chave]['markets'][i]['key']}")
        mercado = int(input("Mercado: "))
        print(
            f"\nEscolheu {games[choice]['bookmakers'][chave]['markets'][mercado]['key']}\n")
        print("Escolha uma aposta:")
        for i in range(0, len(games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes'])):
            print(
                f"{i} - {games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes'][i]['name']} com preço de {games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes'][i]['price']}")
        aposta = int(input("Aposta: "))
        print("\nAposta registada com sucesso!\n")
        print("Deseja fazer outra aposta?")
        exit = int(input("0 - Sim\n1 - Não\nOpção: "))


def main():
    game = menu()


if __name__ == "__main__":
    main()
