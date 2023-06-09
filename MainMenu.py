import pygame as p
import ChessMain

p.init()
screen = p.display.set_mode((800, 700))
p.display.set_caption('Chess')
clock = p.time.Clock()
screen.fill(p.Color("green"))
running = True
textColor = (238,238,210)
bgColor = (118,150,86) 
screen.fill(bgColor)
font = p.font.SysFont(None, 100)
img = font.render("Chess", True, textColor)
screen.blit(img, (250 , 200))
font = p.font.SysFont(None, 40)
img = font.render("Press W to Play as White!", True, textColor)
screen.blit(img, (200 , 400))
img = font.render("Press B to Play as Black!", True, textColor)
screen.blit(img, (200 , 350))
p.display.update()

while running:
        for e in p.event.get():      
            
            if e.type == p.QUIT:
                running = False
            
            if e.type == p.KEYDOWN:
                if e.key == p.K_w:
                    ChessMain.main('w')
                    running = False
                    break
                elif e.key == p.K_b:
                    ChessMain.main('b')
                    running = False
                    break