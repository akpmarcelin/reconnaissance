#importation des bibliothèques
import cv2 as cv
import os
import cascada as ca

# Fonction pour créer le dossier d'une image
def creation_chemin(chemin) :
    if not os.path.exists(chemin) :
        os.makedirs(chemin)
# Fonction pour créer le chemin d'accès aux images    
def images_chemin(x,numero) :
    # Enrégistrement dans notre base
    if x == 0 :
        chemin = os.path.join('images_enreg',f"{numero}")
        
    elif x == 1 : 
        chemin = os.path.join('images_tempo', f"{numero}")  
        
    return chemin    
# Fonction pour recupérer les images         
def capture_photo(y,num) :
    capture = cv.VideoCapture(0)
    # Vérification de l'ouverture de la caméra
    if not capture.isOpened() :
        print("Erreur d'ouverture de la caméra.\n")
        return
    # Caméra ouverte
    while True :    
        val , imgtab0 = capture.read()
        if not val :
            print("Impossible de capturer une image.")
            break
        imgtab, visage = ca.detect(imgtab0)
        cv.imshow("'c' pour prendre une photo ou 'q' pour quitter.",imgtab)
        
        touche = cv.waitKey(1)
        if touche == ord('c') :
            chemin = images_chemin(y,num)
            creation_chemin(chemin)
            chemin = os.path.join(chemin, f"{num}.jpg")             
            cv.imwrite(chemin,imgtab0)
            visage_gris = cv.cvtColor(visage, cv.COLOR_BGR2GRAY)
            chemin = images_chemin(y,num)
            chemin = os.path.join(chemin, f"{num}_visage.jpg")
            cv.imwrite(chemin, visage_gris)
            print("Prise réussie.")
            break
        
        elif touche == ord('q') :
            break
        
    return visage_gris, num   
    # Fermeture de la caméra  
    capture.release()
    cv.destroyAllWindows    
             