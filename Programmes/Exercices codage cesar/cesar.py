from random import randint

###
# 4 fonctions : 
# - encrypt_message()
# - decrypt_message()
# - encrypt_azerty()
# - decrypt_azerty()
# 
# Si une chaine est ajoutée, cela va encoder ou décoder ladite chaine, sinon il faudra spécifier un chemin de fichier à traiter
# 
# L'encrypteur génère une clé de 20 chiffres séparée en 5 clés de 4 chiffres pour effectuer 5 passages différents, cette clé est spécifiée à la fin du fichier
# 
# Je crève le plafond : Pour déchiffrer ce message, on peut utiliser une analyse statistique des lettres (le e est utilisé plus souvent que le z)
# car les lettres sont toujours remplacées par les mêmes charactères
###

def sans_accents(ligne):
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    i = 0
    while i < len(accent):
        ligne = ligne.replace(accent[i], sans_accent[i])
        i += 1
    return ligne


def encrypt_message(message: str | None = "", create_file:bool | None = False)->str:

    """Give it the message to encrypt or nothing to encrypt a txt file \n
    Returns the encrypted file and creates a txt file according to create_file"""

    alphabet_min = [chr(ord("a") + i) for i in range(26)]
    alphabet_maj = [chr(ord("A") + i) for i in range(26)]

    if message == "":
        fichier = open(input("Nom du fichier "), 'r', encoding='utf-8')
        chaine_a_coder = fichier.read()
        fichier.close()
    else:
        chaine_a_coder = message
    chaine_a_coder = chaine_a_coder.lower()
    chaine_a_coder = sans_accents(chaine_a_coder)

    resultat = ""

    cle = ""
    for i in range(20):
        cle += str(randint(0, 9))

    cles = []
    for j in range(5):
        cles.append(cle[j*4 : j*4+4])


    for passage in range(5):
        for index in range(len(chaine_a_coder)):
            try:
                resultat += alphabet_min[((alphabet_min.index(chaine_a_coder[index])) + int(cles[passage][index % len(cles[passage])])) % 26]
            except ValueError:
                try:
                    resultat += alphabet_maj[((alphabet_maj.index(chaine_a_coder[index])) + int(cles[passage][index % len(cles[passage])])) % 26]
                except ValueError:
                    resultat += chaine_a_coder[index]
        chaine_a_coder = resultat
        resultat = ""
        print(chaine_a_coder)

    if create_file == True:
        file_creation = open("Encrypted_message_"+str(cle)+".txt", 'w+')
        file_creation.write(chaine_a_coder + " " + cle)
        file_creation.close
    return chaine_a_coder + " " + cle


def decrypt_message(message: str | None = "", create_file : bool | None = False)->str:

    """Give it the message to decrypt or nothing to decrypt a txt file \n
    Returns the decrypted file and creates a txt file according to create_file"""

    if message == "":
        fichier = open(input("Nom du fichier "), 'r', encoding='utf-8')
        message = fichier.read()
        fichier.close()

    alphabet_min = [chr(ord("a") + i) for i in range(26)]
    alphabet_maj = [chr(ord("A") + i) for i in range(26)]

    chaine_a_decoder = message[0:-21]
    chaine_a_decoder = chaine_a_decoder.lower()

    resultat = ""

    cle = message[-20:]

    cles = []
    for j in range(5):
        cles.append(cle[j*4 : j*4+4])


    for passage in range(4, -1, -1):
        for index in range(len(chaine_a_decoder)):
            try:
                resultat += alphabet_min[((alphabet_min.index(chaine_a_decoder[index])) - int(cles[passage][index % len(cles[passage])])) % 26]
            except ValueError:
                try:
                    resultat += alphabet_maj[((alphabet_maj.index(chaine_a_decoder[index])) - int(cles[passage][index % len(cles[passage])])) % 26]
                except:
                    resultat += chaine_a_decoder[index]
        chaine_a_decoder = resultat
        resultat = ""
        
    if create_file == True:
        file_creation = open("Decrypted_message_" + str(cle)+ ".txt", 'w+')
        file_creation.write(chaine_a_decoder)
        file_creation.close
    return chaine_a_decoder



def Codage_azerty(message:str)->str:
    ch = "azertyuiopqsdfghjklmwxcvbn"
    alphabet = [chr(ord('a') + i) for i in range(26)]
    chaine_a_coder = message
    resultat = ""
    chaine_a_coder = chaine_a_coder.lower()

    for letter in chaine_a_coder:
        try:
            resultat += ch[alphabet.index(letter)]
        except ValueError:
            resultat += letter

    return(resultat)


def decodage_azerty(message:str)->str:
    ch = "azertyuiopqsdfghjklmwxcvbn"
    alphabet = [chr(ord('a') + i) for i in range(26)]
    chaine_a_coder = message
    resultat = ""
    chaine_a_coder = chaine_a_coder.lower()

    for letter in chaine_a_coder:
        try:
            resultat += alphabet[ch.find(letter)]
        except ValueError:
            resultat += letter

    return(resultat)


encrypt_message(create_file=1)