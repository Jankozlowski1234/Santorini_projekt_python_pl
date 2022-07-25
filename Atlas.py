from Pionek import Pionek

class Atlas(Pionek):
    '''
    Podklasa klasy Pionek, która ma zmienione zasady budowania kopół:
    pionek może budować kopóły na każdej wysokości bloku.
    '''
    def gdzie_moze_budowac_kopole(self):
        '''
        Zmodyfikowanie metody o tej samej nazwie, ale uwzględniając zasady budowania kopół Atlasa
        (może on budować kopóły na kazdej wysokości)
        :return: Lista pól, na których może budować kopółę
        '''
        dozwolone = self.plansza.podaj_otoczenie(self.gdzie)
        z_nich_wybierz = []
        for pole in dozwolone:
            if not (pole.czy_na_nim_pionek or pole.czy_kopola):
                z_nich_wybierz.append(pole)
        return z_nich_wybierz