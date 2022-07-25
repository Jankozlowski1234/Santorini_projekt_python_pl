class Pole():
    '''
    Klasa, która reprezentuje pojedyńcze pole na planszy.
    Pole 'pamięta' jakie jest jego położenie, czy ma na sobie plansze lub kopole, oraz jeśli jest na nim pionek,
    to jakiej jest plci, oraz którego jest gracza.
    '''
    def __init__(self,polozenie,czy_kopola=False,wysokosc=0):
        self.polozenie=polozenie
        self.czy_kopola=czy_kopola
        self.wysokosc=wysokosc
        self.czy_na_nim_pionek=False
        self.ktory_gracz=None
        self.plec=None
        self.numer=None
        self.nadaj_numer()


    def nadaj_numer(self):
        '''
        Metoda nadająca unikalny numer każdemu Polu (w zależności od jego położenia)
        :return: Void
        '''
        x,y=self.polozenie
        self.numer=y+(x)*5

    def zbodoj(self):
        '''
        Metoda zwiększająca na danym Polu wysokośc budowli
        :return: Void
        '''
        if self.czy_kopola:
            raise ValueError("Nie można bydować na kopole")
        if self.wysokosc==3:
            raise ValueError("Nie możą dobudowywać kolejnych pięter")
        self.wysokosc+=1
        return

    def zbodoj_kopole(self):
        '''
        Metoda budujaca na danym polu kopułę
        :return: Void
        '''
        if self.czy_kopola:
            raise ValueError("Tu już jest kopola")
        self.czy_kopola=True

    def podaj_polozenie(self):
        '''
        Metoda zwracająca położenie danego pola
        :return: Touple (położenie pola)
        '''
        return self.polozenie

    def podaj_wysokosc(self):
        '''
        Metoda zwracająca wysokość budowki danego pola
        :return: Int (wysokośc budowli na polu)
        '''
        return self.wysokosc

    def podaj_kto_jest(self):
        '''
        Metoda zwracająca Gracza, którego Pionek jest na tym polu
        :return: Gracz (który ma pionek na danym polu)
        '''
        return self.ktory_gracz

    def poluz_pionek(self,gracz,plec):
        '''
        Metoda symulująca położenei na danym polu pionka
        :param gracz: Gracz, którego pionek jest kładziony na to pole
        :param plec:  pleć pionka, który jest kładziony na to pole
        :return: Void
        '''
        self.czy_na_nim_pionek=True
        self.ktory_gracz=gracz
        self.plec=plec
        return

    def wyrzuc_pionek(self):
        '''
        Metoda symulująca usunięcie pionka z danego pola
        :return: Void
        '''
        self.czy_na_nim_pionek=False
        self.ktory_gracz=None
        self.plec=None
        return

    def podaj_numer(self):
        '''
        Metoda, która zwraca numer danego pola
        :return: Int (numer pola)
        '''
        return self.numer

