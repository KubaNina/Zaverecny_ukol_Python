#!/usr/bin/env python3

class Pojistenec():
    # Třída reprezentuje pojištěnce, kterého identifikuje podle jména, příjmení, věku a telefonního čísla

    # jmeno = jméno pojištěnce
    # příjmení = příjmení pojištěnce
    # věk = věk pojištěnce
    # telefon = telefonní kontakt na pojištěnce

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return str("Pojištěnec {0} má uvedené jméno, příjmení, věk a telefon".format(self.jmeno, self.prijmeni, self.vek, self.telefon))
    # vrací textovou reprezentaci Pojištěnce
