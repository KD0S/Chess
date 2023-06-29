import pygame as p
import local2player
import playerCPU
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
picking2 = False
bKbutton.draw(screen, p)
wKbutton.draw(screen, p)
color = "w"
p.display.update()

while picking:
    for e in p.event.get():
        if e.type == p.QUIT:
            picking = False
            break
        
        elif e.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            if bKbutton.rect.collidepoint(pos):
                color = "b"
                picking = False
                picking2 = True
                break
                
            elif wKbutton.rect.collidepoint(pos):
                color = "w"
                picking = False
                picking2 = True
                break

screen.fill(bgColor)
drawText(p, screen, 'Chess', textColor, 100, 180, 100)
drawText(p, screen, 'Pick Your Opponent', textColor, 40, 150, 250)
pvp = p.image.load("./images/pvp.png").convert_alpha()
pvp = p.transform.scale(pvp, (128, 128))
pve = p.image.load("./images/pve.png").convert_alpha()
pve = p.transform.scale(pve, (128, 128))
pveButton = Button(200, 350, pve, "K")
pvpButton = Button(350, 350, pvp, "K")
pveButton.draw(screen, p)
pvpButton.draw(screen, p)
p.display.update()
picking3 = False
while picking2:
    for e in p.event.get():
        if e.type == p.QUIT:
            picking2 = False
            break
        
        elif e.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            if pveButton.rect.collidepoint(pos):
                playerCPU.main(color)
                timer = False
                picking2 = False
                break
                
            elif pvpButton.rect.collidepoint(pos):
                timer = True 
                picking2 = False
                picking3 = True
                break
            
if timer:
    screen.fill(bgColor)
    drawText(p, screen, 'Chess', textColor, 100, 180, 100)
    drawText(p, screen, 'Choose Mode', textColor, 40, 200, 250)
    timer = p.image.load("./images/timer.png").convert_alpha()
    timer = p.transform.scale(timer, (128, 128))
    infinity = p.image.load("./images/infinity.png").convert_alpha()
    infinity = p.transform.scale(infinity, (128, 128))
    timerButton = Button(200, 350, timer, "K")
    infinityButton = Button(350, 350, infinity, "K")
    timerButton.draw(screen, p)
    infinityButton.draw(screen, p)
    p.display.update()

    while picking3:
        
        for e in p.event.get():
            if e.type == p.QUIT:
                picking3 = False
                break
            
            elif e.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if timerButton.rect.collidepoint(pos):
                    local2player.main(color, True)
                    picking3 = False
                    break
                    
                elif infinityButton.rect.collidepoint(pos):
                    local2player.main(color, False)
                    picking3 = False
                    break