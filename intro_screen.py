import pygame
import sys
import time
import game

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.display.set_caption('Max\'s TicTacToe')

clock = pygame.time.Clock()

SWIDTH, SHEIGHT = 300, 400
DIS = pygame.display.set_mode((SWIDTH, SHEIGHT))

bgcolor = (0, 100, 150)

font = pygame.font.SysFont('georgia', 50)
subfont = pygame.font.SysFont('arial', 30)

# colors
green = (0, 175, 0)
lightgreen = (153, 255, 51)
red = (255, 0, 0)
lightred = (255, 102, 102)
black = (0, 0, 0)

play = False


def title(msg, x, y):
    titletext = font.render(msg, True, black)
    
    DIS.blit(titletext, (x, y))


def button(msg, x, y, width, height, defaultcolor, hovercolor):
    rects = pygame.Rect(x, y, width, height)
    pos = pygame.mouse.get_pos()
    buttontext = subfont.render(msg, True, black)

    if x <= pos[0] <= width + x and y <= pos[1] <= height + y:
        pygame.draw.rect(DIS, hovercolor, rects)
        DIS.blit(buttontext, (x + 20, y + 10))
    else:
        pygame.draw.rect(DIS, defaultcolor, rects)
        DIS.blit(buttontext, (x + 18, y + 8))
    pygame.display.update()


def playquit(x, y, width, height, x2):
    pos2 = pygame.mouse.get_pos()
    global play

    if x <= pos2[0] <= width + x and y <= pos2[1] <= height + y:
        game.main()
        
    if x2 <= pos2[0] <= width + x2 and y <= pos2[1] <= height + y:
        time.sleep(0.2)
        pygame.quit()
        sys.exit()


def main():
    run = True
    pygame.init()
    
    pygame.display.set_mode((SWIDTH, SHEIGHT))
    DIS.fill(bgcolor)
    
    title('Max\'s', 80, 50)
    title('Tic-Tac-Toe', 15, 100)
    title('Game', 80, 150)

    while run:
        pygame.init()
        button('Play', 160, 300, 100, 50, green, lightgreen)
        button('Quit', 40, 300, 100, 50, red, lightred)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                playquit(160, 300, 100, 50, 40)

    pygame.quit()
 
