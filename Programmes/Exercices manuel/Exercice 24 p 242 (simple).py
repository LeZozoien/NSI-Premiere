sandwiches=[250,180,350,400]
boissons=[50,0,150,130]
 
def associer_boissons_sandwiches(boissons,sandwiches):

    boissons_triees= sorted(boissons, reverse=True)
    sandwiches_tries= sorted(sandwiches)
    sorted()

    paires = []

    for i in range(len(boissons_triees)):
        paires.append((boissons_triees[i], sandwiches_tries[i]))

    return paires
 
print(associer_boissons_sandwiches(boissons, sandwiches))
