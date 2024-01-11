import pygame
import time
import intro_screen

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.display.set_caption('Max\'s TicTacToe')

turns = 2

WIDTH, HEIGHT = 300, 400
pygame.display.set_mode((WIDTH, HEIGHT))
DIS = pygame.display.set_mode((WIDTH, HEIGHT))

# top row:         aa ab ac
# middle row:      ba bb bc
# bottem row:      ca cb cc
# letters
aa = WIDTH / 6 - 25, HEIGHT / 6 - 50
ab = WIDTH / 2 - 25, HEIGHT / 6 - 50
ac = WIDTH - 75, HEIGHT / 6 - 50
ba = WIDTH / 6 - 25, HEIGHT / 2 - 50
bb = WIDTH / 2 - 25, HEIGHT / 2 - 50
bc = WIDTH - 75, HEIGHT / 2 - 50
ca = WIDTH / 6 - 25, HEIGHT - 100
cb = WIDTH / 2 - 25, HEIGHT - 100
cc = WIDTH - 75, HEIGHT - 100

#  mouse click area
toprow = ['a1', 'b1', 'c1']
middlerow = ['a2', 'b2', 'c2']
bottemrow = ['a3', 'b3', 'c3']

def drawboard():
    COLOR = (255, 255, 255)
    START1 = (WIDTH / 3, 0)
    END1 = (WIDTH / 3, HEIGHT)
    START2 = (WIDTH / 1.5, 0)
    END2 = (WIDTH / 1.5, HEIGHT)
    START3 = (0, HEIGHT / 3)
    END3 = (WIDTH, HEIGHT / 3)
    START4 = (0, HEIGHT / 1.5)
    END4 = (WIDTH, HEIGHT / 1.5)
    LWIDTH = 5

    DIS.fill((0, 125, 100))

    pygame.draw.line(DIS, COLOR, START1, END1, LWIDTH)
    pygame.draw.line(DIS, COLOR, START2, END2, LWIDTH)
    pygame.draw.line(DIS, COLOR, START3, END3, LWIDTH)
    pygame.draw.line(DIS, COLOR, START4, END4, LWIDTH)
    pygame.display.update()

def reset():
    toprow = ['a1', 'b1', 'c1']
    middlerow = ['a2', 'b2', 'c2']
    bottemrow = ['a3', 'b3', 'c3']
    drawboard()


def winmessage():
    font = pygame.font.SysFont('Type 42', 40)
    winrect = pygame.Rect(50, 200, 200, 60)
    win = font.render('GAME OVER', True, (0, 0, 0))

    pygame.draw.rect(DIS, (150, 0, 0), winrect)
    DIS.blit(win, (65, 220))
    pygame.display.update()


def win():
    global toprow
    global middlerow
    global bottemrow 
    
    # winning across
    if toprow == ['x', 'x', 'x'] or toprow == ['o', 'o', 'o']:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()
    if middlerow == ['x', 'x', 'x'] or middlerow == ['o', 'o', 'o']:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()
    if bottemrow == ['x', 'x', 'x'] or bottemrow == ['o', 'o', 'o']:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()

    #winning up and down
    if toprow[0] == middlerow[0] and middlerow[0] == bottemrow[0]:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()
    if toprow[1] == middlerow[1] and middlerow[1] == bottemrow[1]:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()
    if toprow[2] == middlerow[2] and middlerow[2] == bottemrow[2]:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()

    #winning diagonal
    if toprow[0] == middlerow[1] and middlerow[1] == bottemrow[2]:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()
    if toprow[2] == middlerow[1] and middlerow[1] == bottemrow[0]:
        time.sleep(1)
        winmessage()
        time.sleep(2)
        pygame.quit()



