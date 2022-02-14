import math
import copy

"""

Infoprog 2022 levelező forduló - B kategória

név : Veres Z. Benedek
iskola : Selye János Gimnázium, Komárom

"""


#############################################
# Fontosabb változók

raktar = () # A raktár kordinátái
coordinates = [] # Az összes többi kordináta

#############################################


class Repulo:
    """

    A repülőgépet szimbolizáló osztály, minden lépés benne van, amit a repülő meg  tud tenni:
                - Kirakja a szállítmányát
                - Kirakja az összes szállítmányát
                - Felvesz szállítmányt

    """
    def __init__(self,MAX_SIZE,DOBOZ_SIZE,raktar,k):
        """

        :param MAX_SIZE: A repülő legnagyobb tárhelye
        :param DOBOZ_SIZE: Egy doboz nagysága ( a feladatban, meg van adva a tömege, de elosztva megkapjuk hogy mennyi darabot tudunk tárolni)
        :param raktar: A raktár kordinátái
        :param k: Az összes kordináták kópiája

        distance -- A repülő megtett útja
        teresCounter -- Hányszor tért a repülő vissza a bázisra
        pointer -- Éppen melyik kordinátára mutatunk a kordinatak

        """
        self.MAX_SIZE = MAX_SIZE
        self.DOBOZ_SIZE = DOBOZ_SIZE
        self.current_size = MAX_SIZE
        self.raktar = raktar
        self.kordinatak = k

        self.distance = 0
        self.utvonal = []
        self.teresCounter = 0

        self.pointer = 0


    def increaseGP(self):
        """

        Megnöveli  a pointer értékét, így a következő kordinátára mutat

        """
        self.pointer += 1


    def emptyAll(self):
        """

        Kiüríti a rakományát

        """

        if(self.current_size >= self.kordinatak[self.pointer][2]):

            self.kordinatak[self.pointer][2] -= self.current_size  # empties itself
            self.increaseGP()

        else:

            self.kordinatak[self.pointer][2] -= self.current_size  # empties itself


    def goHome(self):
        """

        Hazatér és feltölti a raktárát, valamint kiszámolja a hazautazási távolságot

        """
        self.current_size = self.MAX_SIZE
        self.teresCounter += 1
        self.distance += calcDist(x1=self.raktar[0], y1=self.raktar[1], x2=self.kordinatak[self.pointer][0],
                                  y2=self.kordinatak[self.pointer][1])
        self.utvonal.append(-1)


    def dropGift(self):
        """

        Lead ajándékokat, de nem feltétlen teljesen üríti a raktárát

         """
        self.current_size -= self.kordinatak[self.pointer][2]
        self.kordinatak[self.pointer][2] = 0
        self.increaseGP()


    def __del__(self):
        """

        Kitörli az objektumot, hogy ne maradj szabad memória

        """
        pass



def readData(filename):
    """

    Beolvassa az adatokat:
        -- A raktárba elmenti a raktár kordinátát (ami a file első sora)
        -- a coordinates listába pedig, az összes többi kordinátát bele értve a kiegészítendőt is

    """
    global  raktar

    with open(filename, 'r') as f:

        lines = f.readlines()
        raktar = tuple([int(i) for i in lines[0].split(',')])

        for line in lines[1:21]:

            l = [int(i) for i in line.split(',')]
            coordinates.append(l)



def writeData(filename):
    """

    Átírja az állományát az új, frissített adatokkal

    """
    with open(filename,"w") as f:

        f.write(f"{raktar[0]},{raktar[1]}\n")

        for i in coordinates:

            f.write(f"{i[0]},{i[1]},{i[2]}\n")



def calcDist(x1,y1,x2,y2):
    """

    A Pitagorasz-tétel segítségével kiszámolja a távolságot 2 pont között.

    """
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)



def main(coords,flag= False):
    """

    A fő függvény, 2szer futt le elöször, amikor a flag False, akkor az első és második feladatot teljesíti.
    Második lefutáskor a flag True, akkor pedig a harmadik feladatot teljesíti

    """
    repulo = Repulo(125,1,raktar,coords) # Létrehozza a repülő objektumot, mind két esetben újat, hogy ne keveredjenek a kordináták adatai

    print("###############################")

    while(repulo.pointer < 19): # A ciklus 19-szer fut le, mivel a raktáron és a hiányos kordinátán kívül  18 kordináta van, ahova el kell menni

        if (len(repulo.utvonal) > 0): # Ha előző lépésben a raktárban volt, akkor kiszámolja az onnantól számított távolságot, másképp az előző ponttól számított távolságot

            if (repulo.utvonal[-1] == -1):

                repulo.distance += calcDist(x1=repulo.raktar[0], y1=repulo.raktar[1], x2=repulo.kordinatak[repulo.pointer][0],
                                            y2=repulo.kordinatak[repulo.pointer][1])
            else:

                repulo.distance += calcDist(x1=repulo.kordinatak[repulo.pointer][0], y1=repulo.kordinatak[repulo.pointer][1],
                                            x2=repulo.kordinatak[repulo.utvonal[-1]][0], y2=repulo.kordinatak[repulo.utvonal[-1]][1])

        repulo.utvonal.append(repulo.pointer) # Utvonal mentés

        if repulo.current_size > repulo.kordinatak[repulo.pointer][2]: # Ha a rakomány több, mint a lerakandó ajándék, akkor ürít és megy tovább

            repulo.dropGift()

        elif repulo.current_size == repulo.kordinatak[repulo.pointer][2]: # Ha egyforma, akkor ürít és megy haza

            repulo.emptyAll()
            repulo.goHome()

        else:

            if flag and repulo.current_size != repulo.MAX_SIZE: # A kevesebb és az első feladatot csinálja, akkor ürít és haza, másképpen csak hazamegy

                repulo.goHome()

            else:

                repulo.emptyAll()
                repulo.goHome()


        if (repulo.pointer >= 18 and repulo.kordinatak[18][2] == 0): # Ha a végén járunk, akkor hazatérünk

            repulo.teresCounter += 1
            repulo.distance += calcDist(x1=raktar[0], y1=raktar[1], x2=repulo.kordinatak[18][0], y2=repulo.kordinatak[18][1])
            repulo.utvonal.append(-1)

            break

    print("Térések száma: ", repulo.teresCounter)
    print("Megtett út: ", int(repulo.distance * 1000),"km")
    #print("Útvonal: ", repulo.utvonal)
    if not flag:

        coordinates[-1].append(repulo.current_size) # Kiegészíti a megfelelő számmal a hiányzó értéket az utlsó kordinátában
        writeData("raktar.txt")

    del repulo



if __name__ == "__main__":

    readData("raktar.txt")

    main(copy.deepcopy(coordinates),False)
    main(copy.deepcopy(coordinates),True)
