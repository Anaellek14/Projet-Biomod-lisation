import matplotlib.pyplot as plt
import math


figure, axes = plt.subplots()

axes.set_title('Nombre de bactéries fécales vivantes')
axes.set_xlabel('Jour du traitement')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')
#Les axes du graphique en ligne et le graphique sont nommés

for souris in range (0,96) :    #On doit avoir une courbe pour chaque souris

   fINPUT = open('data_real.csv', 'r')
   fFécal = open('sortie fécal', 'w')
   fCécal = open('sortie cécal', 'w')
   fIleal = open('sortie ileal', 'w')
   #Le fichier contenant les données de l'expérience est ouvert et les fichiers de sortie (qui contiendront les données nécessaires aux 3 graphiques sont crées
   fFécal.close()
   fCécal.close()
   fIleal.close()
   #Afin de ne pas avoir trop de fichiers ouverts en même temps, les fichiers de sortie sont refermés

   ligne = fINPUT.readline()    #Lecture de la première ligne du fichier d'entrée
   liste = []   #Création de la liste qui contiendra les différents éléments du fichier d'entrée
   xgraphligne = []     #Création de la liste qui contiendra les données de l'axe des abscisses
   ygraphligne = []     #Création de la liste qui contiendra les données de l'axe des ordonnées


   while ligne != '':   #Cette boucle est effectuée tant que la ligne n'est pas vide, donc tant qu'il reste des lignes non-lues à notre fichier d'entrée
       ligne = fINPUT.readline()
       ligne = ligne.replace('\n', '') # On retire le retour à la ligne
       liste = ligne.split(';')


       if len(liste) != 11:  # Le nombre de colonnes
           break

       listeSortie = []
       listeSortie2 = []
       listeSortie3= []


       localisation = str(liste[2])

       if localisation == 'fecal':  # On ne prend que les fécales
           fFécal = open('sortie fécal', 'a')
           listeSortie = [liste[4]] +[liste[5]] + [liste[7]] + [liste[8]]  # On ne réécrit que les listes "fécales"
           résultat = ';'.join(listeSortie)  # On assemble les termes de ces listes pour refaire un csv
           lS = résultat.split(';')
           fFécal.write(résultat + '\n')  # On écrit ces listes dans un fichier de sortie en ajoutant le retour à la ligne


       elif localisation == 'cecal' :
           fCécal = open('sortie cécal', 'a')
           listeSortie2 = [liste[4]] +[liste[5]] + [liste[7]] + [liste[8]]
           résultat2 = ';'.join(listeSortie2)  # On assemble les termes de ces listes pour refaire un csv
           fCécal.write(résultat2 + '\n')  # On écrit ces listes dans un fichier de sortie en ajoutant le retour à la ligne
           fCécal.close()


       else :
           fIleal = open('sortie ileal', 'a')
           listeSortie3 = [liste[4]] + [liste[5]] + [liste[7]] + [liste[8]]
           résultat3 = ';'.join(listeSortie3)  # On assemble les termes de ces listes pour refaire un csv
           fIleal.write(résultat3 + '\n')  # On écrit ces listes dans un fichier de sortie en ajoutant le retour à la ligne
           fIleal.close()


       sourisID = int(lS[0].replace('ABX', ''))

       Jour = float(lS[2])
       BactériesFécales = math.log10(float(lS[3]))



       if sourisID==souris :
           xgraphligne.append(Jour)
           ygraphligne.append(BactériesFécales)

       axes.plot(xgraphligne, ygraphligne)
       fFécal.close()


figure.savefig('Nombre de bactéries fécales vivantes chez les 2 groupes de souris en fonction du jour de traitement',
                  dpi=400)


fINPUT.close()


figure, axes = plt.subplots()

axes.set_title('Nombre de bactéries cécales vivantes')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')


fCécal = open('sortie cécal', 'r')  #On réouvre le fichier créé précedemment cette fois en lecture seule
ligneCécal= fCécal
ygraphvioloncécalABX = []
ygraphvioloncécalPlacebo = []


while ligneCécal != '':
   ligneCécal = fCécal.readline()
   ligneCécal = ligneCécal.replace('\n', '')  # On retire le retour à la ligne
   listeCécal = ligneCécal.split(';')

   if len(listeCécal) != 4:  # Le nombre de colonnes
       break

   BactériesCécales = math.log10(float(listeCécal[3]))

   if listeCécal[1] == 'ABX':  # Si les souris sont ABX, on ajoute leur nb de bactéries dans la liste pour les souris ABX
       ygraphvioloncécalABX.append(BactériesCécales)
   else:
       ygraphvioloncécalPlacebo.append(BactériesCécales)  # Sinon, on l'ajoute dans la liste pour les souris placebo

axes.violinplot([ygraphvioloncécalABX, ygraphvioloncécalPlacebo])


figure.savefig('Violon cécal', dpi = 400)


figure, axes = plt.subplots()


axes.set_title('Nombre de bactéries iléales vivantes')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')


fIléal = open('sortie ileal', 'r')
ligneIléal= fIléal
ygraphviolonIléalABX = []
ygraphviolonIléalPlacebo = []


while ligneIléal != '':
   ligneIléal = fIléal.readline()
   ligneIléal = ligneIléal.replace('\n', '')  # On retire le retour à la ligne
   listeIléal = ligneIléal.split(';')

   if len(listeIléal) != 4:  # Le nombre de colonnes
       break


   BactériesIléales = math.log10(float(listeIléal[3]))


   if listeIléal[1] == 'ABX':  # Si les souris sont ABX, on ajoute leur nb de bactéries dans la liste pour les souris ABX
       ygraphviolonIléalABX.append(BactériesIléales)
   else:
       ygraphviolonIléalPlacebo.append(BactériesIléales)  # Sinon, on l'ajoute dans la liste pour les souris placebo


axes.violinplot([ygraphviolonIléalABX, ygraphviolonIléalPlacebo])


figure.savefig('Violon iléal', dpi = 400)
