import pygame
import sys
import math
import time


def project_point(point_number):
    try:
        if vertices[point_number][2]>-FOCAL_LENGTH:
            x_return = vertices[point_number][0]*FOCAL_LENGTH/(FOCAL_LENGTH+vertices[point_number][2])
            x_return *= ZOOM_FACTOR
            x_return += HALF_WIDTH
            y_return = vertices[point_number][1]*FOCAL_LENGTH/(FOCAL_LENGTH+vertices[point_number][2])
            y_return *= ZOOM_FACTOR
            y_return += HALF_HEIGHT
        else:
            x_return = vertices[point_number][0]
            y_return = vertices[point_number][1]*1000
    except:
        x_return = 0
        y_return = 0
    return x_return, y_return


def rotate_object(vertices, angle_x, angle_y, angle_z):
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex

        # Rotate around X-axis
        new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y, z = new_y, new_z

        # Rotate around Y-axis
        new_x = x * math.cos(angle_y) + z * math.sin(angle_y)
        new_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
        x, z = new_x, new_z

        # Rotate around Z-axis
        new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
        new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
        x, y = new_x, new_y

        rotated_vertices.append([x, y, z])

    return rotated_vertices


class Object:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


class Cube(Object):
    def __init__(self, centerx, centery, centerz, sizex, sizey, sizez):
        self.vertices = [
            [centerx + sizex, centery + sizey, centerz + sizez],
            [centerx + sizex, centery + sizey, centerz - sizez],
            [centerx - sizex, centery + sizey, centerz - sizez],
            [centerx - sizex, centery + sizey, centerz + sizez],
            [centerx + sizex, centery - sizey, centerz + sizez],
            [centerx + sizex, centery - sizey, centerz - sizez],
            [centerx - sizex, centery - sizey, centerz - sizez],
            [centerx - sizex, centery - sizey, centerz + sizez]]
        
        self.edges = [
            [0, 1],
            [1, 2],
            [2, 3],
            [0, 3],
            [4, 5],
            [5, 6],
            [6, 7],
            [4, 7],
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7]]


def movement_checks():
    global camera_x, camera_y, camera_z, camera_angle_x, camera_angle_y
    if pygame.key.get_pressed()[pygame.K_z]:
        camera_z += MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_q]:
        camera_x -= MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_d]:
        camera_x += MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_s]:
        camera_z -= MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        camera_y += MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        camera_y -= MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_UP]:
        camera_angle_x += MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        camera_angle_x -= MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        camera_angle_y -= MOVE_SPEED/fps
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        camera_angle_y += MOVE_SPEED/fps


pygame.init()

WIDTH, HEIGHT = 1280, 720
FOCAL_LENGTH = 1 
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
ZOOM_FACTOR = 150
X_TURN_RATE = 0.000
Y_TURN_RATE = 0.000
Z_TURN_RATE = 0.000
FRAMERATE = 60
MOVE_SPEED = 6
fps = FRAMERATE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("3D Filled Cube")


FACES = [
]

OBJECTS = [
    Cube(0, 1, 0, 0.5, 0.5, 0.5),
    Cube(1, 0, 0, 0.5, 0.5, 0.5),
    Cube(-1, 0, 0, 0.5, 0.5, 0.5),
]

angle_x = 0
angle_y = 0
angle_z = 0

camera_angle_x = 0
camera_angle_y = 0
camera_angle_z = 0

camera_x = 0
camera_y = 0
camera_z = 0

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                FOCAL_LENGTH *= 1.1
            elif event.key == pygame.K_k:
                FOCAL_LENGTH /= 1.1
            elif event.key == pygame.K_l:
                ZOOM_FACTOR *= 1.1
            elif event.key == pygame.K_j:
                ZOOM_FACTOR /= 1.1
        elif event.type == pygame.WINDOWRESIZED:
            WIDTH, HEIGHT = pygame.display.get_window_size()
            HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2

    movement_checks()

    screen.fill(BLACK)

    sinusx = math.sin(angle_x)
    cosinusx = math.cos(angle_x)
    sinusy = math.sin(angle_y)
    cosinusy = math.cos(angle_y)
    sinusz = math.sin(angle_z)
    cosinusz = math.cos(angle_z)

    for object in OBJECTS:

        vertices = rotate_object(object.vertices, angle_x, angle_y, angle_z)
        vertices = rotate_object(vertices, camera_angle_x, camera_angle_y, camera_angle_z)
        for vertex in vertices:
            vertex[0] -= camera_x
            vertex[1] -= camera_y
            vertex[2] -= camera_z

        for edge in object.edges:

            pygame.draw.aaline(screen, WHITE, project_point(edge[0]), project_point(edge[1]), 2)
    pygame.display.flip()
    
    angle_x = (angle_x + X_TURN_RATE)%360
    angle_y = (angle_y + Y_TURN_RATE)%360
    angle_z = (angle_z + Y_TURN_RATE)%360

    clock.tick(FRAMERATE)
    fps = clock.get_fps()
    pygame.display.set_caption(str(fps))

pygame.quit()
sys.exit()