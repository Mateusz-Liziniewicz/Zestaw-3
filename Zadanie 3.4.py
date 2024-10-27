while True:
    i = input("Podaj liczbę (lub wpisz 'stop', aby zakończyć): ")

    if (i.lower() == "stop"):
        break

    try:
        x = float(i)
        print(f"Liczba: {x}, Trzecia potęga: {pow(x, 3)}")
    except ValueError:
        print("Podaj liczbę rzeczywistą, lub wpisz 'stop'!")
