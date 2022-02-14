import math

#Global variables



"""
MAX_SIZE = 125 # Mivel 2500 / 20 = 125 igy egyszerubb szamolni
DOBOZ_SIZE = 1

current_size = MAX_SIZE
GLOBALP = 0 # GLOBAL POINTER

distance = 0
utvonal = []
teres_counter = 0
"""


#stores the coordinates

raktar = () # Coordinates of the raktar

coordinates1 = []
coordinates2 = []

class Repulo:
    def __init__(self,MAX_SIZE,DOBOZ_SIZE,raktar,k):
        self.MAX_SIZE = MAX_SIZE
        self.DOBOZ_SIZE = DOBOZ_SIZE
        self.current_size = MAX_SIZE
        self.raktar = raktar
        self.kordinatak = k

        self.distance = 0
        self.utvonal = []
        self.teres_counter = 0

        self.pointer = 0


    def increaseGP(self):
        self.pointer += 1


    def emptyAll(self):
        if(self.current_size >= self.kordinatak[self.pointer][2]):
            self.kordinatak[self.pointer][2] -= self.current_size  # empties itself
            self.increaseGP()
        else:
            self.kordinatak[self.pointer][2] -= self.current_size  # empties itself


    def goHome(self):
        self.current_size = self.MAX_SIZE  # reloads
        self.teres_counter += 1  # increases teres
        self.distance += calcDist(x1=self.raktar[0], y1=self.raktar[1], x2=self.kordinatak[self.pointer][0],
                                  y2=self.kordinatak[self.pointer][1])
        self.utvonal.append(-1)  # hazamegy


    def dropGift(self):
        self.current_size -= self.kordinatak[self.pointer][2]
        self.kordinatak[self.pointer][2] = 0
        self.increaseGP()

    def __del__(self):
        print("Object has been destroyed")

def read_data(filename):
    coordinates = []
    global  raktar
    with open(filename, 'r') as f:
        lines = f.readlines()
        raktar = tuple([int(i) for i in lines[0].split(',')])
        # print(f'raktar: {raktar[0]} :: {raktar[1]}')
        for line in lines[1:21]:
            l = [int(i) for i in line.split(',')]
            print(l)
            coordinates1.append(l)
            coordinates2.append(l)


def calcDist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def main(flag= False,coordinates = []):
    print("Kordasdas", coordinates)
    repulo = Repulo(125,1,raktar,coordinates)

    while(repulo.pointer < 19):

        if (len(repulo.utvonal) > 0):
            if (repulo.utvonal[-1] == -1):
                repulo.distance += calcDist(x1=repulo.raktar[0], y1=repulo.raktar[1], x2=repulo.kordinatak[repulo.pointer][0], y2=repulo.kordinatak[repulo.pointer][1])
            else:
                repulo.distance += calcDist(x1=repulo.kordinatak[repulo.pointer][0], y1=repulo.kordinatak[repulo.pointer][1],
                                               x2=repulo.kordinatak[repulo.utvonal[-1]][0], y2=repulo.kordinatak[repulo.utvonal[-1]][1])

        print(coordinates)
        repulo.utvonal.append(repulo.pointer)
        print("Hely: ",repulo.pointer,"repulo raktar: ", repulo.current_size, " Ajandekok", repulo.kordinatak[repulo.pointer][2])
        if repulo.current_size > repulo.kordinatak[repulo.pointer][2]:
            repulo.dropGift()
        elif repulo.current_size == repulo.kordinatak[repulo.pointer][2]:
            repulo.emptyAll()
            repulo.goHome()
        else:
            if flag:
                repulo.goHome()
            else:
                repulo.emptyAll()
                repulo.goHome()


        if (repulo.pointer >= 18 and repulo.kordinatak[18][2] == 0):
            # go home
            repulo.teres_counter += 1
            repulo.distance += calcDist(x1=raktar[0], y1=raktar[1], x2=repulo.kordinatak[18][0], y2=repulo.kordinatak[18][1])
            repulo.utvonal.append(-1)
            break

    print("Teresek szama: ", repulo.teres_counter)
    print("Megtet ut kmben: ", repulo.distance * 1000)
    print("Utvonal: ", repulo.utvonal)
    if not flag:
        print(repulo.current_size)
        coordinates2[-1].append(repulo.current_size) # 2. feladatohoz, de meg bele kell irni a fajlbais

    del repulo

if __name__ == "__main__":
    read_data("radar")
    main(False,coordinates1)
    main(True,coordinates2)
