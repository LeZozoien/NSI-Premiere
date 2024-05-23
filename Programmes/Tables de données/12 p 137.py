def read_csv(file:str)->list[dict]:
    '''Renvoit une conversion du fichier csv spécifié en argument vers une liste de dictionnaires
    Attention : la première ligne du fichier csv doit contenir les titres'''
    
    with open("livre.csv", "r", encoding="utf-8") as file:
        db=[]
        data = file.read()
        entries = data.split("\n")
        first_line = entries[0]
        title = []
        for item in first_line.split(","):
                item = item.strip()
                title.append(item)
        entries = entries[1::]
        for entry in entries:
            line_dict = {}
            line=[]
            for item in entry.split(","):
                item = item.strip()
                line.append(item)
            for index, object in enumerate(title):
                line_dict[object] = line[index]
            db.append(line_dict)
    return db

if __name__ == "__main__":
    livres = read_csv("livre.csv")
    selection = []

    for livre in livres:
        if (livre["Auteur"] == "Kawabata" and livre["Titre"] != "Nuée d'oiseaux blancs")\
            or (livre["Titre"] == "Fondation" and livre["Auteur"] == "Asimov"):
            
            selection.append(livre)

    print(selection)
