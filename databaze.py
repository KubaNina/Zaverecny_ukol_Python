#!/usr/bin/env python3
import csv   # ke čtení v CSV databází
from pojistenec import Pojistenec

class Databaze():
    # třída Pojištěnci reprezentuje operace se seznamem pojištěnců v aplikaci
    # vypiš všechny = vypíše seznam všech pojištěnců
    # vyhledej = spustí fulltextové vyhledávání v databázi
    # přídej pojištěnce = přidá jméno, příjmení, věk a telefon pojištěnce
    # vrať všechny - vrátí seznam pojištěných
    # ulož = uloží data do souboru pojistenci.csv



    pojistenci = []

    def __init__(self, soubor):
        self.soubor = "pojistenci.csv"

    def vypis_vsechny(self):
        with open(self.soubor, "pojistenci.csv", encoding="utf-8") as f:
            vypis = csv.reader(f, delimiter=" ", quotechar="|")
            for row in vypis:
                print(", ".join(row))

    def vyhledej(self):
        with open(self.soubor, "pojistenci.csv", newline="", encoding="utf-8") as f:
            vyhledej = csv.reader(f, delimiter=" ", quotechar="|")
            for row in vyhledej:
                print(", ".join(row))

    def pridej_pojistence(self, jmeno, prijmeni, vek, telefon):
        p = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(p)

    def vrat_vsechny(self):
        return self.pojistenci

    def uloz(self):
        with open(self.soubor, "pojistenci.csv", encoding="utf-8") as f:
            for p in self.pojistenci:
                hodnoty = [p.jmeno, p.prijmeni, str(p.vek), str(p.telefon)]
                radek = ";".join(hodnoty)
                f.write(radek + "\n")


