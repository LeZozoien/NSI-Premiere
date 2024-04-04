import math

class Object:

    def __init__(self, position) -> None:
        self.center = position
        self.VERTICES = [(1, 1, 1),(1, 1, -1),
                    (1, -1, 1),(1, -1, -1),
                    (-1, 1, 1),(-1, 1, -1),
                    (-1, -1, 1),(-1, -1, -1)]

        self.EDGES = [(0, 1), (0, 2), (0, 4),
                (1, 3), (1, 5), (2, 3),
                (2, 6), (3, 7), (4, 5),
                (4, 6), (5, 7), (6, 7)]

        self.FACES = [(0, 1, 2), (1, 3, 2),
                (2, 3, 6), (3, 7, 6),
                (6, 7, 4), (7, 5, 4),
                (4, 5, 0), (5, 1, 0),
                (0, 2, 4), (6, 4, 2),
                (1, 5, 3), (3, 5, 7),]
        
        self.rotated_vertices = [(1, 1, 1),(1, 1, -1),
                                 (1, -1, 1),(1, -1, -1),
                                 (-1, 1, 1),(-1, 1, -1),
                                 (-1, -1, 1),(-1, -1, -1)]
        
        self.rotation = [0, 0, 0]

    def project_point(self, index, camera, focal):

        # Variables : 
        camx, camy, camz = camera
        pointx, pointy, pointz = self.rotated_vertices[index]

        # Camera to view:
        pointx -= camx
        pointy -= camy
        pointz -= camz
        pointx = -pointx
        pointz = -pointz

        if pointx == 0:
            return None

        # Calculate projected coords
        xproj = focal*pointy/pointx
        yproj = focal*pointz/pointx

        return xproj, yproj
    
    def project_edge(self, index, camera, focal):
        a, b = self.project_point(self.EDGES[index][0], camera, focal), self.project_point(self.EDGES[index][1], camera, focal)
        if (a == None) or (b == None): return None
        else: return a, b

    def calculate_normal(self, index):
        a, b, c = self.rotated_vertices[self.FACES[index][0]],self.rotated_vertices[self.FACES[index][1]],self.rotated_vertices[self.FACES[index][2]]

        u = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
        v = (c[0]-a[0], c[1]-a[1], c[2]-a[2])

        normx = u[1]*v[2] - u[2]*v[1]
        normy = u[2]*v[0] - u[0]*v[2]
        normz = u[0]*v[1] - u[1]*v[0]

        return -normx, -normy, -normz
    
    def project_face(self, index, camera, focal):
        normal = self.calculate_normal(index)
        if normal[0]>0:
            a = self.project_point(self.FACES[index][0], camera, focal)
            b = self.project_point(self.FACES[index][1], camera, focal)
            c = self.project_point(self.FACES[index][2], camera, focal)
            if (a == None) or (b == None) or (c == None): return None
            else:return a, b, c
        else:return None

    def rotate_vertices(self, vertices, camera_rotation):
        camera_rotation = camera_rotation[0]*math.pi/180, camera_rotation[1]*math.pi/180, camera_rotation[2]*math.pi/180
        rotated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            rx, ry, rz = camera_rotation

            # Rotation autour de l'axe x
            x_new = x
            y_new = y * math.cos(rx) - z * math.sin(rx)
            z_new = y * math.sin(rx) + z * math.cos(rx)

            # Rotation autour de l'axe y
            x = x_new * math.cos(ry) + z_new * math.sin(ry)
            y = y_new
            z = -x_new * math.sin(ry) + z_new * math.cos(ry)

            # Rotation autour de l'axe z
            x_new = x * math.cos(rz) - y * math.sin(rz)
            y_new = x * math.sin(rz) + y * math.cos(rz)
            z_new = z

            rotated_vertices.append((x_new, y_new, z_new))

        return rotated_vertices

    def rotate_around_center(self, vertices, rotation):
        rotation = rotation[0]*math.pi/180, rotation[1]*math.pi/180, rotation[2]*math.pi/180
        rotated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            rx, ry, rz = rotation

            # Rotation autour de l'axe x
            x_new = x
            y_new = y * math.cos(rx) - z * math.sin(rx)
            z_new = y * math.sin(rx) + z * math.cos(rx)

            # Rotation autour de l'axe y
            x = x_new * math.cos(ry) + z_new * math.sin(ry)
            y = y_new
            z = -x_new * math.sin(ry) + z_new * math.cos(ry)

            # Rotation autour de l'axe z
            x_new = x * math.cos(rz) - y * math.sin(rz)
            y_new = x * math.sin(rz) + y * math.cos(rz)
            z_new = z

            rotated_vertices.append((x_new, y_new, z_new))

        return rotated_vertices

    def apply_rotation(self, camera_rotation):
        self.rotated_vertices = self.rotate_around_center(self.VERTICES, self.rotation)
        self.rotated_vertices = self.rotate_vertices(self.rotated_vertices, camera_rotation)

