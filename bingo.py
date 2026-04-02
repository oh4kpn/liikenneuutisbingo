import random

# Perusruudut (sisältää käyttäjän antamat + lisättyjä)
base_squares = [
    "Kortiton",
    "Vakuuttamaton",
    "Katsastamaton",
    "Tieliikennekelvoton",
    "Lainattu",
    "Varastettu",
    "Luvattomasti käyttöönotettu",
    "Varastetulla verottomalla löpöllä",
    "Humalassa",
    "Huumausaineiden alaisena",
    "Ehdonalaisessa",
    "Vangittuna",
    "Alaikäinen",
    "Eläkeläinen",
]

# Pro-tason lisäruudut
pro_squares = [
    "Ei muista tapahtunutta",
    "Ajo oli vain lyhyt matka",
    "Auto ei ollut hänen",
    "Kaverin auto",
    "Poliisi tuttu entuudestaan",
    "Useita rikosnimikkeitä",
    "Ei suostunut puhallukseen",
    "Yritti paeta",
    "Pakeni jalan",
    "Suistui tieltä",
    "Ojaan",
    "Osui liikennemerkkiin",
    "Koirapartio paikalla",
    "Useita matkustajia",
    "Kyydissä alaikäisiä",
    "Ajokielto voimassa",
    "Ajoi ylinopeutta",
    "Auto rekisteristä poistettu",
    "Poliisi tutkii",
    "Myönsi teon",
    "Kielsi kaiken",
    "Sekava käytös",
    "Ei omistanut ajoneuvoa",
    "Kuljetti tavaraa",
    "Takavarikoitiin paikan päällä",
]


def generate_bingo(size=5):
    # Yhdistä listat
    all_squares = base_squares + pro_squares

    if len(all_squares) < size * size - 1:
        raise ValueError("Ei tarpeeksi ruutuja bingon generointiin")

    selected = random.sample(all_squares, size * size)

    # Aseta ilmainen ruutu keskelle
    middle = size * size // 2
    selected[middle] = "ILMAINEN: Poliisi tutkii"

    # Muodosta ruudukko
    grid = [selected[i:i+size] for i in range(0, len(selected), size)]

    return grid


def print_bingo(grid):
    size = len(grid)
    col_width = max(len(cell) for row in grid for cell in row) + 2

    def line():
        print("+" + "+".join(["-" * col_width for _ in range(size)]) + "+")

    line()
    for row in grid:
        print("|" + "|".join(cell.center(col_width) for cell in row) + "|")
        line()


if __name__ == "__main__":
    bingo = generate_bingo()
    print_bingo(bingo)

    print("\n--- Uusi bingo ---\n")
    bingo2 = generate_bingo()
    print_bingo(bingo2)
