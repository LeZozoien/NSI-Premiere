def distance(a:tuple, b:tuple)->float|int: # a.

    # Vérification du type de a et b
    if not isinstance(a, (tuple, list)):
        raise TypeError
    if not isinstance(b, (tuple, list)):
        raise TypeError
    
    # Vérification de la longueur de a et b
    if len(a) != 2:
        raise ValueError
    if len(b) != 2:
        raise ValueError
    
    # Vérification du type des valeurs dans b et a
    if not isinstance(a[0], (int, tuple)) or not isinstance(a[1], (int, tuple)) or not isinstance(b[0], (int, tuple)) or not isinstance(b[1], (int, tuple)):
        raise TypeError


    # Code principal de calculation de la distance
    xa, ya = a
    xb, yb = b
    distance = ((xa-xb)**2+(ya-yb)**2)**0.5 # --> sqrt((bx-ax)²+(by-ay)²)

    # Vérification du type de distance
    if not isinstance(distance, (int, float)):
        raise Exception

    return distance

def get_size(points:tuple[tuple]): # b.
    xmin, ymin, xmax, ymax = 0
    for point in points:
        point_x, point_y = point
        if point_x > xmax : xmax = point_x
        if point_x < xmin : xmin = point_x
        if point_y > ymax : ymax = point_y
        if point_y < ymin : ymin = point_y

    size_x = xmax-xmin
    size_y = ymax-ymin

    return size_x, size_y

def get_length(points:tuple[tuple]): # c.
    dist = 0
    for i in range(1, len(points)):
        dist += distance(points[i-1], points[i])
    return dist