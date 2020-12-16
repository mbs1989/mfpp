# Soit i parcourant une liste A
# Soit j parcourant une liste B
# Afficher "greeting" si i et j se rencontrent


for i in range(0,4):
    for j in range(3,0,-1):
        if i == j:
            print("greeting")
        else:
            print(i,j)