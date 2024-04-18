# Basic 3d renderer (3rd version)
from math import tan, sin, cos


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

def draw_triangles(shape:mesh):
    if not isinstance(shape, mesh):
        raise TypeError
    
    for tri in shape.tris:

        triTranslated = triangle(vec3d(0,0,0),vec3d(0,0,0),vec3d(0,0,0))
        triTranslated.points[0].x = tri.points[0].x + pos.x
        triTranslated.points[1].x = tri.points[1].x + pos.x
        triTranslated.points[2].x = tri.points[2].x + pos.x
        triTranslated.points[0].y = tri.points[0].y + pos.y
        triTranslated.points[1].y = tri.points[1].y + pos.y
        triTranslated.points[2].y = tri.points[2].y + pos.y
        triTranslated.points[0].z = tri.points[0].z + pos.z
        triTranslated.points[1].z = tri.points[1].z + pos.z
        triTranslated.points[2].z = tri.points[2].z + pos.z

        triProjected = triangle(vec2d(0,0),vec2d(0,0),vec2d(0,0))

        triProjected.points[0] = vec2d((ffLen*triTranslated.points[0].x / (ffLen + triTranslated.points[0].z)),
                                       (ffLen*triTranslated.points[0].y / (ffLen + triTranslated.points[0].z)))
        triProjected.points[1] = vec2d((ffLen*triTranslated.points[1].x / (ffLen + triTranslated.points[1].z)),
                                       (ffLen*triTranslated.points[1].y / (ffLen + triTranslated.points[1].z)))
        triProjected.points[2] = vec2d((ffLen*triTranslated.points[2].x / (ffLen + triTranslated.points[2].z)),
                                       (ffLen*triTranslated.points[2].y / (ffLen + triTranslated.points[2].z)))

        pygame.draw.polygon(screen,
                            drawColor,
                            (
                                (triProjected.points[0].x * fZoom + halfwindow[0], triProjected.points[0].y * fZoom + halfwindow[1]),
                                (triProjected.points[1].x * fZoom + halfwindow[0], triProjected.points[1].y * fZoom + halfwindow[1]),
                                (triProjected.points[2].x * fZoom + halfwindow[0], triProjected.points[2].y * fZoom + halfwindow[1]),
                            ),
                            1)


# --> Mainloop

while running:
    tick += 1
    tick = tick % 360
    pos = vec3d(cos(tick/180*3.1415),0,sin(tick/180*3.1415))
    if 0 <= tick % 360 < 90: pos.y += tick/120
    elif 90 <= tick % 360 < 180: pos.y += (180-tick)/120
    elif 180 <= tick % 360 < 270: pos.y -= (180-tick)/120
    elif 270 <= tick % 360 < 360: pos.y -= (tick-360)/120
    pos.z += 1.5

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    draw_triangles(meshCube)

    pygame.display.flip()

    pygame.time.wait(20)