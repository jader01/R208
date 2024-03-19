#############################################################################################
#                          creation des fonction
#############################################################################################


#1. creation des deux tableau
def adperson(tab, nom, prenom, sexe, date): #fonction d'ajout de personnes
    #ce tableau servira repertorirer les personnes
    tab.append([nom, prenom, sexe, date]) #on rajouter toutes ces valeur dans un tableau
    #print(tab)
    return(tab)
    
def adparent(tab, enfant, parent): #ajout du deuxième tableau
    #ce tableau fera le lien entre l'indice d'une personne et l'indice de sont parent ex :
    # si sur une me ligne on as [1, 3] cela veut dire que la personne avec l'indice 1 aura pour parent la perosnne avec l'indice 3
    tab.append([enfant, parent])
    print(tab)
    return(tab)


#2. affichage du tableau
def printtab(): #affichage du tableau ad person
    for person in tab : #pour toute personnes dans le tableau
        print(person) #on affiche seulement la lgiende de la personne


#3. selectionner num personne
def selectnum(tab): 
    for num in range(len(tab)) : #pour tout les numero (qui correspondent a l'indice du parents) allant jusqu'a la taille du tableau
        print(num) #on affiche sont indice


#4. link personne tab
#def linkparent():
    


##################################################################
#                           apl de fonction
#################################################################

tab=[]
adperson(tab, 'rueda lucantis', 'jade', 2, (2004,3,3))
adperson(tab, 'jean', 'coline', 2, (1971,7,12))
adperson(tab, 'dupouy', 'bernard', 1, (2007,6,14))
adperson(tab, 'nemesis', 'noah', 1, (2004, 2, 2))
adperson(tab, 'overlord', 'ju', 1, (2004, 2, 2))

printtab()
selectnum(tab)

adparent(tab, 0, 1)


