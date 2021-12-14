import pygame
from sudokusolution import Sudoku

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku")

white = (255, 255, 255)
black = (0, 0, 0)

topcord = []
bottomcord = []
leftcord = []
rightcord = []

for i in range(10):
    topcord.append((50 + i*(400/9), 50))
    bottomcord.append((50 + i*(400/9), 450))
    leftcord.append((50, 50 + i*(400/9)))
    rightcord.append((450, 50 + i*(400/9)))

cellPos = []
for i in range(9):
    poss = []
    for j in  range(9):
        poss.append([(leftcord[j][1] + leftcord[j+1][1]) / 2 , (topcord[i][0] + topcord[i+1][0]) / 2])
    cellPos.append(poss)

crossLines = [(50, 183.33), (450, 183.33), (450, 316.66), (50, 316.66)]

screen.fill(white)
for i in range(10):
    siz = 5 if i % 3 == 0 else 3
    pygame.draw.line(screen, (0, 0, 0), topcord[i], bottomcord[i], siz)
    pygame.draw.line(screen, (0, 0, 0), leftcord[i], rightcord[i], siz)

font = pygame.font.Font('freesansbold.ttf', 24)

time_step = 50

def solution(my_sudoku, ind=0):
    if ind == len(my_sudoku.pairs):
        return True
    pygame.time.delay(time_step)
    for i in range(9):
        my_sudoku.sudoku[my_sudoku.pairs[ind][0]][my_sudoku.pairs[ind][1]] = i + 1
        text = font.render(str(i+1), True, black, white)
        textrec = text.get_rect()
        textrec.center = cellPos[my_sudoku.pairs[ind][0]][my_sudoku.pairs[ind][1]]
        screen.blit(text, textrec)
        pygame.display.update()
        if my_sudoku.checksudoku(ind):
            if solution(my_sudoku, ind + 1):
                return True
    text = font.render("#", True, black, white)
    textrec = text.get_rect()
    textrec.center = cellPos[my_sudoku.pairs[ind][0]][my_sudoku.pairs[ind][1]]
    screen.blit(text, textrec)
    pygame.display.update()
    my_sudoku.sudoku[my_sudoku.pairs[ind][0]][my_sudoku.pairs[ind][1]] = 0
    return False
# ======================= Done with Outline =============================================
sudoku = [[2, 4, 0, 0, 5, 7, 3, 6, 0],
          [0, 0, 0, 0, 0, 8, 0, 0, 9],
          [3, 7, 8, 0, 0, 0, 2, 0, 0],
          [0, 6, 0, 0, 4, 1, 7, 0, 2],
          [0, 8, 0, 0, 0, 0, 0, 0, 5],
          [0, 0, 0, 0, 0, 5, 0, 1, 0],
          [1, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 6],
          [0, 0, 0, 8, 1, 2, 0, 0, 0]]
my_sudoku = Sudoku(sudoku)

for i in range(9):
    for j in range(9):
        if my_sudoku.sudoku[i][j] != 0:
            text = font.render(str(my_sudoku.sudoku[i][j]), True, black, white)
            textrec = text.get_rect()
            textrec.center = cellPos[i][j]
            screen.blit(text, textrec)
            pygame.time.delay(5)
            pygame.display.update()

while True:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        solution(my_sudoku)
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
