import pygame as p
import ChessMain
from utils import Button

p.init()
screen = p.display.set_mode((700, 600))
p.display.set_caption('Chess')
clock = p.time.Clock()
screen.fill(p.Color("green"))
running = True
textColor = (238,238,210)
bgColor = (118,150,86) 
screen.fill(bgColor)
font = p.font.Font('./fonts/Poppins-Bold.ttf', 100)
img = font.render("Chess", True, textColor)
screen.blit(img, (180 , 100))
font = p.font.Font('./fonts/Poppins-Bold.ttf', 40)
img = font.render("Pick Your Side", True, textColor)
screen.blit(img, (200 , 250))
imageBK = p.image.load("./images/bK_logo.png").convert_alpha()
imageBK = p.transform.scale(imageBK, (128, 128))
imageWK = p.image.load("./images/wK_logo.png").convert_alpha()
imageWK = p.transform.scale(imageWK, (128, 128))
bKbutton = Button(200, 350, imageBK, "K")
wKbutton = Button(350, 350, imageWK, "K")
picking = True
bKbutton.draw(screen, p)
wKbutton.draw(screen, p)

p.display.update()
while picking:
    for e in p.event.get():
        if e.type == p.QUIT:
            picking = False
            break
        
        elif e.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            if bKbutton.rect.collidepoint(pos):
                ChessMain.main('b')
                picking = False
                break
                
            elif wKbutton.rect.collidepoint(pos):
                ChessMain.main('w')
                picking = False
                break
