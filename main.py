import pygame
from wolvbasics import *
red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)

def main():
    pygame.init()
    pygame.font.init()
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png')
    menuoptions = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-550,0])
    fac.display_bkg()
    mouseclick = False
    fac.display_menu()

    while not end:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouseclick = True
            if event.type == pygame.MOUSEBUTTONUP:
                    mouseclick = False
        mousepos = pygame.mouse.get_pos()
        mouseonoption = fac.checkmouse(mousepos)

        if mouseonoption != -1 and mouseclick: #Detecting Option Clicked
            print "Menu Option Clicked: ", menuoptions[mouseonoption]
            mouseclick = False
        if mouseonoption != -1 and mouseonoption not in fac.getTurned():
            #Turns blue the option the mouse is on
            txt = menuoptions[mouseonoption]
            fac.appendTurned(mouseonoption)
            newrender = bob.buildtxtrender(txt, 0, darkBlue)
            fac.popmenurenders(mouseonoption)
            fac.insertmenurenders(mouseonoption, newrender)
            screen.fill(black)
            fac.display_bkg()
            fac.display_menu()
        elif fac.getTurned() != [] and mouseonoption == -1:
            #Returns all text to normal colors
            fac.emptyTurned()
            fac.resetmenurenders()
            screen.fill(black)
            fac.display_bkg()
            fac.display_menu()
        elif len(fac.getTurned()) > 1:
            fac.emptyTurned()
            fac.resetmenurenders()
            txt = menuoptions[mouseonoption]
            fac.appendTurned(mouseonoption)
            newrender = bob.buildtxtrender(txt, 0, darkBlue)
            fac.popmenurenders(mouseonoption)
            fac.insertmenurenders(mouseonoption, newrender)
            screen.fill(black)
            fac.display_bkg()
            fac.display_menu()
    pygame.quit()

if __name__ == '__main__':
    main()
