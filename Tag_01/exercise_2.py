from math import sqrt

def eucl(p1, p2, q1, q2):

    func = sqrt((p1 - q1)**2 + (p2 - q2)**2)
    return func

print(f"Entfernung der Vektoren = " + str(eucl(2, 3, 10, 8)))