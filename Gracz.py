from Pionek import Pionek

class Gracz():
    '''
    Klasa, która reprezentuje pojedyńczego gracza.
    Gracz 'wie' jakie są jego pionki, oraz jak się nazywa.
    '''


    def __init__(self,nazwa,pole1,pole2,plansza,gra,pionek=Pionek):
        self.pionki=[pionek(pole1,plansza=plansza,gracz=self,gra=gra),pionek(pole2,plansza=plansza,gracz=self,gra=gra,plec="K")]
        self.nazwa=nazwa

    def podaj_pionek(self,plec):
        '''
        Metoda zwracająca pionka o określonej płci
        :param plec: płeć, której chcemy znaleźć pionek
        :return: Pionek o podanej płci
        '''
        if self.pionki[0].podaj_plec() == plec:
            return self.pionki[0]
        return self.pionki[1]

    def podaj_nazwe(self):
        '''
        Zwraca nazwę gracza
        :return: Str (nazwa gracza)
        '''
        return self.nazwa

    def podaj_drugi_pionek(self,pionek):
        '''
        Metoda zwracająca pionek, drugi od podanego
        :param pionek: pionke, którego nie chemy
        :return: Pionek (ale innu od podanego jako argument)
        '''
        return [x for x in self.pionki if x.podaj_plec()!=pionek.podaj_plec()][0]

    def czy_oba_bez_ruchu(self):
        '''
        Metoda sprawdzająca, czy oba pionki są bez ruchu
        :return: Bolean
        '''
        for pionek in self.pionki:
            pionek.mozliwosc_poruszania()
        if [pionek.czy_moze_sie_ruszac for pionek in self.pionki]==[False,False]:
            return True
        return False
