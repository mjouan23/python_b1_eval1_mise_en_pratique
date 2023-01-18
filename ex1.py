# EV 1 - Mise en pratique
# 1ère
# a reçoit 8
a = 8
# b reçoit 6 (8-2)
b = a - 2
# c reçoit 12 (4+6+2)
c = 4 + b + 2
# On écrase la valeur initiale de a pour la remplacer par 0 (12 modulo de 2, il reste 0 car 12 est pair)
a = c % 2
print(a)
print(b)
print(c)


# 3ème
a = -1
b = a + 3
c = -1 + b + 2
a = c % 2
print(a)
print(b)
print(c)