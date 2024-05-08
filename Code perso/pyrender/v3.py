# Basic 3d renderer (3rd version)
from math import tan, sin, cos, radians


# --> Classes

class vec3d:
    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z

    def __repr__(self) -> str:
        return f"vec3d at {self.x}, {self.y}, {self.z}"

class vec2d:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"vec2d at {self.x}, {self.y}"

class triangle:
    def __init__(self, a, b, c) -> None:
        if not (isinstance(a, (vec3d, vec2d)) and isinstance(b, (vec3d, vec2d)) and isinstance(c, (vec3d, vec2d))):
            raise TypeError
        self.points = [a, b, c]

        # --> For easier usage in for loops
        self.points:list[vec3d|vec2d]
    
    def __repr__(self) -> str:
        return f"triangle with points {self.points}"

class mesh:
    def __init__(self, *tris:triangle) -> None:
        self.tris = []
        for tri in tris:
            if not isinstance(tri, triangle):
                raise TypeError
            self.tris.append(tri)

        # --> For easier usage in for loops
        self.tris:list[triangle]


# --> Pygame window setup

import pygame

pygame.init()

background_colour = (0, 0, 0)
drawColor = (255, 255, 255)
windowSize = (1920, 1080)
halfwindow = windowSize[0]//2, windowSize[1]//2

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Pyrender')
pygame.display.flip()

running = True
clock = pygame.time.Clock
tick = 0


# --> Main code

meshCube = mesh()

meshCube.tris = [

    # South :
    triangle(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)),
    triangle(vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0)),

    # East :
    triangle(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)),
    triangle(vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1)),
    
    # North :
    triangle(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)),
    triangle(vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1)),
    
    # West :
    triangle(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)),
    triangle(vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0)),

    # Top :
    triangle(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)),
    triangle(vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0)),
    
    # Bottom :
    triangle(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)),
    triangle(vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0)),

]


# Valeurs du plan de projection

ffLen = 1
fFov = 90
fAspectRadio = windowSize[1]/windowSize[0]
fFovRad = 1/tan(fFov * 0.5 / 180 * 3.14159265)
fZoom = 100


# --> Fonctions

def rotate_point(point:vec3d, angle_x, angle_y, angle_z):
    # Convert angles from degrees to radians
    angle_x = radians(angle_x)
    angle_y = radians(angle_y)
    angle_z = radians(angle_z)
    
    # Rotation around X-axis
    x = point.x
    y = point.y
    z = point.z
    cos_x = cos(angle_x)
    sin_x = sin(angle_x)
    new_y = y * cos_x - z * sin_x
    new_z = y * sin_x + z * cos_x
    
    # Rotation around Y-axis
    cos_y = cos(angle_y)
    sin_y = sin(angle_y)
    new_z2 = new_z * cos_y - x * sin_y
    new_x = new_z * sin_y + x * cos_y
    
    # Rotation around Z-axis
    cos_z = cos(angle_z)
    sin_z = sin(angle_z)
    new_x2 = new_x * cos_z - new_y * sin_z
    new_y2 = new_x * sin_z + new_y * cos_z
    
    return vec3d(new_x2, new_y2, new_z2)


def project_point(point:vec3d):
    if point.z < 0.1 and point.z > 0:
        vec2d(0,0)
    try:
        return vec2d((ffLen*point.x / (ffLen + point.z)),
                    (ffLen*point.y / (ffLen + point.z)))
    except :
        return vec2d(0,0)


def draw_triangles(shape:mesh):
    if not isinstance(shape, mesh):
        raise TypeError
    
    for tri in shape.tris:

        triRotated = triangle(
            rotate_point(tri.points[0], cam_angle.x, cam_angle.y, cam_angle.z),
            rotate_point(tri.points[1], cam_angle.x, cam_angle.y, cam_angle.z),
            rotate_point(tri.points[2], cam_angle.x, cam_angle.y, cam_angle.z)
        )

        triTranslated = triangle(vec3d(0,0,0),vec3d(0,0,0),vec3d(0,0,0))
        triTranslated.points[0].x = triRotated.points[0].x + pos.x
        triTranslated.points[1].x = triRotated.points[1].x + pos.x
        triTranslated.points[2].x = triRotated.points[2].x + pos.x
        triTranslated.points[0].y = triRotated.points[0].y + pos.y
        triTranslated.points[1].y = triRotated.points[1].y + pos.y
        triTranslated.points[2].y = triRotated.points[2].y + pos.y
        triTranslated.points[0].z = triRotated.points[0].z + pos.z
        triTranslated.points[1].z = triRotated.points[1].z + pos.z
        triTranslated.points[2].z = triRotated.points[2].z + pos.z

        triProjected = triangle(vec2d(0,0),vec2d(0,0),vec2d(0,0))

        triProjected.points[0] = project_point(triTranslated.points[0])
        triProjected.points[1] = project_point(triTranslated.points[1])
        triProjected.points[2] = project_point(triTranslated.points[2])

        pygame.draw.polygon(screen,
                            drawColor,
                            (
                                (triProjected.points[0].x * fZoom + halfwindow[0], triProjected.points[0].y * fZoom + halfwindow[1]),
                                (triProjected.points[1].x * fZoom + halfwindow[0], triProjected.points[1].y * fZoom + halfwindow[1]),
                                (triProjected.points[2].x * fZoom + halfwindow[0], triProjected.points[2].y * fZoom + halfwindow[1]),
                            ),
                            1)


# --> Mainloop

pos = vec3d(0,0,0)
cam_angle = vec3d(0,0,0)


while running:

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:

                case pygame.K_p: fZoom *= 1.1
                case pygame.K_m: fZoom /= 1.1

                case pygame.K_i: pos.z += 0.2
                case pygame.K_k: pos.z -= 0.2
                case pygame.K_l: pos.x += 0.2
                case pygame.K_j: pos.x -= 0.2
                case pygame.K_o: pos.y += 0.2
                case pygame.K_u: pos.y -= 0.2

                case pygame.K_q: cam_angle.y += 5
                case pygame.K_d: cam_angle.y -= 5
                case pygame.K_s: cam_angle.x += 5
                case pygame.K_z: cam_angle.x -= 5
                case pygame.K_a: cam_angle.z += 5
                case pygame.K_e: cam_angle.z -= 5

    screen.fill(background_colour)

    draw_triangles(meshCube)

    pygame.display.flip()

    pygame.time.wait(20)