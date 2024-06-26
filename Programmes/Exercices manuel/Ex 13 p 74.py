villes_capitales = {
    'albanie': 'Tirana',
    'allemagne': 'Berlin',
    'andorre': 'Andorre-la-Vieille',
    'autriche': 'Vienne',
    'belgique': 'Bruxelles',
    'biélorussie': 'Minsk',
    'bosnie-herzégovine': 'Sarajevo',
    'bulgarie': 'Sofia',
    'chypre': 'Nicosie',
    'croatie': 'Zagreb',
    'danemark': 'Copenhague',
    'espagne': 'Madrid',
    'estonie': 'Tallinn',
    'finlande': 'Helsinki',
    'france': 'Paris',
    'grèce': 'Athènes',
    'hongrie': 'Budapest',
    'irlande': 'Dublin',
    'islande': 'Reykjavik',
    'italie': 'Rome',
    'lettonie': 'Riga',
    'liechtenstein': 'Vaduz',
    'lituanie': 'Vilnius',
    'luxembourg': 'Luxembourg',
    'macédoine du nord': 'Skopje',
    'malte': 'La Valette',
    'moldavie': 'Chisinau',
    'monaco': 'Monaco',
    'monténégro': 'Podgorica',
    'norvège': 'Oslo',
    'pays-bas': 'Amsterdam',
    'pologne': 'Varsovie',
    'portugal': 'Lisbonne',
    'république tchèque': 'Prague',
    'roumanie': 'Bucarest',
    'royaume-uni': 'Londres',
    'russie': 'Moscou',
    'saint-marin': 'Saint-Marin',
    'serbie': 'Belgrade',
    'slovaquie': 'Bratislava',
    'slovénie': 'Ljubljana',
    'suède': 'Stockholm',
    'suisse': 'Berne',
    'ukraine': 'Kiev',
    'vatican': 'Vatican',
}

def get_capitale(pays:str):
    pays = pays.strip().lower()
    if pays in villes_capitales: return villes_capitales[pays]
    else: return None

def get_pays(capitale:str):
    for pays in villes_capitales:
        if villes_capitales[pays] == capitale:
            return pays
    return None


demande = input("Quelle ville ?")
print(get_pays(demande))