import numpy
import pygame
import random
import tetriminos
import game as game_class
import game_constants as gc


def main():
    pygame.init()
    win = pygame.display.set_mode((gc.WIN_WIDTH, gc.WIN_HEIGHT))
    pygame.display.set_caption('Tetris')
    game_loop(win)


def game_loop(win):
    game = game_class.Game()
    clock = pygame.time.Clock()

    tiles = [
        tetriminos.I_Tetrimino(5, 0),
        tetriminos.O_Tetrimino(5, 0),
        tetriminos.T_Tetrimino(5, 0),
        tetriminos.S_Tetrimino(5, 0),
        tetriminos.Z_Tetrimino(5, 0),
        tetriminos.J_Tetrimino(5, 0),
        tetriminos.L_Tetrimino(5, 0)
        ]

    bg_img = game.draw_bg(win)
    static_array = game.get_static_game_array()

    tile = random.choice(tiles)
    spawn_new_tile = False

    run = True
    while run:
        clock.tick(30)

        if spawn_new_tile:
            tile = random.choice(tiles)
            spawn_new_tile = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                static_array = game.get_static_game_array()
                if event.key == pygame.K_SPACE:
                    tile.rotate(static_array)

                if event.key == pygame.K_LEFT:
                    tile.move_x(static_array, -1)

                if event.key == pygame.K_RIGHT:
                    tile.move_x(static_array, 1)

        update = tile.move_y(static_array)
        if update is not None:
            run = game.update_static_game_array(update)
            spawn_new_tile = True

        draw_ingame_window(win, bg_img, game, tile)


def draw_ingame_window(win, bg_img, game, tile):
    win.blit(bg_img, (0, 0))
    game.draw_static(win)
    tile.draw(win)
    pygame.display.update()


if __name__ == '__main__':
    main()
