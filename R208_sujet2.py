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



#5. connaitre les ascendant a partir du numero
def findparent(adparent:list, id:int)-> list: #les :[] servent a spécifier le type attendu et le --> sert a spécifier ce que tu veux en sortie 
    print("lancement de la fonction trouver les parents et acendant : \n")

    #print("le tableau de l'asso indice enfant et indice parent est :\n")
    #print(adparent)

    #print("le tableau d'association indice + personne est : \n")
    #print(selectnum)

    
    tabparent=[] #tableau stockage du resulstat
    for elm in adparent : #pour tous les element dans le tableau ad parent (du coup ça prend petite liste par petite liste)
        if id ==elm[0] : #on associe l'id passer en paramètre au première element des petites 
            indiceparent=elm[1] #on associe id a l'id du parent trouver pour l'enfant demander
            tabparent.append(indiceparent) #on rajoute au tableau de résultat l'id du parent
            
            tabparent += findparent(adparent, indiceparent) # on concatène le tableau de resultat on lui rajoutant a chaque fois (avec +=) le resultat de notre fonction que l'on re r'apelle
    print("les ascendant de l'id choisi sont : \n", tabparent, "\n")

    return(tabparent)

#6. connaitre les descandant a partir d'un infice

def findenfant(adparent:list, id: int)-> list:
    tabenfant=[]
    #print("on lance la fonction pour trouver la descandance ...")

    for elm in adparent :
        if id==elm[1]:
            indiceenfant=elm[0]
            tabenfant.append(indiceenfant)

            tabenfant += findenfant(adparent, indiceenfant)
    #print("la descandance de ", id, "est :")
    
    print("la desceandance est composé de : \n", tabenfant, "\n")
    return(tabenfant)


#7. trouver le lien entre les frère et les soeur

def lienfrsr(adparent, id:int):
    fretsr=[] #pour stocker le resultat final lien frère et soeur
    idparent=[] #pour stoker les parents pour faire le lien plus tard
    
    #print("le t'ableau utiliser est :", adparent)

    print("lancement de la fonction retrouver frère et soeur \n")
    for elm in adparent: #on cherche a nouveaux les différentes partie dans adprent
        if id==elm[0]: #si l'id correspond à l'indice d'un enfant
            idparent.append(elm[1]) #alors on rajoute 
    #print("l'enfant qui a pour id", elm[0], "a pour parent les personne avec l'id", idparent) #juste pour voirs l'avancer de la fonctoin

    for p in idparent: #on parcours pour la première fois les element dans ma table d'id parent
        for elm2 in adparent : #et on parcours une nouvelle fois la liste pour trouver les élement
            if id!=elm2[0] and p==elm2[1]: #si l'id de l'enfant n'est pas = a l'id et que l'id du parent est égale à celui trouver avant
                fretsr.append(elm2[0]) #on ajoute l'élement du frère dans le tableau de resultat
                print("l'enfant qui a pour id", id, "et qui a pour parents", idparent, "a pour frère ou soeur", fretsr, "\n")


#8. a partir du numéro de personne affiche les info des personnes classer par nom

def infopeople(tabpersonneetid:list, id1:int, id2:int, id3:int):
    #print("le tableau de personne utilisé est", tabpersonneetid)
    print("l'id choisi est ", id1)
    stockid=[]

    stockid.append(id1)
    stockid.append(id2)
    stockid.append(id3)

    for elm in tabpersonneetid : #pour tous les element dans le tableau d'association personne = id
        if elm[0]==id1 : #si l'indice correspon à l'id choisi
            print("la personne correspondant à l'indice", id1, "est :", elm[1]) #on affiche la personne associé

    #for elm in tabpersonne :
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
adperson(tab, 'martin', 'simon', 1, (1920, 2, 2))
adperson(tab, 'oda', 'evan', 1, (2005, 2, 2))



# apl de fonction
printtab()
tabindice=selectnum(tab)
print("resultat fonction selectnum", tabindice)
##

#valeur en brut ajout lien parent efnan 
tab2=[]
adparent(tab2, 0, 1)
adparent(tab2, 2, 1)
adparent(tab2, 1, 5)
adparent(tab2, 5, 4)
adparent(tab2, 0, 3)


#print("resultat fonction ad parent :", tab2)



# apl de fonction
findparent(tab2, 0) #on appelle la fonction de sortie des parents avec en paramètre le tbaleau asso--> idenfant | id parent, puis le tableau indice | personne, puis la valeur de l'enfant rechercher (qui a therme sera un input)
findenfant(tab2, 4) #apelle de la fonction permettant de trouver la descandance d'une personne

lienfrsr(tab2, 0)

infopeople(tabindice, 0, 1, 2)

print("\n \nfin du programme.")
