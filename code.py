import numpy as np
import math

# hbplus a extrait les h-bond

num_res_donneur =[] #numero du résidu donneur
num_res_accept =[] #numéros résidu accepteur

#extraire résidue
with open("new_2hbb.hb2", "r") as filing:
    for line in filing:
        if line.startswith("A00"):
            res_don_numb = int(line [1:5])
            res_acc_numb = int(line[15:19])
            num_res_donneur.append(res_don_numb)
            num_res_accept.append(res_acc_numb)

#création liste qui associe les listes d'extraction
h_bond = []

for i in range(len(num_res_donneur)): 
    h_bond.append([num_res_donneur[i], num_res_accept[i]])

#création des listes n_turn dans lesquels on introduira les résidus concernés
turn_3 = []
turn_4 = []
turn_5 = []

for i in range(len(h_bond)):
    x = abs(h_bond[i] [0] - h_bond[i] [1])
    if x == 3:
        turn_3.append([h_bond[i][0], h_bond[i][1]])
    elif x == 4:
        turn_4.append([h_bond[i][0], h_bond[i][1]])
    elif x == 5:
        turn_5.append([h_bond[i][0], h_bond[i][1]])

#création liste helix où il faut intégrer les turn consécutifs
helix = []

for i in range(len(turn_3)-1):
    if (turn_3[i][0]) == (turn_3[i+1][0] -1) and (turn_3[i][1]) == (turn_3[i+1][1] -1):
        helix.append([turn_3[i][0], turn_3[i][1]])
        if i < (len(turn_3)-2):
            if (turn_3[i+1][0] != (turn_3[i+2][0] -1)) or ((turn_3[i+1][1]) != (turn_3[i+2][1] -1)):
                helix.append([turn_3[i+1][0], turn_3[i+1][1]])

for i in range(len(turn_4)-1):
    if (turn_4[i][0]) == (turn_4[i+1][0] -1) and (turn_4[i][1]) == (turn_4[i+1][1] -1):
        helix.append([turn_4[i][0], turn_4[i][1]])
        if i < (len(turn_4)-2):
            if (turn_4[i+1][0] != (turn_4[i+2][0] -1)) or ((turn_4[i+1][1]) != (turn_4[i+2][1] -1)):
                helix.append([turn_4[i+1][0], turn_4[i+1][1]])

for i in range(len(turn_5)-1):
    if (turn_5[i][0]) == (turn_5[i+1][0] -1) and (turn_5[i][1]) == (turn_5[i+1][1] -1):
        helix.append([turn_5[i][0], turn_5[i][1]])
        if i < (len(turn_5)-2):
            if (turn_5[i+1][0] != (turn_5[i+2][0] -1)) or ((turn_5[i+1][1]) != (turn_5[i+2][1] -1)):
                helix.append([turn_5[i+1][0], turn_5[i+1][1]])

#on a les résidus qui forment une hélice dans hélix, on passe au feuillet.
#on peut enlever les résidus formant une hélice de la liste  h_bond pour la suite car 
#ils ne pourront pas faire en plus des liaisons avec un feuillet
#pour cela on fait en sorte que si h_bond n'est pas dans helix alors il va dans la nouvelle liste
h_bond2 = []
for i in range(len(h_bond)):
    if h_bond[i] not in helix:
        h_bond2.append(h_bond[i])

#on prend la liste h_bond2, on met les [i][0] dans l'ordre croissant afin de pouvoir
#voir les consécutifs

h_bond_tri = sorted(h_bond2)
i_consecutif = []

for i in range(len(h_bond_tri)-1):
     if (h_bond_tri[i][0]+1) == (h_bond_tri[i+1][0]) and (h_bond_tri[i][0]-1) == (h_bond_tri[i-1][0]):
        i_consecutif.append([h_bond_tri[i-1], h_bond_tri[i], h_bond_tri[i+1]])

