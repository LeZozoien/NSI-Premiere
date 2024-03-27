import pygame

class Cube:
    def __init__(self) -> None:
        
        self.VERTICES = [(1, 1, 1),(-1, 1, 1),
                        (1, 1, -1),(-1, 1, -1),
                        (1, 3, 1),(-1, 3, 1),
                        (1, 3, -1),(-1, 3, -1)]

        self.EDGES = [(0, 1), (0, 2), (0, 4),
                    (1, 3), (1, 5), (2, 3),
                    (2, 6), (3, 7), (4, 5),
                    (4, 6), (5, 7), (6, 7)]

        self.FACES = [(0, 1, 2), (1, 3, 2),
                    (4, 6, 5), (5, 6, 7),
                    (0, 2, 4), (2, 6, 4),
                    (5, 3, 1), (5, 7, 3),
                    (7, 6, 2), (7, 2, 3),
                    (1, 0, 5), (0, 4, 5),]
    
    def get_rotated(self, anglex, angley, anglez):
        pass


pygame.init()
BGCOLOR = (0, 0, 0)
WINDOWSIZE = (1920, 1080)
HALFSIZE = (WINDOWSIZE[0]//2, WINDOWSIZE[1]//2)
screen = pygame.display.set_mode(WINDOWSIZE)
screen.fill(BGCOLOR)
pygame.display.set_caption('Window')
pygame.display.flip()

cube = Cube()
scene_objects = [cube]

def project_point(point_x, point_y, point_z, focal)->tuple[float|int]:

    projected_x = point_x * focal / (point_y+focal)
    projected_y = point_z * focal / (point_y+focal)

    return projected_x, projected_y

def project_edges(object_edges:tuple[int], object_vertices:tuple[float|int], focal:float)->list[list[tuple[float|int]]]:
    projected_edges = []
    for edge in object_edges:
        point_a, point_b = object_vertices[edge[0]], object_vertices[edge[1]]
        a_projected = project_point(point_a[0], point_a[1], point_a[2], focal)
        b_projected = project_point(point_b[0], point_b[1], point_b[2], focal)
        projected_edges.append((a_projected, b_projected))
    return projected_edges

def get_face_vectors(point_1, point_2, point_3):
    vec1x = point_2[0] - point_1[0]
    vec1y = point_2[1] - point_1[1]
    vec1z = point_2[2] - point_1[2]
    vec1 = [vec1x, vec1y, vec1z]
    vec2x = point_3[0] - point_1[0]
    vec2y = point_3[1] - point_1[1]
    vec2z = point_3[2] - point_1[2]
    vec2 = [vec2x, vec2y, vec2z]

    return vec1, vec2

def calculate_normal(point_1, point_2, point_3):

    a, b = get_face_vectors(point_1, point_2, point_3)

    normx = a[1]*b[2] - a[2]*b[1]
    normy = a[2]*b[0] - a[0]*b[2]
    normz = a[0]*b[1] - a[1]*b[0]
    normal = [normx, normy, normz]
    return normal



running = True
drawing = True
zoom_factor = 100
focal = 1

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

    if drawing:

        for object in scene_objects:

            to_draw_edges = project_edges(object.EDGES, object.VERTICES, focal)

            for face in object.FACES:
                point_A, point_B, point_C = object.VERTICES[face[0]], object.VERTICES[face[1]], object.VERTICES[face[2]]
                face_normal = calculate_normal(point_A, point_B, point_C)
                if face_normal[1] < 0:
                    projected_A, projected_B, projected_C = [project_point(point_A[0], point_A[1], point_A[2], focal),
                                                            project_point(point_B[0], point_B[1], point_B[2], focal),
                                                            project_point(point_C[0], point_C[1], point_C[2], focal)]
                    projected_A, projected_B, projected_C = [(projected_A[0]*zoom_factor + HALFSIZE[0], projected_A[1]*zoom_factor + HALFSIZE[1]),
                                                            (projected_B[0]*zoom_factor + HALFSIZE[0], projected_B[1]*zoom_factor + HALFSIZE[1]),
                                                            (projected_C[0]*zoom_factor + HALFSIZE[0], projected_C[1]*zoom_factor + HALFSIZE[1])]
                    print(projected_A, projected_B, projected_C)
                    pygame.draw.polygon(screen, (0, 255, 255), [projected_A, projected_B, projected_C])


            for edge in to_draw_edges:
                ax, ay = edge[0][0], edge[0][1]
                bx, by = edge[1][0], edge[1][1]
                ax, ay, bx, by = ax*zoom_factor, ay*zoom_factor, bx*zoom_factor, by*zoom_factor
                pygame.draw.line(screen, (255, 255, 255), (ax+HALFSIZE[0], ay+HALFSIZE[1]), (bx+HALFSIZE[0], by+HALFSIZE[1]))


    drawing = False
    
    pygame.display.flip()