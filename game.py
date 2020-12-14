import pygame
import numpy as np
import game_constants as gc


class Game():
    NUM_X = gc.WIN_WIDTH // gc.BLOCKSIZE
    NUM_Y = gc.WIN_HEIGHT // gc.BLOCKSIZE
    COLOURS = [gc.I_COLOUR, gc.O_COLOUR,
               gc.T_COLOUR, gc.S_COLOUR,
               gc.Z_COLOUR, gc.J_COLOUR,
               gc.L_COLOUR]

    def __init__(self):
        self.static_game_array = np.zeros((self.NUM_X, self.NUM_Y))
        self.score = 0

    def check_for_finished_row(self):
        finished_rows = []
        # over each row
        for i in range(self.NUM_Y):
            if 0 not in self.static_game_array[:, i]:
                finished_rows.append(i)
        return finished_rows

    def remove_rows(self, rows):
        for row in rows:
            self.score += 1
            self.static_game_array[:, 1:row+1] = self.static_game_array[:, 0:row]

    def check_for_lost(self):
        if np.count_nonzero(self.static_game_array[:, 2]) > 0:
            return True
        return False

    def update_static_game_array(self, update):
        self.static_game_array = update
        finished = self.check_for_finished_row()
        if finished:
            self.remove_rows(finished)
        lost = self.check_for_lost()
        if lost:
            print(f'Your score was {self.score}. Good Job!')
            return False
        return True

    def get_static_game_array(self):
        return self.static_game_array

    def draw_static(self, win):
        for i in range(self.NUM_Y):
            for j in range(self.NUM_X):
                width = j * gc.BLOCKSIZE + 1
                height = i * gc.BLOCKSIZE + 1
                if self.static_game_array[j, i] != 0:
                    tile_type = int(self.static_game_array[j, i])
                    loc = (width, height, gc.BLOCKSIZE - 2, gc.BLOCKSIZE - 2)
                    pygame.draw.rect(win, self.COLOURS[tile_type-1], loc)

    @staticmethod
    def draw_bg(win):
        win.fill(gc.BG_COLOUR)
        blocksize = gc.BLOCKSIZE
        for x in range(gc.WIN_WIDTH):
            for y in range(gc.WIN_HEIGHT):
                rect = pygame.Rect(x * blocksize, y * blocksize,
                                   blocksize, blocksize)
                pygame.draw.rect(win, gc.LINIE_COLOUR, rect, 1)

        pygame.image.save(win, 'imgs/tetris_background.png')
        bg_img = pygame.image.load('imgs/tetris_background.png')
        return bg_img

    def print_static_game_array(self):
        print(self.static_game_array.T)
