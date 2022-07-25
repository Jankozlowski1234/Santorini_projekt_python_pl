

class Pionek():
    '''
    Klasa imitująca pojedyńczego pionka w grze. Pionek 'wie', na jakim polu się znajduje, jakiej jest płci, na jakiej jest wysokości,
    kto jest jego graczem, oraz w jakiej grze się znajduje
    '''
    def __init__(self,pole,plansza,gracz,gra,plec="M"):
        self.gdzie=pole
        self.plec=plec
        self.poziom=0
        self.plansza=plansza
        self.gdzie.poluz_pionek(gracz,plec)
        self.gracz=gracz
        self.gra=gra
        self.czy_moze_sie_ruszac=True

    def gdzie_jest(self):
        '''
        Metoda zwracająca pole na którym znajduje się pionek
        :return: Pole
        '''
        return self.gdzie

    def wysokosc(self):
        '''
        Metoda zwracająca wysokość na której znajduje się pionek
        :return: Int (wysokość na jakiej jest poionek)
        '''
        return self.poziom

    def porusz_sie(self,nowe_pole):
        '''
        Metoda poruszająca pionkiem na wskazane miejsce
        :param nowe_pole: pole, na które ma wejść dany pionke
        :return:Void
        '''
        self.gdzie.wyrzuc_pionek()
        self.gdzie=nowe_pole
        self.gdzie.poluz_pionek(self.podaj_gracza(),self.podaj_plec())
        self.uaktualnij_poziom()
        return

    def gdzie_sie_moze_poruszyc(self):
        '''
        Metoda znajdująca pola, na któe może poruszyć się dany pionek
        :return: lista pól, na które może się ten pionke poruszyć
        '''
        dozwolone=self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz=[]
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc()-1<=self.wysokosc():
                    z_nich_wybierz.append(pole)
        return z_nich_wybierz

    def gdzie_moze_budowac(self):
        '''
        Metoda znajdująca pola, na których może budować dany pionek
        :return: lista pól, na których może ten pionek budować
        '''
        dozwolone = self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz = []
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc() <3 :
                    z_nich_wybierz.append(pole)
        return z_nich_wybierz

    def gdzie_moze_budowac_kopole(self):
        '''
        Metoda znajdująca pola, na których może budować kopółę dany pionek
        :return: lista pól, na których może ten pionek budować kopółę
        '''
        dozwolone = self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz = []
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc() == 3 :
                    z_nich_wybierz.append(pole)
        return z_nich_wybierz

    def mozliwosc_poruszania(self):
        '''
        Metoda uaktualizowująca czy dany pionek ma możliość ruchu w którąkolwiek stronę
        :return: Void
        '''
        if self.gdzie_sie_moze_poruszyc()==[]:
            self.czy_moze_sie_ruszac=False
        else:
            self.czy_moze_sie_ruszac=True
        return

    def podaj_plec(self):
        '''
        Metoda zwracająca płeć danego pionka
        :return: Str (płeć pionka)
        '''
        return self.plec

    def podaj_gracza(self):
        '''
        Metoda zwracająca gracza, który jest właścicielem tego pionka
        :return: Gracz
        '''
        return self.gracz

    def poruszanie(self):
        '''
        Metoda przygotowująca pionek do ruchu ("patrzy", gdzie ten pionek może się poruszyć i wybiera jedno z tych pól)
        :return: Int (numer pola na który pionek ma się poruszyć)
        '''
        if self.podaj_gracza().czy_oba_bez_ruchu():
            return "Przegrana"
        if not self.czy_moze_sie_ruszac:
            gdzie= self.podaj_drugiego_pionka().poruszanie()
            return gdzie
        gdzie_sie_moze_ruszyc=self.gdzie_sie_moze_poruszyc()
        self.gra.rysuj_numerki([x.podaj_numer() for x in gdzie_sie_moze_ruszyc],
                           f"Graczu {self.podaj_gracza().podaj_nazwe()},wybierz pole na które chcesz się poruszyć")
        gdzie = int(input("Podaj pole na które chcesz się poruszyć:").strip().lower())
        while gdzie not in [x.podaj_numer() for x in gdzie_sie_moze_ruszyc]:
            gdzie = int(input("Podaj pole na które chcesz się poruszyć:").strip().lower())
        return gdzie


    def budowanie_budynku(self):
        '''
        Metoda, która wybiera, gdzie ma być zbudowany budynek i budująca go
        :return: Void
        '''
        gdzie_mozna_budowac = self.gdzie_moze_budowac()
        self.gra.rysuj_numerki([x.podaj_numer() for x in gdzie_mozna_budowac],
                           f"Graczu {self.podaj_gracza().podaj_nazwe()} wybierz pole gdzie chcesz wybudować budowlę")
        gdzie = int(input("Podaj pole, na którym chcesz budować budowlę:").strip().lower())
        while gdzie not in [x.podaj_numer() for x in gdzie_mozna_budowac]:
            gdzie = int(input("Podaj pole, na którym chcesz budować budowlę:").strip().lower())
        for i in [x for x in gdzie_mozna_budowac if x.podaj_numer() == gdzie]:
            i.zbodoj()
        return


    def budowanie_kopoly(self):
        '''
        Metoda, która wybiera, gdzie ma być zbudowana kopóła i budująca go
        :return: Void
        '''
        gdzie_mozna_budowac = self.gdzie_moze_budowac_kopole()
        if gdzie_mozna_budowac == []:
            print("Nie masz gdzie budować kopóły, musisz budować budynek")
            self.budowanie_budynku()
            return
        self.gra.rysuj_numerki([x.podaj_numer() for x in gdzie_mozna_budowac],
                           f"Graczu {self.podaj_gracza().podaj_nazwe()} wybierz pole gdzie chcesz wybudować kopółe")
        gdzie = int(input("Podaj pole, na którym chcesz budować kopółę:").strip().lower())
        while gdzie not in [x.podaj_numer() for x in gdzie_mozna_budowac]:
            gdzie = int(input("Podaj pole, na którym chcesz budować kopółę:").strip().lower())
        for i in [x for x in gdzie_mozna_budowac if x.podaj_numer() == gdzie]:
            i.zbodoj_kopole()
        return

    def czy_wygral(self):
        '''
        Metoda zwrcająca czy dany pionke jest na pozycji wygranej
        :return: Bolean
        '''
        return self.wysokosc()==3

    def uaktualnij_poziom(self):
        '''
        Metoda uaktualizowując poziom danego pionka
        :return: Void
        '''
        self.poziom=self.gdzie.podaj_wysokosc()

    def podaj_pole_drugiego_pionka(self):
        '''
        Metoda zwracająca pole drugiego pioneka tego samego gracza
        :return: Pole (na którym jest drugi pionek)
        '''
        return self.podaj_drugiego_pionka().gdzie_jest()

    def podaj_drugiego_pionka(self):
        '''
        Metoda zwracająca drugi pionek tego samego gracza
        :return: Pionek
        '''
        gracz=self.podaj_gracza()
        pionek_2=gracz.podaj_drugi_pionek(self)
        return pionek_2

