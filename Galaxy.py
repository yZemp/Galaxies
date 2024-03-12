from PIL import Image

class Galaxy:
    def __init__(self, name: str, path: str, bar: bool = None, type: str = None):
        '''
        Galaxy class constructor
        name: name of the galaxy
        path: path to image in folder
        bar: does the galaxy have a bar or not
        type: elliptical, spiral, irregular
        '''
        self.name = name
        self.path = path
        self.bar = bar
        self.type = type
    
    def __str__(self):
        return f"Galaxy {self.name}"
    
    def show(self):
        img = Image.open(self.path)
        img.show()
