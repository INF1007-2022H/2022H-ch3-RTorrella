from cmath import pi


print("Saisir la valeur des degrés")
d=int(input())

print("Saisir la valeur des minutes")
m=int(input())

print("Saisir la valeur des secondes")
s=int(input())

dd= d + m/60 + s/3600
r=(dd*pi)/180
print("Cet angle vaut " + str(r) + " rad")