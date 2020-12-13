import pygame
import numpy as np
import game_constants as gc


class Tetrimino(object):
    COLOUR = (0, 0, 0)
    LENGTH = 4
    NUM_X = gc.WIN_WIDTH // gc.BLOCKSIZE
    NUM_Y = gc.WIN_HEIGHT // gc.BLOCKSIZE
    START_X = gc.START_X
    START_Y = gc.START_Y
    TYPE = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.tetrimino_array = np.zeros((self.LENGTH, self.LENGTH))
        self.tick_count = 0

    def valid_move(self, static_array, x=None, y=None):
        if not x:
            x = self.x
        if not y:
            y = self.y

        id_list = np.where(self.tetrimino_array == 1)
        for idx, idy in zip(id_list[1], id_list[0]):
            pos_x = idx + x
            pos_y = idy + y
            valid = self.valid_id(static_array, pos_x, pos_y)
            if not valid:
                return False
        return True

    def valid_id(self, static_array, x, y):
        # checking for moving out of bounds in x
        valid_x_range = 0 <= x <= self.NUM_X - 1
        # checking for moving out of bounds in y
        valid_y_range = y <= self.NUM_Y - 1
        if not valid_x_range or not valid_y_range:
            return False
        else:
            # checking if there is allready a block
            valid_pos = static_array[x, y] == 0
            if not valid_pos:
                return False
        return True

    def rotate(self, static_array, direction=1):
        if direction == 1 and self.valid_rotation(static_array, direction):
            self.tetrimino_array = np.rot90(self.tetrimino_array, 3)

        if direction == -1 and self.valid_rotation(static_array, direction):
            self.tetrimino_array = np.rot90(self.tetrimino_array, 1)

    def valid_rotation(self, static_array, direction):
        possible_tetrimino_array = self.tetrimino_array
        if direction == 1:
            possible_tetrimino_array = np.rot90(self.tetrimino_array, 3)
        if direction == -1:
            possible_tetrimino_array = np.rot90(self.tetrimino_array, 1)

        id_list = np.where(possible_tetrimino_array == 1)
        for idx, idy in zip(id_list[1], id_list[0]):
            valid = self.valid_id(static_array, self.x+idx, self.y+idy)
            if not valid:
                return False
        return True

    def move_x(self, static_array, direction):
        if self.valid_move(static_array, x=self.x+direction):
            self.x += direction

    def move_y(self, static_array):
        update = None
        self.tick_count += 1
        if self.tick_count == gc.FALL_VEL:
            if self.valid_move(static_array, y=self.y+1):
                self.y += 1
                self.tick_count = 0
            else:
                update = self.get_static(static_array)
        return update

    def get_static(self, static_array):
        id_list = np.where(self.tetrimino_array == 1)
        for idx, idy in zip(id_list[1], id_list[0]):
            static_array[self.x + idx, self.y + idy] = self.TYPE
        self.__init__(self.START_X, self.START_Y)
        return static_array

    def draw(self, win):
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                width = (self.x + j) * gc.BLOCKSIZE + 1
                height = (self.y + i) * gc.BLOCKSIZE + 1
                if self.tetrimino_array[i, j]:
                    loc = (width, height, gc.BLOCKSIZE - 2, gc.BLOCKSIZE - 2)
                    pygame.draw.rect(win, self.COLOUR, loc)

    def print(self):
        print(self.tetrimino_array)


class I_Tetrimino(Tetrimino):
    COLOUR = gc.I_COLOUR
    LENGTH = 4
    TYPE = 1

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[1, :] = 1


class O_Tetrimino(Tetrimino):
    COLOUR = gc.O_COLOUR
    LENGTH = 4
    TYPE = 2

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[1:3, 1:3] = 1


class T_Tetrimino(Tetrimino):
    COLOUR = gc.T_COLOUR
    LENGTH = 3
    TYPE = 3

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[0, 1] = 1
        self.tetrimino_array[1, :] = 1


class S_Tetrimino(Tetrimino):
    COLOUR = gc.S_COLOUR
    LENGTH = 3
    TYPE = 4

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[0, 1:] = 1
        self.tetrimino_array[1, :2] = 1


class Z_Tetrimino(Tetrimino):
    COLOUR = gc.Z_COLOUR
    LENGTH = 3
    TYPE = 5

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[0, :2] = 1
        self.tetrimino_array[1, 1:] = 1


class J_Tetrimino(Tetrimino):
    COLOUR = gc.J_COLOUR
    LENGTH = 3
    TYPE = 6

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[0, 0] = 1
        self.tetrimino_array[1, :] = 1


class L_Tetrimino(Tetrimino):
    COLOUR = gc.L_COLOUR
    LENGTH = 3
    TYPE = 7

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tetrimino_array[0, 2] = 1
        self.tetrimino_array[1, :] = 1
