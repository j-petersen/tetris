import pygame
import numpy as np
import game_constants as gc

class Game():
    NUM_X = gc.WIN_WIDTH // gc.BLOCKSIZE
    NUM_Y = gc.WIN_HEIGHT // gc.BLOCKSIZE

    def __init__(self):
        self.static_game_array = np.zeros((self.NUM_X, self.NUM_Y))

    def update_static_game_array(self, update):
        self.static_game_array = update

    def get_static_game_array(self):
        return self.static_game_array

    @staticmethod
    def draw_bg(win):
        win.fill(gc.BG_COLOUR)
        blocksize = gc.BLOCKSIZE
        for x in range(gc.WIN_WIDTH):
            for y in range(gc.WIN_HEIGHT):
                rect = pygame.Rect(x*blocksize, y*blocksize,
                                   blocksize, blocksize)
                pygame.draw.rect(win, gc.LINIE_COLOUR, rect, 1)

        pygame.image.save(win, 'imgs/tetris_background.png')
        bg_img = pygame.image.load('imgs/tetris_background.png')
        return bg_img

    def print_static_game_array(self):
        print(self.static_game_array.T)
