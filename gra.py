from Pole import Pole
from Plansza import Plansza
from Gracz import Gracz
from Atlas import Atlas
from Apollo import Apollo
from Pionek import Pionek
from Minotaur import Minotaur
from Artemida import Artemida
from Hermes import Hermes
from pydoc import render_doc

class Gra():
    '''
    Główna klasa w projekcie, odpowiada za rozpoczęcie gry, oraz dawanie ruchu kolejnym graczom.
    '''
    def __init__(self):
        self.plansza = None
        self.gracze=[]
        self.slownik_pol=None
        self.slownik_nomerkow=None
        self.slownik_pionkow={"hermes":Hermes,"minotaur":Minotaur,"apollo":Apollo,"atlas":Atlas,"artemida":Artemida,"zwykły":Pionek}

    def zacznij(self):
        '''
        Metoda zaczynająca gre, tworzy ona obu graczy wraz z Pionkami, plansze oraz Pola.
        '''
        nazwa1 = input("Podaj nazwę pierwszego gracza: ").strip()
        nazwa2 = input("Podaj nazwę drugiego gracza: ").strip()
        while nazwa2 ==nazwa1:
            nazwa2 = input("Podaj nazwę drugiego gracza, inną od nazwy pierwszego gracza:").strip()
        jaka_gra=input("Czy chcecie grać w wejsję z bogami (tak lub nie):").strip().lower()
        if jaka_gra=="tak":
            nazwy=""
            nazwy_sprawdzenie=[]
            for nazwa in self.slownik_pionkow.keys():
                if nazwa!="zwykły":
                    nazwy_sprawdzenie.append(nazwa)
                    nazwy+=nazwa
                    nazwy+=", "
            nazwy=nazwy[:-2]
            bog1=input(f"Graczu {nazwa1} wybierz jednego boga z podanych ({nazwy}): ").strip().lower()
            while not bog1 in nazwy_sprawdzenie:
                bog1 = input(f"Graczu {nazwa1} wybierz jednego boga z podanych ({nazwy}): ").strip().lower()
            nazwy = ""
            nazwy_sprawdzenie = []
            for nazwa in self.slownik_pionkow.keys():
                if nazwa != "zwykły" and nazwa !=bog1:
                    nazwy_sprawdzenie.append(nazwa)
                    nazwy += nazwa
                    nazwy += ", "
            nazwy = nazwy[:-2]
            bog2=input(f"Graczu {nazwa2} wybierz jednego boga z podanych ({nazwy}): ").strip().lower()
            while not bog2 in nazwy_sprawdzenie:
                bog2 = input(f"Graczu {nazwa2} wybierz jednego boga z podanych ({nazwy}): ").strip().lower()
            bog1=self.slownik_pionkow[bog1]
            bog2 = self.slownik_pionkow[bog2]
        else:
            bog1=self.slownik_pionkow["zwykły"]
            bog2 = self.slownik_pionkow["zwykły"]



        slownik_pol = {}
        slownik_nomerkow={}
        n=0
        for i in range(5):
            for j in range(5):
                slownik_pol[(i, j)] = Pole((i, j))
                slownik_nomerkow[n]= (i,j)
                n+=1
        self.plansza = Plansza(slownik_pol=slownik_pol,slownik_numerkow=slownik_nomerkow,gracz1=nazwa1,gracz2=nazwa2)
        self.slownik_pol=slownik_pol
        self.slownik_nomerkow=slownik_nomerkow


        self.rysoj_poczotek(f"Graczu {nazwa1}, wybiez dwa pola, na których zaczniejsz gre:")
        pola=input("Podaj dwa pola, oddzielone przecinkiem:")

        pola=pola.split(",")
        nr1=int(pola[0].strip())
        nr2=int(pola[1].strip())
        pole1=slownik_pol[slownik_nomerkow[nr1]]
        pole2=slownik_pol[slownik_nomerkow[nr2]]

        Gracz1=Gracz(nazwa1,pole1,pole2,plansza=self.plansza,gra=self,pionek=bog1)
        self.gracze.append(Gracz1)
        self.rysoj_poczotek2([nr1,nr2],text=f"Graczu {nazwa2}, wybiez dwa pola, na których zaczniejsz gre:")
        pola=input("Podaj dwa pola, oddzielone przecinkiem:")

        pola=pola.split(",")
        nr1=int(pola[0].strip())
        nr2=int(pola[1].strip())
        pole1=slownik_pol[slownik_nomerkow[nr1]]
        pole2=slownik_pol[slownik_nomerkow[nr2]]

        Gracz2=Gracz(nazwa2,pole1,pole2,plansza=self.plansza,gra=self,pionek=bog2)
        self.gracze.append(Gracz2)
        zwyciezca = self.petla_ruchow()

        self.rysoj(f"Gracz {zwyciezca.podaj_nazwe()} zwyciężył, Gratulacje")



    def rysoj(self,text=""):
        '''
        Wywołuje na Planszy metodę rysuj.
        :param text: tekst, który będzie wyświetlany na planszy
        :return: Void
        '''
        self.plansza.rysoj(text=text)
        return

    def rysoj_poczotek(self,text=""):
        '''
        Specialna metoda używana na początku rozrywki
        :param text: tekst, który będzie wyświetlany na planszy
        :return: Void
        '''
        self.plansza.rysuj_numerki([i for i in range(25)],text=text)
        return

    def rysoj_poczotek2(self,lista,text=""):
        '''
        Metoda do ryzsowania planszy dla ustawienia drugiego gracza
        :param lista:  lista numerów pól, które są już zajęte
        :param text: tekst, który będzie wyświetlany na planszy
        :return: Void
        '''
        self.plansza.rysuj_numerki([i for i in range(25) if i not in lista],text=text)
        return

    def rysuj_numerki(self,lista,text=""):
        '''
        Metoda, która rysuje planszę a na niej tylko niektóre pola
        :param lista:  lista numerów pól, które mają być wyświetlone
        :param text: tekst, który będzie wyświetlany na planszyr
        :return: Void
        '''
        self.plansza.rysuj_numerki(lista,text=text)
        return


    def ruch(self,gracz):
        '''
        Metoda symulująca ruch jednego z graczy
        :param gracz: Gracz, którego jest teraz ruch
        :return: Void lub Str (jeśli gra się kończy)
        '''
        self.rysoj(f"Graczu {gracz.podaj_nazwe()}, wybierz plec pionka, którym chcesz się ruszyć")
        plec=input("Podaj plec pionka, którym chcesz się ruszyć (skrutowo):").strip().upper()
        while plec not in ["K","M"]:
            plec = input("Podaj plec pionka, którym chcesz się ruszyć (skrutowo):").strip().upper()

        pionek_ruszany=gracz.podaj_pionek(plec)
        gdzie=pionek_ruszany.poruszanie()
        if gdzie=="Przegrana":
            return "Przegrana"
        pionek_ruszany.porusz_sie(self.slownik_pol[self.slownik_nomerkow[gdzie]])
        if pionek_ruszany.czy_wygral():
            return "Wygrana"
        if pionek_ruszany.gdzie_moze_budowac_kopole()==[]:
            pionek_ruszany.budowanie_budynku()
            return
        self.rysoj(f"Graczu {gracz.podaj_nazwe()}, czy chesz budować kopole, czy budynek")
        co=input("Podaj czy chcesz budować kopole, czy budynek(napsz 'b', lub 'k'):").strip().lower()
        while co not in ["b","k"]:
            co = input("Podaj czy chcesz budować kopole, czy budynek(napsz 'b', lub 'k'):").strip().lower()
        if co == "b":
            pionek_ruszany.budowanie_budynku()
        else:
            pionek_ruszany.budowanie_kopoly()
        return


    def petla_ruchow(self):
        '''
        Metoda symulująca przebieg rozrywki, po kolei rusza graczami, aż do momentu skonczenia gry
        :return: Gracz (ten, który wygrał grę)
        '''
        gracz=self.gracze[0]
        koniec =None
        while koniec is None:
            koniec=self.ruch(gracz)
            gracz=self.podaj_drugiego(gracz)
        if koniec=="Przegrana":
            return gracz
        return self.podaj_drugiego(gracz)


    def podaj_drugiego(self,gracz):
        '''
        Meteda, która zwraca gracza innego od tego, którego podajemy jako parametr
        :param gracz: gracz, którego nie chcemy zwrócić
        :return: Gracz
        '''
        return [x for x in self.gracze if x.podaj_nazwe()!= gracz.podaj_nazwe()][0]



def napisz_dokumentacje():
    napisy=["gra","Plansza","Pole","Gracz","Pionek","Apollo","Hermes","Minotaur","Artemida","Atlas"]
    a=""
    for napis in napisy:
        a+=render_doc(napis)
    print(a)
    return


if __name__=="__main__":
#   napisz_dokumentacje()
    gra = Gra()
    gra.zacznij()

