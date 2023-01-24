from random import randint

game = 'ano'

while game == 'ano':

    print("***BlackJack***\n   **INFO**\nOdpovedaj iba slovami: ano, nie")

    hrac = 0
    bankar = 0
    fold = 0

    while fold == 0:
        if hrac < 21:
            karta = randint(1, 11)
            bankar = bankar + karta

        if (bankar > 16):
            if (bankar < 22):
                print("\nMám", bankar, ". Už neťahám")
                fold = 1
                hodnota = 'dalej'
            else:
                fold = 1
                hodnota = 'nie'

        if (bankar < 17):
            print("\nVytiahol som si", karta, ". Ja mám", bankar)
            hodnota = input("Chceš kartu? ")
            while hodnota != 'ano' and hodnota != 'nie':
                hodnota = input(
                    "Ak chceš kartu napíš ano, ak kartu nechceš napíš nie ")

        if (hodnota == 'ano'):
            karta = randint(1, 11)
            hrac = hrac + karta
            print("Vytiahol si", karta, ". Ty máš", hrac)

        if (hodnota == 'nie'):
            fold = 1
            hodnota = 'konec'
      
        if hrac > 20:
            fold = 1
            hodnota = 'konec'

    if (hodnota == 'nie'):
        while bankar < 17:
            karta = randint(1, 11)
            bankar = bankar + karta
            print("\nVytiahol som si", karta, ". Ja mám", bankar, "Ty máš",
                  hrac)

    if (hodnota == 'dalej'):
        hodnota = input("Chces kartu?")
        while hodnota != 'ano' and hodnota != 'nie':
            hodnota = input(
                "Ak chceš kartu napíš ano, ak kartu nechceš napíš nie ")

    while hodnota == 'ano':
        if (hrac < 21):
            karta = randint(1, 11)
            hrac = hrac + karta

            print("Vytiahol si", karta, ". Ty máš", hrac)

            if (hrac > 21):
                hodnota = 'nie'
            if (hrac < 21):
                hodnota = input("Chces kartu?")
                while hodnota != 'ano' and hodnota != 'nie':
                    hodnota = input(
                        "Ak chceš kartu napíš ano, ak kartu nechceš napíš nie "
                    )

    if (hrac < 22):
        if (hrac == 21):
          print("Máš", hrac, "a vyhral si. GRATULUJEM")
          game = input("Pre pokračovanie napíš ano")
          while game != 'ano' and game != 'nie':
              game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")
        else:
          if (hrac > bankar):
            print("Mám", bankar, "a ty máš", hrac, ". Vyhral si, GRATULUJEM")
            game = input("Pre pokračovanie napíš ano")
            while game != 'ano' and game != 'nie':
                game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")

    if (bankar < 22):
        if (bankar == 21):
          print("Mám", bankar, "a prehral si.")
          game = input("Pre pokračovanie napíš ano")
          while game != 'ano' and game != 'nie':
              game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")
      
        if (bankar > hrac):
            print("Mám", bankar, "a ty máš", hrac, ". Prehral si")
            game = input("Pre pokračovanie napíš ano")
            while game != 'ano' and game != 'nie':
                game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")

        if (bankar == hrac):
            print("Obaja máme", bankar, ". Remíza")
            game = input("Pre pokračovanie napíš ano")
            while game != 'ano' and game != 'nie':
                game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")
  
    if (bankar > 21):
        print("Mám", bankar, "a prehral som. GRATULUJEM")
        game = input("Pre pokračovanie napíš ano")
        while game != 'ano' and game != 'nie':
            game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")

    if (hrac > 21):
        print("Máš", hrac, "a prehral si.")
        game = input("Pre pokračovanie napíš ano")
        while game != 'ano' and game != 'nie':
            game = input("Ak chceš napíš ano, ak chceš skončiť napíš nie")


print("Koniec hry")
