from cmath import pi


print("Saisir un angle en rad")
x=float(input())
dd= (x*180)/pi
d=int(dd)
m=(dd-d)*60
s=(dd-d-m/60)*3600
print ("Cet angle vaut " + str(d) + "° " + str(round(m)) + " min " + str(round(s)) + " s")