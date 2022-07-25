from Pionek import Pionek

class Artemida(Pionek):
    '''
    Podklasa klasy Pionek, która ma zmienione zasady poruszania:
    pionek może może poruszyć się dwa razy podczas swojej tury.
    '''
    def gdzie_sie_moze_poruszyc(self):
        '''
        Zmodyfikowanie metody o tej samej nazwie, ale uwzględniając zasadu ruchów Artemidy
        (może on poruszać się dwa razy)
        :return: Lista pól, na które może się poruszyć
        '''
        dozwolone=self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz_1=[]
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc()-1<=self.wysokosc():
                    z_nich_wybierz_1.append(pole)
        z_nich_wybierz=[]
        for pole in z_nich_wybierz_1:
            dozwolone=[pole_2 for pole_2 in self.plansza.podaj_otoczenie(pole) if pole_2.podaj_polozenie()!=self.gdzie.podaj_polozenie()]
            for pole_1 in dozwolone:
                if not (pole_1.czy_na_nim_pionek or pole_1.czy_kopola):
                    if pole_1.podaj_wysokosc() - 1 <= pole.podaj_wysokosc():
                        z_nich_wybierz.append(pole_1)
        do_wybrania=z_nich_wybierz+z_nich_wybierz_1
        koncowo=[]
        for pole in do_wybrania:
            if pole.podaj_polozenie() not in [x.podaj_polozenie() for x in koncowo]:
                koncowo.append(pole)
        return koncowo