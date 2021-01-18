# Surface S = l*h*p

def surface(x,y,z):
    ma_surface = x*y*z
    return ma_surface

l=30
h=40
p=10

resultat = surface(l,h,p)

print("ma surface est de ", resultat)
print("ma moitie de surface est de ", resultat/2)