def normalize_vector(vec):
    x, y, z = vec
    dist = (x**2+y**2+z**2)**0.5
    return (x/dist, y/dist, z/dist)

def dot_product(vec_a, vec_b):
    return vec_a[0]*vec_b[0] + vec_a[1]*vec_b[1] + vec_a[2]*vec_b[2]

def add_vectors(vec_a, vec_b):
    return vec_a[0]+vec_b[0], vec_a[1]+vec_b[1], vec_a[2]+vec_b[2]

Camerapos = [4, 0, 0]
Camerarot = [0, 0, 0]
focal = 1
zoom = 1
lightDir = normalize_vector([2, 0, 3])

cube = Object([0, 0, 0])

for vertex_idx in range(len(cube.VERTICES)):
    print(cube.project_point(vertex_idx, Camerapos, focal))

for edge_idx in range(len(cube.EDGES)):
    print(cube.project_edge(edge_idx, Camerapos, focal))

for face_idx in range(len(cube.FACES)):
    print(cube.project_face(face_idx, Camerapos, focal))


import pygame

pygame.init()

background_colour = (0, 0, 0)
windowSize = (1920, 1080)
halfSize = windowSize[0]//2, windowSize[1]//2

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()

running = True
clk = pygame.time.Clock()

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:

                case pygame.K_p: zoom *= 1.1
                case pygame.K_m: zoom /= 1.1

                case pygame.K_i: Camerarot[2] += 5
                case pygame.K_k: Camerarot[2] -= 5
                case pygame.K_l: Camerarot[1] += 5
                case pygame.K_j: Camerarot[1] -= 5
                case pygame.K_o: Camerarot[0] += 5
                case pygame.K_u: Camerarot[0] -= 5
            
    screen.fill(background_colour)

    cube.rotation = [(cube.rotation[0])%360, (cube.rotation[1])%360, (cube.rotation[2])%360]
    cube.apply_rotation(Camerarot)
    for face_idx in range(len(cube.FACES)):
        projected = cube.project_face(face_idx, Camerapos, focal)
        if projected != None:
            projected = [[projected[0][0]*100*zoom+halfSize[0], projected[0][1]*100*zoom+halfSize[1]], [projected[1][0]*100*zoom+halfSize[0], projected[1][1]*100*zoom+halfSize[1]], [projected[2][0]*100*zoom+halfSize[0], projected[2][1]*100*zoom+halfSize[1]]]

            # Shading
            normal = cube.calculate_normal(face_idx)
            normal = normalize_vector(normal)
            
            color = dot_product(normal, lightDir)
            if color<0:color = 0.1
            if color>1:color = 1

            color = [color*255, color*255, color*255]

            # Drawing
            pygame.draw.polygon(screen, color, projected, 0)
            pygame.draw.polygon(screen, (0, 255, 255), projected, 3)


    for edge_idx in range(len(cube.EDGES)):
        proj = cube.project_edge(edge_idx, Camerapos, focal)
        proj = [[proj[0][0]*100*zoom+halfSize[0], proj[0][1]*100*zoom+halfSize[1]], [proj[1][0]*100*zoom+halfSize[0], proj[1][1]*100*zoom+halfSize[1]]]
        pygame.draw.line(screen, (0, 150, 100), proj[0], proj[1])

    pygame.display.flip()
    clk.tick(60)