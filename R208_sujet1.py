#############################################################################################
#                          creation d'une fonction
#############################################################################################



#1. creation fonction ajout de valeur
def enregistrevaleur(tab,date,heure,idcap,val,donnee): #enregistrement de valeur
    tab.append([tab, date, heure, idcap, val, donnee]) #on rajouter toutes ces valeur dans un tableau
    return(tab) 

#2. afficher dans ordre d'insert 
def odreinsert(tab):
    for i in range(len(tab)): # pour toutes les ligne jusqu'a la taille du tableau (len(tab)= la longueur du tableau) et (i= au nombre de ligne (a tout les tableau dans le tableau))
        for j in range(tab[i]): # pour toutes les collones "j" jusqu'a la taille de tous les element de i
            print(tab[i][j]+'\t') #on affiche i la ligne puis j la colone (le \'t' etant un tab pour l'affichage)

#3. filtrer tab pour ligne idcapteur 
def filtreid(tab,idcap): #filtrer les id avec en paramètre le tableau et les identifiant de capteur
    result=[] #tableau pour stocker le resultat
    
    for i in range(len(tab)): #pour toutes les ligne allant jusqu'a la longeur du tableau
        if tab[i][2]==id: # si pour toutes les lignes l'emplament de id est égale à idea
            result.append(tab[i]) #on rajoute la ligne dans notre table de resultat
    return result
    
#4. filtre tab pour date
def filtredate(tab,date): # on fait une fonction avec en paramètre le tableau puis la date
    result=[] #tableau pour 

    for i in range(len(tab)): #pour toutes les ligne allant jusqu'a la longeur du tableau
        if tab[i][0]=id: # si pour toutes les lignes l'emplament de id est égale à idea
            result.append(tab[i]) #on rajoute la ligne dans notre table de resultat
    return result
    
#5. trie odre chrono date heure (trie a bulle)

def rangmintab(tab,p): #on fait une fonction avec en paramètre le tableau puis une variable p
    res=p #on associe la variable p entrer en paramètre a 'res'
    for i in range (p,len(tab)): #pour toutes les lignes allant de p a la longeur du tableau 
        if tab [i]<tab[res]: # si la valeur de la ligne est inferieur au resultat passer en paramètre
            res=i #alors on assoscie la valeur du resultat passer en paramètre au numéro de ligne
        return res

def tri(tab): #fonction de trie
    for i in range(len(tab)-1): #comme on compare l'element a celui d'après, -1 car si on arrive a la fin il n'y a pas d'après
        rmin=rangmintab(tab,i) #on associe de le resultat de la fonction précédente a la variable rmin
        permut(tab,i,rmin) #on associe les variable a permute pour la fonction d'après


def permut(tab,a,b): #permut a en paramètre les paramètre ci dessus
    temp=tab[a]
    tab[a]=tab[b]
    tab[b]=temp

#6. squelette principal
def menu(tab):

    
    while True :
        print('a : si vous souhaiter enregistrer une nouvelle valeur')
        print('b : si vous souhaiter filtrer les valeurs')
        print('c : si vous souhaiter quitter et afficher le resultat')
        choix=input('que souhaiter vous faire ? (vous ne pouvais pas quitter sans entrer au moins une valeur) : ')
        
        if choix=='a':
            dateint=(input('entrer l\'anee \n '),input('entrer le mois \n '),input('entrer le jour\n '))
            print(dateint)

            heureint=(input('entrer l heure '),input('entrer les minutes '),input('entrer les secondes '))
            print(heureint)

            idcapint=input('entre l identifiant du capteur ')
            print(idcapint)
            
            valint=input('entrer la valeur enregistrer ')
            print(valint)
            
            typedon=input('entrer le type de donne correspondante \n')
            print(typedon)

            print(enregistrevaleur(tab,dateint,heureint,idcapint,valint,typedon))

        elif choix=='b':
            tri(tab)
            print(tab)
            

        elif choix=='c' :
            print('fin')
            print(enregistrevaleur(tab,dateint,heureint,idcapint,valint,typedon))  
            quit()
        
        else :
            print("entrer non valide\n")


def main():
    tab = []
    menu(tab)
    #enregistrevaleur(tab,(2,3,2022),(10,50,1),8,22.4,'TEMP')
    odreinsert(tab)
    t1=filtreid(tab,'8')
    print(t1)
    t2=filtredate(t1,(3,3,2002))
    print(t2)
    t3=filtredate(filtreid(tab,'8'),(3,3,2022))

    
##################################################################
#                           apl de fonction
#################################################################

main()
