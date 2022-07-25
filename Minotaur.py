from Pionek import Pionek

class Minotaur(Pionek):
    '''
    Podklasa klasy Pionek, która ma zmienione zasady poruszania:
    pionek może może poruszyć się na pole, na którym znajduje się pionek innego gracza, i 'wypchnąć' go na kolejne pole
    (jeśli taki ruch jest możliwy)
    '''
    def gdzie_sie_moze_poruszyc(self):
        '''
        Zmodyfikowanie metody o tej samej nazwie, ale uwzględniając zasadu ruchów Minotaura
        (może on "przesuwać pionka na innych polach")
        :return: Lista pól, na które może się poruszyć
        '''
        pole_drugiego=self.podaj_pole_drugiego_pionka()
        dozwolone=self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz=[]
        for pole in dozwolone:
            if not pole.czy_kopola:
                if pole.podaj_wysokosc()-1<=self.wysokosc():
                    if pole.czy_na_nim_pionek:
                        if self.czy_tam_na_pewno_moze_pujsc(pole):
                            z_nich_wybierz.append(pole)
                    else:
                        z_nich_wybierz.append(pole)
        z_nich_wybierz = [pole for pole in z_nich_wybierz if pole.podaj_numer() != pole_drugiego.podaj_numer()]
        return z_nich_wybierz

    def czy_tam_na_pewno_moze_pujsc(self,pole):
        '''
        Metoda sprawzająca, czy na to pole na pewno może wejść minotaur
        (czyli czy przesunięcie pionka, który na nim stał jest na pewno możliwe)
        :param pole: pole, na które mógłby wejść
        :return: Bolean
        '''
        polozenie_nowe=self.podaj_polozenie_po_przesunieciu(pole)
        if  polozenie_nowe not in self.gra.slownik_pol:
            return False
        pole_nowe=self.gra.slownik_pol[polozenie_nowe]
        if pole_nowe.czy_kopola or pole_nowe.czy_na_nim_pionek:
            return False
        return True

    def porusz_sie(self,nowe_pole):
        '''
        Metoda porusazjąca Minotaurem zgodnie z jego zasadami
        :param nowe_pole: pole, na które minotaur ma się przemieścić
        :return: Void
        '''
        if not nowe_pole.czy_na_nim_pionek:
            self.gdzie.wyrzuc_pionek()
            self.gdzie=nowe_pole
            self.gdzie.poluz_pionek(self.podaj_gracza(),self.podaj_plec())
            self.uaktualnij_poziom()
            return
        polozenie_przesuwanego=self.podaj_polozenie_po_przesunieciu(nowe_pole)
        nowe_pole_przesuwanego=self.gra.slownik_pol[polozenie_przesuwanego]
        pole_1=self.gdzie_jest()
        self.gdzie.wyrzuc_pionek()
        gracz_2=nowe_pole.podaj_kto_jest()
        pionek_2=[pionek for pionek in gracz_2.pionki if pionek.podaj_plec() == nowe_pole.plec][0]
        nowe_pole.wyrzuc_pionek()
        self.gdzie = nowe_pole
        self.gdzie.poluz_pionek(self.podaj_gracza(), self.podaj_plec())
        self.uaktualnij_poziom()

        pionek_2.gdzie = nowe_pole_przesuwanego
        nowe_pole_przesuwanego.poluz_pionek(gracz_2, pionek_2.podaj_plec())
        pionek_2.uaktualnij_poziom()
        return

    def podaj_polozenie_po_przesunieciu(self,pole):
        '''
        Metoda, która podaje położenie, na którym by się znalazł popychany przez minotaura pionek
        :param pole: pole, na którym obecnie znajduje się popychany pionek
        :return: położenie pola(para liczb)
        '''
        x_1,y_1=self.gdzie_jest().podaj_polozenie()
        x_2,y_2=pole.podaj_polozenie()
        return (2*x_2-x_1,2*y_2-y_1)