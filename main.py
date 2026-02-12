from cryptography.fernet import Fernet
import glob

Choix = input(" Choisisez votre mode (1) pour Crypter (2) pour Décrypter : ")
if Choix == "1" :

    ## Géneration de la clef ##
    user_key = input("Générer une nouvelle clé (o/n) ")

    if user_key.lower() == 'o':
        user_key = Fernet.generate_key()
        with open('key.key', 'wb') as f:
            f.write(user_key)
    else:
        try :
            with open('key.key', 'rb') as f:
                user_key = f.read() 
        except :
            pass
        
            
        
    ## Encryption ##
    try :
        files = glob.glob("**/*.txt", recursive=True, include_hidden=True)
        for file in files:
            with open(file, 'rb') as f:
                data = f.read()
            fernet = Fernet(user_key)
            encrypted = fernet.encrypt(data)
            with open(file, 'wb') as f:
                f.write(encrypted)
    except :
        print("Pas de clef déjà existante")

## Décryptage ##
if Choix == "2" :
    decriptefil = input("Entrez la clef de décryptage : ")
    try :
        files = glob.glob('*/**.txt', recursive=True, include_hidden=True)
        for file in files:
            with open(file, 'rb') as f:
                data = f.read()
            fernet = Fernet(decriptefil)
            decrypted = fernet.decrypt(data)
            with open(file, 'wb') as f:
                f.write(decrypted)
    except :
        print("La clef entrer n'est pas valide")
