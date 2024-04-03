import math

class Object:

    def __init__(self) -> None:
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
                (0, 2, 4), (7, 2, 3),]
                # (1, 0, 5), (0, 4, 5),]

    def project_point(self, index, camera, focal):

        # Variables : 
        camx, camy, camz = camera
        pointx, pointy, pointz = self.VERTICES[index]

        # Camera to view:
        pointx -= camx
        pointx = -pointx
        pointy -= camy
        pointz -= camz

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
        a, b, c = self.VERTICES[self.FACES[index][0]],self.VERTICES[self.FACES[index][1]],self.VERTICES[self.FACES[index][2]]

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

Camerapos = [4, 0, 0]
focal = 1

cube = Object()

for vertex_idx in range(len(cube.VERTICES)):
    print(cube.project_point(vertex_idx, Camerapos, focal))

for face_idx in range(len(cube.FACES)):
    print(cube.project_face(face_idx, Camerapos, focal))