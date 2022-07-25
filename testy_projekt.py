import unittest
from Pole import Pole
from Plansza import Plansza
from Gracz import Gracz
from gra import Gra


class Test(unittest.TestCase):
    def setUp(self):
        self.gra= Gra
        self.pole_1=Pole((1,1))
        self.pole_2=Pole((2,3))
        self.pole_3=Pole((4,4),True,3)
        slownik_pol = {}
        slownik_nomerkow={}
        n=0
        for i in range(5):
            for j in range(5):
                slownik_pol[(i, j)] = Pole((i, j))
                slownik_nomerkow[n]= (i,j)
                n+=1

        self.plansza=Plansza(slownik_pol=slownik_pol,slownik_numerkow=slownik_nomerkow,gracz1="gracz1",gracz2="gracz2")
        self.pole_4=self.plansza.slownik_pol[(3,4)]
        self.pole_5=self.plansza.slownik_pol[(0,0)]
        self.gracz=Gracz(nazwa="gracz1",pole1=self.pole_1,pole2=self.pole_2,plansza=self.plansza,gra=self.gra)
        self.pionek_k=self.gracz.podaj_pionek("K")
        self.pionek_m=self.gracz.podaj_pionek("M")

    def test_pole(self):
        self.assertEqual(self.pole_1.podaj_polozenie(),(1,1))
        self.assertEqual(self.pole_1.podaj_numer(), 6)
        self.assertFalse(self.pole_1.czy_kopola)
        self.assertTrue(self.pole_3.czy_kopola)
        self.assertEqual(self.pole_1.podaj_wysokosc(),0)
        self.assertEqual(self.pole_3.podaj_wysokosc(), 3)
        with self.assertRaises(ValueError):
            self.pole_3.zbodoj()
        with self.assertRaises(ValueError):
            self.pole_3.zbodoj_kopole()
        self.pole_4.zbodoj()
        self.pole_4.zbodoj_kopole()
        with self.assertRaises(ValueError):
            self.pole_4.zbodoj()

    def test_plansza(self):
        self.assertEqual(len(self.plansza.slownik_pol),25)
        self.assertEqual(len(self.plansza.slownik_numerkow), 25)
        self.assertEqual(len(self.plansza.podaj_otoczenie(self.pole_1)),8)
        self.assertEqual(len(self.plansza.podaj_otoczenie(self.pole_5)),3)


    def test_pionek(self):
        self.assertFalse(self.pionek_m.czy_wygral())
        self.assertEqual(self.pionek_m.podaj_plec(),"M")
        self.assertEqual(self.pionek_m.podaj_gracza().podaj_nazwe(),self.gracz.podaj_nazwe())
        self.assertEqual(self.pionek_m.podaj_pole_drugiego_pionka().podaj_polozenie(),self.pole_2.podaj_polozenie())
        self.assertEqual(len(self.pionek_m.gdzie_moze_budowac_kopole()),0)
        self.assertEqual(len(self.pionek_m.gdzie_moze_budowac()), 8)
        self.assertEqual(len(self.pionek_m.gdzie_sie_moze_poruszyc()), 8)





    def test_gracz(self):
        self.assertEqual(self.gracz.podaj_nazwe(),"gracz1")
        self.assertEqual(self.gracz.podaj_pionek("k").podaj_plec(),"K")
        self.assertEqual(self.gracz.podaj_drugi_pionek(self.gracz.podaj_pionek("k")).podaj_plec(), "M")
        self.assertFalse(self.gracz.czy_oba_bez_ruchu())
        self.pionek_m.mozliwosc_poruszania()
        self.assertTrue(self.pionek_m.czy_moze_sie_ruszac)





if __name__ == "__main__":
    unittest.main()

















