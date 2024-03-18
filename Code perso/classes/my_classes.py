from math import cos, radians, sin

class vec3:
    def __init__(self, x:int|float, y:int|float, z:int|float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError
        if not isinstance(y, (int, float)):
            raise TypeError
        if not isinstance(z, (int, float)):
            raise TypeError

        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return "Vector3 ({}, {}, {})".format(self.x, self.y, self.z)
    
    def __add__(self, other):
        if isinstance(other, (vec3)):
            return vec3(self.x+other.x, self.y+other.y, self.z+other.z)
        else: raise TypeError
        
    def __sub__(self, other):
        if isinstance(other, (vec3)):
            return vec3(self.x-other.x, self.y-other.y, self.z-other.z)
        else: raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return vec3(self.x*other, self.y*other, self.z*other)
        else:raise TypeError

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return vec3(self.x/other, self.y/other, self.z/other)
        else:raise TypeError

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalized(self):
        return self/self.magnitude()
        
class vec2:
    def __init__(self, x:int|float, y:int|float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError
        if not isinstance(y, (int, float)):
            raise TypeError

        self.x = x
        self.y = y

    def __repr__(self) -> str: return "Vector2 ({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        if isinstance(other, (vec2)):
            return vec2(self.x+other.x, self.y+other.y)
        else: raise TypeError
        
    def __sub__(self, other):
        if isinstance(other, (vec2)):
            return vec2(self.x-other.x, self.y-other.y)
        else: raise TypeError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vec2(self.x*other, self.y*other)
        else:raise TypeError

    def __rmul__(self, other): return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return vec2(self.x/other, self.y/other)
        else: raise TypeError

    def normalized(self): 
        if self.magnitude()!=0 : return self/self.magnitude()
    def magnitude(self)->int: return (self.x**2+self.y**2)**0.5
    def tovec3(self): return vec3(self.x, self.y, 0)

    @staticmethod
    def staticNormalize(vector):
        if not isinstance(vector, vec2):
            raise TypeError
        if vector.magnitude()!=0 : return vector/vector.magnitude()

    def rotated(self, angle:int):
        if angle < 0:
            angle += 360 * (abs(angle//360) + 1)
        match angle%360:
            case 0:return self
            case 90:return vec2(self.y, -self.x)
            case 180:return vec2(-self.x, -self.y)
            case 270:return vec2(-self.y, self.x)
            case _:
                angle = radians(angle)
                xn = self.x*cos(angle) - self.y*sin(angle)
                yn = self.y*cos(angle) + self.x*sin(angle)

                return vec2(xn, yn)

class point3(vec3):
    def __init__(self, x:int|float, y:int|float, z:int|float, name:str) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError
        if not isinstance(y, (int, float)):
            raise TypeError
        if not isinstance(z, (int, float)):
            raise TypeError

        self.x = x
        self.y = y
        self.z = z

        self.name = name

    def distOrigin(self): return self.magnitude()

    def segment(self, other):
        if not isinstance(other, (vec3, point3)):
            raise TypeError
        new = other-self
        return new
    
class point2(vec2):
    def __init__(self, x: int | float, y: int | float, name: str) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError
        if not isinstance(y, (int, float)):
            raise TypeError

        self.x = x
        self.y = y

        self.name = name

    def distOrigin(self): return self.magnitude()

    def segment(self, other):
        if not isinstance(other, (vec2, point2)):
            raise TypeError
        new = other-self
        return new

class polynomial:
    def __init__(self, *args) -> None:
        if not isinstance(args, (list, tuple)):
            raise TypeError
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError
        weights = args

class trinome(polynomial):
    def __init__(self, a, b, c) -> None:
        if not isinstance(a, (int, float)):
            raise TypeError
        
        if not isinstance(b, (int, float)):
            raise TypeError
        
        if not isinstance(c, (int, float)):
            raise TypeError
            
        self.a = a
        self.b = b
        self.c = c

    def determinant(self)->float:
        return self.b**2 - (4*self.a*self.c)
    
    def rootsnumber(self):
        if self.determinant() > 0:
            return 2
        elif self.determinant() < 0:
            return 0
        else: return 1

    def roots(self):
        match self.rootsnumber():
            case 0: return None
            case 1: return -self.b / (2*self.a)
            case 2: return ((-self.b)+(self.determinant()**0.5)) / (2*self.a), ((-self.b)-(self.determinant()**0.5)) / (2*self.a)

