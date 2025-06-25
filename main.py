#les module 
from time import sleep 

panier = []
#fonction pour afficher le contenu du panier 
def content(panier):
     a = 1
     print(f"Votre panier contient les produits suivants :")
     for produit in panier :
         print(f"\n{a}-{produit}")
         a += 1
     print("Affichage du panier terminé")
    
#fonction de l'accueil.
def app_run (panier) :
    sleep(0.5)
    while True :
        try :
            sleep(1)
            print("veuillez choisir :")
            choix = int(input(" 1-Pour ajouter un produit.\n 2-Pour retirer un produit.\n 3-Afficher le panier.\n 4-Quitter\n    >"))
            if choix == 1 :
                return ajouter(panier)
            elif choix == 2 :
                return  retirer (panier) 
            elif choix  == 3 :
                return afficher (panier)
            elif choix == 4 :
                if panier == [] :
                    print("Votre panier est vide .")
                    print("À bientôt !!")
                else :
                    content(panier)
                    print("À bientôt !!")    
            else :
                return app_run(panier)
        except ValueError: 
            print("VEUILLEZ ENTRER UN NOMBRE VALIDE.")            
#fonction pour  ajouter  un  produit a liste .   
def ajouter (panier):
    sleep(0.5)
    ajout = input("Quel produit voulez-ajouter ? \n    >")
    while ajout == "":
        sleep(0.2)
        ajout = input("Quel produit voulez-ajouter ? \n    >")
    panier.append(ajout)
    sleep(0.5)
    print("Produit ajouter avec succès !!\n")
    content (panier)
    while True:
        try :
            print ("\nVeuillez choisir")
            choix = int(input("1-Pour ajouter  un autre produits \n2-Pour retourner au menu.\n 3-Quitter\n    >"))
            if choix == 1 :
                return ajouter (panier)
            elif choix == 2 :
                return app_run (panier)    
            elif choix == 3 :
                exit("À bientôt")
        except ValueError: 
            print("Veuillez entrer un nombre valide")       
#fonction pour retirer un produit du panier 
def retirer(panier):
    sleep(0.5)
    if panier == [] :
        print("Votre panier est vide")
        sleep(0.5)
        while True :
            try : 
                print("Choisissez :")
                choix = int(input("1-Pour ajouter un produit.\n2- Pour revenir au menu \n 3-Quitter\n    >")) 
                if choix == 1 :
                    return ajouter (panier)
                elif choix == 2 :
                    return app_run(panier)
                elif choix  == 3 :
                    exit("À bientôt") 
            except ValueError:    
                print("Veuillez entrer un nombre valide.")  
                return retirer(panier)    
    else :
        retir = input("Quel produit voulez-retirer?\n    >") 
        while retir == "":
            print("Vous devez écrire le nom d'un produit")
            retir = input("Quel produit voulez-retirer?\n    >") 
        if not retir in panier :
            print("Ce produit n'est pas dans votre panier.")
            return app_run(panier)
        else :
            panier.remove (retir) 
            print(f"Le produit : {retir} à été retiré de votre panier.") 
            content (panier)
            return app_run(panier)

#fonction pour  afficher  le contenu  du panier 
def afficher (panier) :
    sleep(0.5)
    if panier == [] :
        print("Votre panier est vide")
        sleep(0.5)
        while True :
            try : 
                sleep(0.5)
                print("Choisissez :")
                choix = int(input("1-Pour ajouter un produit.\n2- Pour revenir au menu \n 3-Quitter\n    >")) 
                if choix == 1 :
                    return ajouter (panier)
                elif choix == 2 :
                    return app_run(panier)
                elif choix  == 3 :
                    exit("À bientôt") 
            except ValueError:    
                print("Veuillez entrer un nombre valide.")  
                return afficher(panier)       
    else :
        content(panier) 
        return app_run(panier)       
    
app_run(panier)        