#définition bridge parallèle où i-1 et i+1 ont le même j, ou un même i se lie avec j-1 et j+1 
#i = résidu donneur, j = résidu donneur
bridge_p = []
bridge_antip = []

for i in range(len(i_consecutif)):
    if i_consecutif[i][0][1] == (i_consecutif[i][2][1]-2):
        bridge_p.append(i_consecutif[i])

for i in range(len(i_consecutif)):
    if i_consecutif[i][0][1] == (i_consecutif[i][2][1]+2):
        bridge_antip.append(i_consecutif[i])

#une fois qu'on a nos bridges, on sait que un ladder correspond à deux bridges consécutifs
ladder_p = []
ladder_p2 = []
ladder_ap = []
ladder_ap2 =[]
for i in range(len(bridge_p)-1) :
    if (bridge_p[i][0][0]+1) == bridge_p[i+1][0][0]:
        ladder_p.append(bridge_p[i])
        ladder_p.append(bridge_p[i+1])

for ladder in range(len(ladder_p)):  #pour enlever les ladders qui serait en double
    if ladder_p[ladder] not in ladder_p2:
        ladder_p2.append(ladder_p[ladder])

for i in range(len(bridge_antip) - 1):
    if (bridge_antip[i][0][0]+1) == bridge_antip[i+1][0][0] :
        ladder_ap.append(bridge_antip[i])
        ladder_ap.append(bridge_antip[i+1])

for ladder in range(len(ladder_ap)):
    if ladder_ap[ladder] not in ladder_ap2:
        ladder_ap2.append(ladder_ap[ladder])

#un feuillet existe si deux ladders ont des résidus en commun

#pour afficher mes résultats comme DSSP, je dois avoir le nombre total de mes résidus
x1 = min(num_res_donneur)
x2 = min(num_res_accept)
x = min(x1, x2)

y1 = max(num_res_donneur)
y2 = max(num_res_accept)
y = max(y1, y2)

#j'extrais de la liste helix les résidus 
residu_helix = []

for i in helix:
    if i[0] not in residu_helix:
        residu_helix.append(i[0])
        if i[1] not in residu_helix:
            residu_helix.append(i[1])

residu_helix.sort()

#j'extrais de la liste ladder les résidus
residu_ladder = []
for i in ladder_p:
    if i[0][0] not in residu_ladder:
        residu_ladder.append(i[0][0])
        if i[1][0] not in residu_ladder:
            residu_ladder.append(i[1][0])
            if i[2][0] not in residu_ladder:
                residu_ladder.append(i[2][0])
                if i[0][1] not in residu_ladder:
                    residu_ladder.append(i[0][1])
                    if i[1][1] not in residu_ladder:
                       residu_ladder.append(i[1][1])
                       if i[2][1] not in residu_ladder:
                            residu_ladder.append(i[2][1])

for i in ladder_ap:
    if i[0][0] not in residu_ladder:
        residu_ladder.append(i[0][0])
        if i[1][0] not in residu_ladder:
            residu_ladder.append(i[1][0])
            if i[2][0] not in residu_ladder:
                residu_ladder.append(i[2][0])
                if i[0][1] not in residu_ladder:
                    residu_ladder.append(i[0][1])
                    if i[1][1] not in residu_ladder:
                       residu_ladder.append(i[1][1])
                       if i[2][1] not in residu_ladder:
                            residu_ladder.append(i[2][1])
residu_ladder.sort()

#affichage des numéros de résidu et de leur structure sous forme d'un "tableau" comme sur DSSP
print("numéro résidu  structure")
for i in range(x, y+1):
    if i in residu_helix:
        print(f"     {i}          hélice")
    elif i in residu_ladder:
        print(f"     {i}          ladder")
    else:
        print(f"     {i}           -")
print(i)
print( )
print("Un feuillet existe si les ladders ont un résidu en commun")
print(f"Liste des ladders parallèles: {ladder_p2}")
print(f"Liste des ladders anti-parallèles: {ladder_ap2}")