#source: Lukas Peraza from the 112 pygame lecture
#http://blog.lukasperaza.com/getting-started-with-pygame/
#this is modified to have a game clock and to break when the timerfired quit is true
import pygame, os


class PygameGame(object):

    def init(self):
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)
    
    #this block of code is cited from http://www.nerdparadise.com/tech/python/pygame/basics/part2/
    _image_library = {}
    def get_image(self,path):
        image = PygameGame._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            PygameGame._image_library[path] = image
        return image

    def __init__(self, width=700, height=700, fps=60, title="GeoHell"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0,0,0)
        self.seconds = 0
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        pygame.time.set_timer(pygame.USEREVENT +1, 1000)
        
        font = pygame.font.Font(None, 30)
        
        playing = True
        while playing:
            time = clock.tick(self.fps)
            quit = self.timerFired(time)
            if quit: break
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.USEREVENT +1:
                    self.seconds += 1
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            
            self.redrawAll(screen)
            
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()