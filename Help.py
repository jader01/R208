#R208

#SUJET 2

#Fonctions

#question 1
def ajouter (tab,nom,prénom,sexe,datedenaissance):
    temp = [len(tab),nom,prénom,sexe,datedenaissance]
    tab.append(temp)

#question 2
def afficher (tab):  #permet d'afficher un tableau et non une unique valeur de tableau
    for i in range (len(tab)): 
        print (tab[i]) 

#question 3
def séléction (tab,prénom):
    for i in range (len(tab)):
        if tab[i][2] == prénom:
            x = tab[i][0]
    return x

#question 4
def ajouterlien (lien,id_parent,id_enfant):
    temp = [id_parent,id_enfant]
    lien.append(temp)

#question 5
def ascendant (tab,id_enfant):
    res = []
    for i in range (len(tab)) :
        if tab [i][1] == id_enfant :
            id_parent = tab [i][0]
            res.append(id_parent)
            temp = ascendant(tab,id_parent)
            res = res + temp
    return res        

#question 6
def descendant (tab,id_parent):
    res = []
    for i in range (len(tab)) :
        if tab [i][0] == id_parent :
            id_enfant = tab [i][1]
            res.append(id_enfant)
            temp = descendant(tab,id_enfant)
            res = res + temp
    return res     

#question 7
def freresoeur(tab,id_enfant):
    res = []
    for i in range (len(tab)):
        if tab[i][1] == id_enfant:
            id_parent = tab [i][0]
    for i in range (len(tab)):
        if id_parent == tab [i][0] and tab[i][1] != id_enfant:
            temp = tab [i][1]
            res.append(temp)
    return res        

#question 8
def tri (tab,id1,id2,id3):
    print("lancement de la question 8.................")
    res = []
    newtab = []
    againtab = []
    res.append(id1)
    res.append(id2)
    res.append(id3)
    for p in range (len(res)):
        for i in range (len(tab)):
            if tab[i][0]==res[p]:
                newtab.append(tab[i][1])
    print (newtab)
    newtab.sort()
    print (newtab)
    for l in range (len(newtab)):
        for k in range (len(tab)):
            if newtab[l]==tab[k][1]:
                print (newtab[l])
                againtab.append(tab[k])
    print (againtab)

            

#    for i in range (len(tab)):
#        if tab[i][0] == id1 or tab[i][0] == id2 or tab[i][0] == id3:
#            res.append(tab[i])
 

#question 9
#def tri_age (tab,id1,id2,id3):
#    res = []
#    for i in range (len(tab)):
#        if tab[i][0] == id1 or tab[i][0] == id2 or tab[i][0] == id3:
#            res.append(tab[i])
#    for i in range (len(res)):
#        mini = res[i][4]
#        for j in range (i+1, len(res)):
#            if res[j]<res[mini]:
#                mini = res[j][4]
#        res[i][4], res[mini] = res[mini], res[i][4]
#    return res 

#question 10
def menu(tab):
    print ("SUJET 2") 
    print("1.Afficher le tableau")
    print("2.Ajouter une ligne au tableau des personnes")
    print("3.Ajouter une nouevelle ligne dans le tableau des liens")
    print("4.Sélectionner le numéro d'une personne")
    print("5.Connaître ses ascendants")
    print("6.Connaître ses descendants")
    print("7.Connaître ses frères et soeurs")
    print("8.Trier dans l'ordre alphabétique")
    print("9.Trier du plus âgé au plus jeune")
    choix = input("Que voulez-vous faire ? ")


#Programme principale

mytab = []

ajouter(mytab,'Dupre','Richard','M',(1978,5,27))
ajouter(mytab,'Garnier','Emilie','F',(1946,6,12))
ajouter(mytab,'Vidal','Edouard','M',(1995,12,3))
ajouter(mytab,'Mertz','Natasha','F',(1988,12,21))
ajouter(mytab,'Moen','Rebecca','F',(1968,6,3))
ajouter(mytab,'Becker','Ollie','F',(1967,10,11))

#print('Le tableau des personnes est :') 
#afficher(mytab)

y = séléction(mytab,'Emilie')
#print("Séléction d'un numéro :",y)

lien = []

ajouterlien(lien,1,2)
ajouterlien(lien,2,3)
ajouterlien(lien,3,4)
ajouterlien(lien,0,2)
ajouterlien(lien,0,5)

#print('Le tableau des liens de parenté est :') 
#afficher(lien)

x = ascendant(lien,4)      #attention mettre le bon tableau
#print('Ses ascendants sont :',x)

w = descendant(lien,1)
#print('Ses descendants sont :',w)

z = freresoeur(lien,2)
#print ("Ses frères et soeurs sont :",z)

m = tri(mytab,0,3,1)
print("q8")

#a = tri_age(mytab,0,1,2)
#print("q9",a)
#print (mytab[0][1])
print (mytab[0][4][0])
