#############################################################################################
#                          creation des fonction
#############################################################################################


#1. creation des deux tableau
def adperson(tab, nom, prenom, sexe, date):
    tab.append([nom, prenom, sexe, date]) #on rajouter toutes ces valeur dans un tableau
    #print(tab)
    return(tab)
    
def adparent(tab, enfant, parent):
    tab.append([enfant, parent])
    print(tab)
    return(tab)


#2. affichage du tableau
def printtab():
    for person in tab :
        print(tab)






    
##################################################################
#                           apl de fonction
#################################################################

tab=[]
adperson(tab, 'rueda lucantis', 'jade', 2, (2004,3,3))
adperson(tab, 'jean', 'coline', 2, (1971,7,12))
adperson(tab, 'dupouy', 'bernard', 1, (2007,6,14))

printtab()

#adparent(tab, 0, 1)

