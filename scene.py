from constants import *

class Scene():
    def __init__(self, tag, btns=[], lbls=[]):
        self.tag = tag
        self.buttons = btns
        self.labels = lbls
    
    def render(self, screen):
        for obj in self.buttons+self.labels:
            obj.render(screen)