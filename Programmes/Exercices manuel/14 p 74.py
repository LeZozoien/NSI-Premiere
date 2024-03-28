personnes = {
    "Jean Aymar": {"taille": 178,
                   "pays": "USA",
                   "age": 31},
    "Clio Patre": {"taille": 179,
                   "pays": "Portugal",
                   "age": 32},
}

def get_age(name:str):
    if name in personnes: return personnes[name]["age"]
    else: return None

def get_mean_height():
    tot_height = 0
    for personne in personnes:
        tot_height += personnes[personne]["taille"]
    tot_height /= len(personnes)
    return tot_height