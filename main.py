#!/usr/bin/env python3
import tkinter
from databaze import Databaze


class Aplikace(tkinter.Frame):

    # Třída k zobrazení grafického rozhraní tkinter
    # pojištěnci = název zobrazeného rámce

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.db = Databaze("pojistenci.csv")
        self.master.title = "Pojištěnci"
        self.master.rowconfigure(0, weight=500)
        self.master.rowconfigure(1, weight=500)
        self.master.columnconfigure(0, weight=1000)
        self.vytvor_komponenty()
        self.uvitani = ""
        self.vypsani = ""
        self.pridani = ""
        self.vyhledani = ""
        self.konec = ""


    def vytvor_komponenty(self):

        # vytvoření klikatelných odkazů v grafickém rozhraní pro přístup k databázi.

        self.uvitani = tkinter.Label(text = "Vítejte v evidenci pojištěnců.", bg="lightblue")  # uvítání
        self.vypsani = tkinter.Label(text = "Vypsat seznam všech pojištěnců.", bg="white", command=self.vypsani_clicked)  # vypíše seznam všech pojištěnců
        self.vyhledani = tkinter.Label(text= "Vyhledat v seznamu pojištěnců.", bg="white", command=self.vyhledani_clicked)  # vyhledá v seznamu pojištěnců
        self.pridani = tkinter.Button(self.master, text="Přidat záznam do seznamu pojištěnců.", command=self.pridani_clicked) # přidá a uloží nový záznam
        self.konec = tkinter.Label(text="Konec", bg="grey", fg="white", command=self.konec_clicked)  # ukončí okno aplikace
        self.uvitani.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.vypsani.grid(row=2, column=0, sticky=tkinter.NSEW)
        self.vyhledani.grid(row=3, column=0, sticky=tkinter.NSEW)
        self.pridani.grid(row=4, column=0, sticky=tkinter.NSEW)
        self.konec.grid(row=4, column=1, sticky=tkinter.NSEW)

    def vypsani_clicked(self):
        self.db.vypis_vsechny()

    def vyhledani_clicked(self):
        self.db.vyhledej()

    def pridani_clicked(self):
        self.db.pridej_pojistence("Pavel", "Slavík", 22, 777747776)
        self.db.pridej_pojistence("Jan","Novák", 31, 604607606)
        self.db.pridej_pojistence("Tomáš", "Marný", 40, 607822833)
        self.db.pridej_pojistence("Michaela", "Ptáčková", 41, 213456788)
        self.db.uloz()

    def konec_clicked(self):
        self.close()

root = tkinter.Tk()
aplikace = Aplikace(root)
aplikace.mainloop()
