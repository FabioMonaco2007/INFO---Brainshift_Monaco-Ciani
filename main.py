import pygame

def main():
    #Inizializza tutti i moduli di pygame 
    pygame.init()

    #Configurazione della finestra (800x600)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    #Creazione del Clock per gestire il framerate 
    clock = pygame.time.Clock()

    running = True
    while running:
        #1. Gestione Eventi
        for event in pygame.event.get():
            #Chiusura tramite la X della finestra
            if event.type == pygame.QUIT:
                running = False
            
            #Chiusura tramite il tasto ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #2. Aggiornamento Logica (vuoto per ora)

        #3. Finestra nera
        screen.fill((0, 0, 0))

        #Aggiorna il display 
        pygame.display.flip()

        #Limita il framerate a 60 FPS 
        clock.tick(60)

    #Uscita pulita dal gioco
    pygame.quit()

if __name__ == "__main__":
    main()