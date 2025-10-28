import random
import time

def mostrar_dado(valor):
    caras = {
        1: [
            "+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"
        ]
    }
    for linea in caras[valor]:
        print(linea)

def lanzar_dado():
    print("Lanzando el dado...")
    time.sleep(1)
    valor = random.randint(1, 6)
    mostrar_dado(valor)
    print(f"Salió: {valor}")

lanzar_dado()
