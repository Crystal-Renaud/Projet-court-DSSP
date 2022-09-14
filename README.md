# Projet-court-DSSP

## Pré-requis
Il faut d'abord télécharger une protéine sur [PDB](https://www.rcsb.org/).   
Puis obtenir le programme [HBPLUS](https://www.ebi.ac.uk/thornton-srv/software/HBPLUS/) ainsi que l'autorisation pour l'utiliser.   

Traiter le format PDB de la protéine par HBPLUS depuis votre terminal. Pour lancer HBPLUS il faut enlever le format .gz en faisant "tar -xvzf hbplus.tar.gz" dans votre terminal. Puis pour démarrer le programme la première fois, il faut taper "make". Pour le lancer, il faut entrer dans HBPLUS "cd hbplus" et noter "./hbplus".   
Le programme vous demandera où vous voulez mettre le output puis le nom du fichier que vous voulez traiter (ne pas oublier de mettre .pdb). Le fichier contenant les liaisons hydrogène (fichier .hb2) se trouvera où vous l'avez indiquer. 

## Environnement 
Installer [miniconda](https://docs.conda.io/en/latest/miniconda.html).
Utiliser Python. 

## Lancement du programme
Lancer le programme : python3 code.py 
Pour changer le input (la protéine), il faut changer le nom du fichier .hb2 dans le code (après le with open). 
