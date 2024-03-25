def distance(a:tuple, b:tuple): # a.
    xa, ya = a
    xb, yb = b
    distance = ((xa-xb)**2+(ya-yb)**2)**0.5
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