from cryptography.fernet import Fernet
import glob

Choix = input(" Choisisez votre mode 1 (Crypter) ou 2 pour (Déscrypter) : ")
if Choix == "1" :

    ## Generation de la clef ##
    user_key = input("Générer une nouvelle clé (o/n) ")

    if user_key.lower() == 'o':
        user_key = Fernet.generate_key()
        with open('key.key', 'wb') as f:
            f.write(user_key)
    else:
        with open('key.key', 'rb') as f:
            user_key = f.read()
        
    ## Encryptage ##
    files = glob.glob("*.txt")
    for file in files:
        with open(file, 'rb') as f:
            data = f.read()
        fernet = Fernet(user_key)
        encrypted = fernet.encrypt(data)
        with open(file, 'wb') as f:
            f.write(encrypted)

## Décryptage ##
if Choix == "2" :
    decriptefil = input("Entrez la clef de décryptage : ")

    file = glob.glob('*.txt')
    for files in file:
        with open(files, 'rb') as f:
            data = f.read()
        fernet = Fernet(decriptefil)
        decrypted = fernet.decrypt(data)
        with open(files, 'wb') as f:
            f.write(decrypted)
