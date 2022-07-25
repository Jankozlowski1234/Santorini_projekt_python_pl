import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle



class Plansza():
    '''
    Klasa, która reprezentuje planszę gry, pamięta wszystkie pola, oraz jest odpowiedzialna za rysowanie planszy
    '''
    def __init__(self,slownik_pol,slownik_numerkow,gracz1,gracz2):
        self.slownik_pol=slownik_pol
        self.kolory={0:"gray",1:"b",2:"r",3:"y","p":"gray","k":"cyan","g1":"m","g2":"y","napis":"w"}
        self.slownik_numerkow=slownik_numerkow
        self.gracze={gracz1:"g1",gracz2:"g2"}
        self.gracz1=gracz1
        self.gracz2=gracz2


    def przygotoj_do_rysowania(self,text=""):
        '''
        Metoda rysujaca całą planszę, oraz legendę, ale nie wyświetlająca tego, co narysuje.
        :param text: tekst, który będzie wyświetlany na planszy
        :return: ax (wizuaizacja planszy, na której można jeszcze malować oraz ja wyświetlić)
        '''

        fig, ax = plt.subplots()
        ax.axis('off')
        ax.set(xlim=(-1, 9), ylim=(-2, 7))
        ax.add_patch(Rectangle((-0.5, -0.5), 6, 6, color="g"))

        for pole in self.slownik_pol.values():
            x, y = pole.podaj_polozenie()
            ax.add_patch(Rectangle((x, y), 0.9, 0.9,color=self.kolory[pole.podaj_wysokosc()]),)

            if pole.czy_kopola:
                ax.add_patch(Circle((x+0.5,y+0.5),0.3,color=self.kolory["k"]))

            if pole.czy_na_nim_pionek:
                ax.add_patch(Circle((x + 0.5, y + 0.5), 0.3, color=self.kolory[self.gracze[pole.podaj_kto_jest().nazwa]]))
                ax.text(x + 0.35, y + 0.35,pole.plec,color=self.kolory["napis"],size=10,fontname="Comic Sans MS")

        ax.text(1, 6.3, "SANTORINI",size=30,fontname="Comic Sans MS")
        ax.text(0, 5.7, text, size=10, fontname="Comic Sans MS")

        ax.text(6, 5, "Legenda:",fontname="Comic Sans MS")
        ax.add_patch(Rectangle((6, 3.7),0.7,0.7,color=self.kolory[0]))
        ax.text(7, 4, "Poziom 0",fontname="Comic Sans MS")
        ax.add_patch(Rectangle((6, 2.7), 0.7, 0.7, color=self.kolory[1]))
        ax.text(7, 3, "Poziom 1",fontname="Comic Sans MS")
        ax.add_patch(Rectangle((6, 1.7), 0.7, 0.7, color=self.kolory[2]))
        ax.text(7, 2, "Poziom 2",fontname="Comic Sans MS")
        ax.add_patch(Rectangle((6, 0.7), 0.7, 0.7, color=self.kolory[3]))
        ax.text(7, 1, "Poziom 3",fontname="Comic Sans MS")

        ax.add_patch(Circle((6.35, 0.2), 0.3, color=self.kolory["k"]))
        ax.text(7, 0.1, "Kopuła",fontname="Comic Sans MS")
        ax.add_patch(Circle((6.35, -0.5), 0.3, color=self.kolory["g1"]))
        ax.text(7, -0.65, self.gracz1,fontname="Comic Sans MS")
        ax.add_patch(Circle((6.35,-1.2),0.3, color=self.kolory["g2"]))
        ax.text(7, -1.3, self.gracz2,fontname="Comic Sans MS")
        return ax

    def rysuj_numerki(self,lista,text=""):
        '''
        Metoda, która 'dorysowuje' do planszy odpowiednie numery pól, i ją pokazuje graczom.
        :param lista: lista numerów pól, które mają być narysowane
        :param text: tekst, który będzie wyświetlany na planszy
        :return: Void
        '''
        ax = self.przygotoj_do_rysowania(text)
        for numerek in lista:
            x,y=self.slownik_numerkow[numerek]
            ax.text(x+0.6,y+0.6,str(numerek),fontname="Comic Sans MS",size=10)
        plt.show()
        return


    def rysoj(self,text=""):
        '''
        Metoda pokazująca graczom narysowany obraz planszy
        :param text: tekst, który będzie wyświetlany na planszy
        :return: Void
        '''
        self.przygotoj_do_rysowania(text)
        plt.show()

    def podaj_otoczenie(self,pole):
        '''
        Metoda, która dla podanego pola zwróci listę pól, które są w jego sąsiedztwie
        :param pole: pole, którego liste sąsiadów ma zwrócić
        :return: lista pól z otoczenia danego pola
        '''
        koordynaty=[i for i in range(5)]
        x,y=pole.podaj_polozenie()
        lista_pol=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if (x+i) in koordynaty:
                    if (y+j) in koordynaty:
                        if (i,j)!=(0,0):
                            lista_pol.append(self.slownik_pol[(x+i,y+j)])
        return lista_pol






