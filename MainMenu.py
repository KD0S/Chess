import pygame as p
import ChessMain
from utils import Button, drawText
import colors

p.init()
screen = p.display.set_mode((700, 600))
p.display.set_caption('Chess')
clock = p.time.Clock()
screen.fill(p.Color("green"))
running = True
textColor = colors.lightGreen
bgColor = colors.darkGreen
screen.fill(bgColor)
drawText(p, screen, 'Chess', textColor, 100, 180, 100)
drawText(p, screen, 'Pick Your Side', textColor, 40, 200, 250)
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
