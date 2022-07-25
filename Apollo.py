from Pionek import Pionek

class Apollo(Pionek):
    '''
    Podklasa klasy Pionek, która ma zmienione zasady poruszania:
    pionek może może poruszyć się na pole, na którym znajduje się pionek innego gracza i zamienić się z nim miejscami
    (jeśli ruch jest zgodny z pozostałymi zasadami)
    '''

    def gdzie_sie_moze_poruszyc(self):
        '''
        Zmodyfikowanie metody o tej samej nazwie, ale uwzględniając zasadu ruchów Apolla
        (zamienić się miejscem z innym pionkiem podczas swojego ruchu)
        :return: Lista pól, na które może się poruszyć
        '''
        pole_drugiego=self.podaj_pole_drugiego_pionka()
        dozwolone=self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz=[]
        for pole in dozwolone:
            if not pole.czy_kopola:
                if pole.podaj_wysokosc()-1<=self.wysokosc():
                    z_nich_wybierz.append(pole)
        z_nich_wybierz = [pole for pole in z_nich_wybierz if pole.podaj_numer() != pole_drugiego.podaj_numer()]
        return z_nich_wybierz

    def porusz_sie(self,nowe_pole):
        '''
        Metoda porusazjąca Apollem zgodnie z jego zasadami
        :param nowe_pole: pole, na które Apollo ma się przemieścić
        :return: Void
        '''

        if not nowe_pole.czy_na_nim_pionek:
            self.gdzie.wyrzuc_pionek()
            self.gdzie=nowe_pole
            self.gdzie.poluz_pionek(self.podaj_gracza(),self.podaj_plec())
            self.uaktualnij_poziom()
            return
        pole_1=self.gdzie_jest()
        self.gdzie.wyrzuc_pionek()
        gracz_2=nowe_pole.podaj_kto_jest()
        pionek_2=[pionek for pionek in gracz_2.pionki if pionek.podaj_plec() == nowe_pole.plec][0]
        nowe_pole.wyrzuc_pionek()
        self.gdzie = nowe_pole
        self.gdzie.poluz_pionek(self.podaj_gracza(), self.podaj_plec())
        self.uaktualnij_poziom()
        pionek_2.gdzie = pole_1
        pole_1.poluz_pionek(gracz_2, pionek_2.podaj_plec())
        pionek_2.uaktualnij_poziom()
        return



