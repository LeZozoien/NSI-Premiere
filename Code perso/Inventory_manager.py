class NoObjectError(Exception):
    def __init__(self, object) -> None:
        super().__init__("no such object as " + str(object))

class NotEnoughObjects(Exception):
    def __init__(self, object) -> None:
        super().__init__("Not enough of  " + str(object))

class Inventory:
    def __init__(self):
        self.objects = {}

    def add_object(self, object:str, count:int|None = 1):
        object = object.lower().strip()

        if object in self.objects:
            self.objects[object] = self.objects[object]+count
        else:
            self.objects[object] = count

    def rem_object(self, object:str, count:int|None = 1):
        object = object.lower().strip()
        
        if object in self.objects:
            if self.objects[object] == count:
                self.objects.pop(object)
            elif self.objects[object] > count:
                self.objects[object] = self.objects[object]-count
            else:
                raise NotEnoughObjects(object)                
        else:
            raise NoObjectError(object)

    def count_object(self, object:str):
        object = object.lower().strip()

        if object in self.objects:
            return self.objects[object]
        else:
            return 0

    def print_objects(self):
        for object in self.objects:
            print(object, self.objects[object])
    
    def __repr__(self) -> str:
        return "Inventory : " + str(self.objects)
