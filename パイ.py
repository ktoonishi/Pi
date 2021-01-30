# -*- coding:utf-8 -*-
import pygame
import sys
import random

# import keras
# deep learning
# mysql

WORK_SIZE = 400
SCREEN_PADDING = 8
IMAGE_SIze = 60
FONT_SIZE = 48
CALC_EP = 1000

COLOR_WHITE = (240, 240, 240)
COLOR_RED = (240, 40, 40)
COLOR_GREEN = (40, 240, 40)
COLOR_BLUE = (40, 40, 240)


def main():
    print ("start perogorimming")

    pygame.init()
    screen = pygame.display.set_mode((WORK_SIZE, WORK_SIZE + FONT_SIZE))
    pygame.display.set_caption("Pi")
    font = pygame.font.Font(None, FONT_SIZE)

    img = pygame.image.load("title.png")

    #
    rr = WORK_SIZE * WORK_SIZE
    pi_cnt = 0
    calc_cnt = 0.0
    pi_val = 0.0

    # screen initialize
    screen.fill((0, 0, 0))

    while(True):
        calc_cnt = calc_cnt + 1.0
        # 
        rx = random.randint(0, WORK_SIZE)
        ry = random.randint(0, WORK_SIZE)

        if rx * rx + ry * ry <= rr:
            pygame.draw.circle(screen, COLOR_BLUE, (rx, ry), 1, 1)
            pi_cnt = pi_cnt + 1
        else:    
            pygame.draw.circle(screen, COLOR_RED, (rx, ry), 1, 1)

        pi_val = 4 * pi_cnt / calc_cnt

        # display current value
        pygame.draw.circle(screen, COLOR_GREEN, (0, 0), WORK_SIZE, 5)
        screen.fill(COLOR_WHITE, (0, WORK_SIZE, WORK_SIZE, FONT_SIZE))
        text = font.render (str(pi_val), True, COLOR_BLUE)
        screen.blit(text, [SCREEN_PADDING, WORK_SIZE + SCREEN_PADDING])

        # Update display
        pygame.display.update()

        # Event
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



if __name__=="__main__":
    main()
