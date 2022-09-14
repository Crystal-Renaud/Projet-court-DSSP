import numpy as np
import math

# hbplus a extrait les h-bond

num_res_donneur =[] #numero du résidu donneur
name_res_donneur = [] #son nom
num_res_accept =[] #numéros résidu accepteur
name_res_accept = [] #son nom

#extraire résidue
with open("new_2hbb.hb2", "r") as filing:
    for line in filing:
        if line.startswith("A00"):
            res_don_numb = int(line [1:5])
            res_don_name = line[7:9].strip() #strip sert à enlever les espaces
            res_acc_numb = int(line[15:19])
            res_acc_name = line[21:23].strip()
            num_res_donneur.append(res_don_numb)
            name_res_donneur.append(res_don_name)
            num_res_accept.append(res_acc_numb)
            name_res_accept.append(res_acc_name)

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
        bridge_p.append([i_consecutif[i]])

for i in range(len(i_consecutif)):
    if i_consecutif[i][0][1] == (i_consecutif[i][2][1]+2):
        bridge_antip.append([i_consecutif[i]])

