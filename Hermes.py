from Pionek import Pionek

class Hermes(Pionek):
    '''
    Podklasa klasy Pionek, która ma zmienione zasady poruszania:
    pionek może poruszać się normalnie, lub poruszyć się o dowolną ilość pól, jeśli ciągle będize znajdowac się na tym samym poziomie
    '''
    def gdzie_sie_moze_poruszyc(self):
        '''
        Zmodyfikowanie metody o tej samej nazwie, ale uwzględniając zasadu ruchów Hermesa
        (może on poruszać ile chce na jednym poziomie)
        :return: Lista pól, na które może się poruszyć
        '''
        dozwolone=self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz=[]
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc()-1<=self.wysokosc():
                    z_nich_wybierz.append(pole)
        z_nich_wybierz_ten_sam_poziom_robocze=[]
        z_nich_wybierz_ten_sam_poziom_gotowe = []
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                if pole.podaj_wysokosc()==self.wysokosc():
                    z_nich_wybierz_ten_sam_poziom_robocze.append(pole)
        while [pole for pole in z_nich_wybierz_ten_sam_poziom_robocze if pole.podaj_polozenie() not in [pole.podaj_polozenie() for pole in z_nich_wybierz_ten_sam_poziom_gotowe]]!=[]:
            do_kopiowania=z_nich_wybierz_ten_sam_poziom_robocze[:]
            z_nich_wybierz_ten_sam_poziom_robocze=[pole for pole in z_nich_wybierz_ten_sam_poziom_robocze if pole.podaj_polozenie() not in [pole.podaj_polozenie() for pole in z_nich_wybierz_ten_sam_poziom_gotowe]]
            z_nich_wybierz_ten_sam_poziom_gotowe+=do_kopiowania
            do_dodawania=[]
            for pole_1 in z_nich_wybierz_ten_sam_poziom_robocze:
                for pole_2 in self.plansza.podaj_otoczenie(pole_1):
                    if not (pole_2.czy_na_nim_pionek or pole_2.czy_kopola):
                        if pole_2.podaj_wysokosc() == self.wysokosc():
                            do_dodawania.append(pole_2)
            z_nich_wybierz_ten_sam_poziom_robocze+=do_dodawania
        z_nich_wybierz.append(self.gdzie_jest())
        do_wybrania = z_nich_wybierz + z_nich_wybierz_ten_sam_poziom_gotowe
        koncowo = []
        for pole in do_wybrania:
            if pole.podaj_polozenie() not in [x.podaj_polozenie() for x in koncowo]:
                koncowo.append(pole)
        return koncowo

