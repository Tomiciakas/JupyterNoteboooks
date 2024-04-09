A = 70

def printA():
    print("As esu nauja printA() funkcija")
    print("Dar vienas pakeitimas")
    print("Paskutinis pakeitimas")

class Vehicle():
    def __init__(self, P, R):
        self.P = P
        self.R = R
class Car(Vehicle):
    def __init__(self, P, R, S):
        super().__init__(P, R)
        self.S = S

    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimas vietas"
        return Txt

# test = Car(P= 'pavadinimas', R=5000, S= 5)
# print(test.GetSeats())
class Bus(Vehicle):
    def __init__(self, P, R, S):
        super().__init__(P, R)
        self.S = S

    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu "
        return Txt

# test = Bus(P= 'pavadinimas', R=5000, S= 40)
# print(test.GetSeats())
class Train(Vehicle):
    def __init__(self, P, R, S):
        super().__init__(P, R)
        self.S = S

    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu"
        return Txt

    # test = Train(P= 'pavadinimas', R=5000, S= 100)
    # print(test.GetSeats())



class Txtreader():
    """
    labai kieta mano klase         
    """
    def __init__(self, failo_pavadinimas):
        self.failo_pavadinimas = failo_pavadinimas
        self.I = []
        self.U = []
        self.j = []
        self.P = []   

    def skaitytojas(self):
        """
        labai kieta mano funkcija         
        """
        failas = open(self.failo_pavadinimas, mode='r') 
        tekstas = failas.readlines()
        failas.close()

        for eilute in tekstas[1:]:  #praleidziam 0 eilute, nes ten yra tik tekstas ir ji mum nereikalinga
            u = float(eilute.split(';')[0])
            self.U.append(u)
            i = float(eilute.split(';')[1])
            self.I.append(i)
            J = float(eilute.split(';')[2])
            self.j.append(J)
            p = float(eilute.split(';')[3])
            self.P.append(p)

    def maksimalusP(self):
        maximumas = max(self.P)
        return maximumas
    
    def pce(self):
        maximumas = self.maksimalusP()
        ats = maximumas / 1000 *100
        return ats   