def xo():
    global toprow
    global middlerow
    global bottemrow
    global DIS

    font = pygame.font.SysFont('sans', 100)
    textx = font.render('x', True, (150, 200, 255))
    texto = font.render('o', True, (255, 255, 255))
    global turns

    pos = pygame.mouse.get_pos()
    # top left
    if 0 <= pos[0] <= WIDTH / 3 and 0 <= pos[1] <= HEIGHT / 3:
        if toprow[0] != 'x' and toprow[0] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, aa)
                turns += 1
                toprow[0] = 'x'
            else:
                DIS.blit(texto, aa)
                turns += 1
                toprow[0] = 'o'
    # top middle
    if WIDTH / 3 <= pos[0] <= WIDTH / 1.5 and 0 <= pos[1] <= HEIGHT / 3:
        if toprow[1] != 'x' and toprow[1] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, ab)
                turns += 1
                toprow[1] = 'x'
            else:
                DIS.blit(texto, ab)
                turns += 1
                toprow[1] = 'o'
    # top right
    if WIDTH / 1.5 <= pos[0] <= WIDTH and 0 <= pos[1] <= HEIGHT / 3:
        if toprow[2] != 'x' and toprow[2] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, ac)
                turns += 1
                toprow[2] = 'x'
            else:
                DIS.blit(texto, ac)
                turns += 1
                toprow[2] = 'o'
    # middle left
    if 0 <= pos[0] <= WIDTH / 3 and HEIGHT / 3 <= pos[1] <= HEIGHT / 1.5:
        if middlerow[0] != 'x' and middlerow[0] != 'o': 
            if turns % 2 == 0:
                DIS.blit(textx, ba)
                turns += 1
                middlerow[0] = 'x'
            else:
                DIS.blit(texto, ba)
                turns += 1
                middlerow[0] = 'o'
    # middle middle
    if WIDTH / 3 <= pos[0] <= WIDTH / 1.5 and HEIGHT / 3 <= pos[1] <= HEIGHT / 1.5:
        if middlerow[1] != 'x' and middlerow[1] != 'o': 
            if turns % 2 == 0:
                DIS.blit(textx, bb)
                turns += 1
                middlerow[1] = 'x'
            else:
                DIS.blit(texto, bb)
                turns += 1
                middlerow[1] = 'o'
    # middle right
    if WIDTH / 1.5 <= pos[0] <= WIDTH and HEIGHT / 3 <= pos[1] <= HEIGHT / 1.5:
        if middlerow[2] != 'x' and middlerow[2] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, bc)
                turns += 1
                middlerow[2] = 'x'
            else:
                DIS.blit(texto, bc)
                turns += 1
                middlerow[2] = 'o'
    # bottem left
    if 0 <= pos[0] <= WIDTH / 3 and HEIGHT / 1.5 <= pos[1] <= HEIGHT:
        if bottemrow[0] != 'x' and bottemrow[0] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, ca)
                turns += 1
                bottemrow[0] = 'x'
            else:
                DIS.blit(texto, ca)
                turns += 1
                bottemrow[0] = 'o'
    # bottem middle
    if WIDTH / 3 <= pos[0] <= WIDTH / 1.5 and HEIGHT / 1.5 <= pos[1] <= HEIGHT:
        if bottemrow[1] != 'x' and bottemrow[1] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, cb)
                turns += 1
                bottemrow[1] = 'x'
            else:
                DIS.blit(texto, cb)
                turns += 1
                bottemrow[1] = 'o'
    # bottem right
    if WIDTH / 1.5 <= pos[0] <= WIDTH and HEIGHT / 1.5 <= pos[1] <= HEIGHT:
        if bottemrow[2] != 'x' and bottemrow[2] != 'o':
            if turns % 2 == 0:
                DIS.blit(textx, cc)
                turns += 1
                bottemrow[2] = 'x'
            else:
                DIS.blit(texto, cc)
                turns  += 1
                bottemrow[2] = 'o'
    pygame.display.update()


def main():
    run = True
    drawboard()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xo()
                win()

    intro_screen.main()
