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
    



#2. affichage du tableau
def printtab(): #affichage du tableau ad person
    print("affichage du tableau de personnes : \n")
    for person in tab : #pour toute personnes dans le tableau
        print(person) #on les personnes ligne par ligne


#3. selectionner num personne
def selectnum(tab): 
    print("\n selection du numero de l'indice et lien avec la personnes :")
    indiceparent=[] #tableau d'association du résultat
    for num in range(len(tab)) : #pour tout les numero (qui correspondent a l'indice du parents) allant jusqu'a la taille du tableau
        indiceparent.append([num, tab[num]]) #on affiche sont indice a coté les infos de la personne lier a cette indice
    print(indiceparent)

    return(indiceparent)
    


#4. faire des association du tableau parent enfant
def adparent(tab, enfant, parent):
    tab.append([enfant, parent])
    return(tab)


#5. connaitre les parent a partir du numero
def sortparent(adparent:list, selectnum:list, id:int)-> list: #les :[] servent a spécifier le type attendu et le --> sert a spécifier ce que tu veux en sortie 
    print("lancement de la fonction d'association : \n")

    print("le tableau de l'asso indice enfant et indice parent est :\n")
    print(adparent)

    print("le tableau d'association indice + personne est : \n")
    print(selectnum)

    #if adparent[1][1]==selectnum[1][0]:
        #print("CA MARCHE")
        #print(selectnum[0], "est l'enfant de", selectnum[1])

    tabparent=[] #tableau stockage du resulstat
    for elm in adparent : #pour tous les element dans le tableau ad parent (du coup ça prend petite liste par petite liste)
        if id ==elm[0] : #on associe l'id passer en paramètre au première element des petites 
            tabparent.append(elm[1]) #on rajoute au tableau le deuxième element de la petite liste (qui correspondra donc aux parents)
    print(tabparent)



 

    


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

# apl de fonction
printtab()
tabindice=selectnum(tab)
print("resultat fonction selectnum", tabindice)
##

#valeur en brut ajout lien parent efnan 
tab2=[]
adparent(tab2, 0, 1)
adparent(tab2, 2, 1)
#print("resultat fonction ad parent :", tab2)



# apl de fonction
sortparent(tab2, tabindice, 0)

print("\n \nfin du programme.")
