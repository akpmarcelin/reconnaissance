import cv2 as cv
import os
import main_face as mf
import face_recognition as fs
# Fonction pour la détection des images
    # Fonction pour le cadre
def cadre(image, color) :
    # Classificateur
    classi = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
    
    image_gris = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    caract =  classi.detectMultiScale(image_gris, 1.1, 8)
   
    for (x, y, w, h) in caract :
        cv.rectangle(image, (x, y), (x+w, y+h), color, 2)
        cv.putText(image, 'Face', (x, y-4), cv.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv.LINE_AA)
        visage = image[y:y+h, x:x+w]
       
    return image, visage

# Fonction de détection
def detect(image) :
    color = {"blue" : (255,0,0), "red" : (0,0,255), "green" : (0,255,0)}
    image, visage = cadre(image,color["blue"])
    return image, visage

def recon(y, visage_tempo, num) :
    chemin = mf.images_chemin(0, num)
    visage_origi = os.path.join(chemin, f"{num}_visage.jpg")
    visage_origi =  fs.load_image_file(visage_origi)
    visage_tempo =  fs.load_image_file(visage_tempo)
    
    vo_encode = fs.face_encodings(visage_origi)
    vt_encode = fs.face_encodings(visage_tempo)
    
    vo_encode = vo_encode[0]
    vt_encode = vt_encode[0]
    
    resultat = fs.compare_faces(vt_encode,vo_encode)
    
    if resultat[0] : 
        print("Vous êtes dans le régistre")
        
    else :
        print("Vous n'êtes pas dans le régistre")   
