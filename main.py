import pygame
import random
from generator import generate_trial
from ui import draw_card

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Progetto Informatica - Fase 6")

    clock = pygame.time.Clock()
    
    #Inizializziamo il generatore di numeri casuali
    rng = random.Random()
    
    #GENERIAMO IL TRIAL (La carta da visualizzare)
    #Lo facciamo prima del loop così rimane fisso a schermo
    current_trial = generate_trial(rng)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #LOGICA: per ora non dobbiamo aggiornare nulla
        
        #RENDERING - Sfondo nero
        screen.fill((0, 0, 0))

        #Chiamiamo la funzione per disegnare la carta
        #Passiamo None a config perché per ora non lo stiamo usando
        draw_card(screen, current_trial, None)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()