# Importation des bibliothèques et fonctions
import main_face
import cascada

# Entrée des informations
nom = (input("Entrez votre nom : \n")).upper()
prenom = (input("Entrez votre prénom : \n")).title()
# Vérification de l'appartenance à la liste des inscrits
with open("liste_inscrits.txt","+") as inscrit :
    a = 0
    Lignes = inscrit.readlines() 
    for ligne in Lignes :
        mots = ligne.split("_")
        if  (mots[0] == nom and mots[1] == prenom) :
            a = a + 1
            numero = int(mots[2])
            break
        numero = int(mots[2]) 
    # S'il y a appartenance, vérifier la concoordance des visages      
    if a == 1 : 
        print("Ce nom appartient bel et bien au régistre \n")
        print("Veuillez autoriser l'utilisation de la caméra pour une vérification faciale \n")
        reponse = (input("OUI ou NON : \n")).upper()
        if reponse == "OUI" : 
            visage_tempo, num = main_face.capture_photo(1,numero)
            cascada.recon(1, visage_tempo, num)         
            
    else :
       reponse = (input("Voulez-vous vous inscrire ? (OUI ou NON) \n")).upper()
       if reponse == "OUI":
           numero = numero + 1
           inscrit.write(nom+"_"+prenom+"_"+numero+"\n")
           main_face.capture_photo(0,numero)
           
       
            
