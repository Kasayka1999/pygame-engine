import pygame as pg

_ = False
mini_map = [ #! Will be replaced later
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,1,1,1,_,_,_,1],
    [1,1,1,_,1,_,_,1,_,2,_,_,1],
    [1,1,1,_,_,_,1,1,_,2,_,1,1],
    [1,_,1,_,_,_,1,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,1],
    [3,3,3,3,3,3,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self,app):
        self.app = app
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value
    def draw(self):
        [pg.draw.rect(self.app.window.surface,(96,96,96),(pos[0] * 100,pos[1] * 100,100,100),2) for pos in self.world_map]