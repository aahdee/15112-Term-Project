import pygame, os

class GameObject(pygame.sprite.Sprite):
    
    #this block of code is cited from http://www.nerdparadise.com/tech/python/pygame/basics/part2/
    _image_library = {}
    def get_image(self,path):
        image = GameObject._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            GameObject._image_library[path] = image
        return image

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = self.get_image(image)
        self.width, self.height = self.image.get_size()
        self.radius = self.width/2
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.x - self.width/2, self.y - self.height/2, 
                                self.width, self.height)
        

    def draw(self, surface):
        surface.blit(self.image,(self.x,self.y))
    
    