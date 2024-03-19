#############################################################################################
#                          creation des fonction
#############################################################################################


#1. creation des deux tableau
def adperson(tab, nom, prenom, sexe, date): #fonction d'ajout de personnes
    #print("creation du tableau des personnes....")
    #ce tableau servira repertorirer les personnes
    tab.append([nom, prenom, sexe, date]) #on rajouter toutes ces valeur dans un tableau
    #print(tab)
    print("\n")
    return(tab)
    
def adparent(tab, enfant, parent): #ajout du deuxième tableau
    #print("creation du tableau lien parents enfant...")
    #ce tableau fera le lien entre l'indice d'une personne et l'indice de sont parent ex :
    # si sur une me ligne on as [1, 3] cela veut dire que la personne avec l'indice 1 aura pour parent la perosnne avec l'indice 3
    tab.append([enfant, parent])
    return(tab)


#2. affichage du tableau
def printtab(): #affichage du tableau ad person
    print("affichage du tableau de personnes : \n")
    for person in tab : #pour toute personnes dans le tableau
        print(person) #on les personnes ligne par ligne


#3. selectionner num personne
def selectnum(tab): 
    print("\n selection du numero de l'indice et lien avec la personnes :")
    for num in range(len(tab)) : #pour tout les numero (qui correspondent a l'indice du parents) allant jusqu'a la taille du tableau
        print(num, tab[num]) #on affiche sont indice a coté les infos de la personne lier a cette infice

#4. link personne tab
#def linkparent(tabpeople, tablink):
    #if 



    


##################################################################
#                           apl de fonction
#################################################################

print('lancement du programme ...\n')
tab=[]
# valeur en brut d'ajout de personne
adperson(tab, 'rueda lucantis', 'jade', 2, (2004,3,3))
adperson(tab, 'jean', 'coline', 2, (1971,7,12))
adperson(tab, 'dupouy', 'bernard', 1, (2007,6,14))
adperson(tab, 'nemesis', 'noah', 1, (2004, 2, 2))
adperson(tab, 'overlord', 'ju', 1, (2004, 2, 2))

##
printtab()
selectnum(tab)
##

#valeur en brut ajout d eien
adparent(tab, 0, 1)
adparent(tab, 2, 1)

print("\n \nfin du programme.")
