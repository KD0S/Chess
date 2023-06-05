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
screen.blit(img, (256 , 200))
font = p.font.SysFont(None, 40)
img = font.render("Press S to Start!", True, textColor)
screen.blit(img, (256 , 400))
p.display.update()

while running:
        for e in p.event.get():      
            
            if e.type == p.QUIT:
                running = False
            
            if e.type == p.KEYDOWN:
                if e.key == p.K_s:
                    ChessMain.main('b')
                    running = False
                    break