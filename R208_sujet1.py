#############################################################################################
#                          creation d'une fonction
#############################################################################################



#1. creation fonction ajout de valeur
def enregistrevaleur(tab,date,heure,idcap,val,donnee):
    tab.append([tab, date, heure, idcap, val, donnee]) #on rajouter toutes ces valeur dans un tableau
    return(tab)

#2. afficher dans ordre d'insert 
def odreinsert(tab):
    for i in range(len(tab)):
        for j in range(tab[i]):
            print(tab[i][j]+'\t')

#3. filtrer tab pour ligne idcapteur 
def filtreid(tab,idcap):
    result=[]
    
    for i in range(len(tab)): 
        if tab[i][2]==id:
            result.append(tab[i])
    return result
    
#4. filtre tab pour date
def filtredate(tab,date):
    result=[]

    for i in range(len(tab)): 
        if tab[i][0]==id:
            result.append(tab[i])
    return result
    
#5. trie odre chrono date heure

def rangmintab(tab,p):
    res=p
    for i in range (p,len(tab)):
        if tab [i]<tab[res]:
            res=i
        return res

def tri(tab):
    for i in range(len(tab)-1):
        rmin=rangmintab(tab,i)
        permut(tab,i,rmin)


def permut(tab,a,b):
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

            
    
##################################################################
#                           apl de fonction
#################################################################

tab = []
menu(tab)
#enregistrevaleur(tab,(2,3,2022),(10,50,1),8,22.4,'TEMP')
odreinsert(tab)
t1=filtreid(tab,'8')
print(t1)
t2=filtredate(t1,(3,3,2002))
print(t2)
t3=filtredate(filtreid(tab,'8'),(3,3,2022))
