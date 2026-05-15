import pygame
import random
from generator import generate_trial
from ui import draw_card #Importiamo la funzione per la card
from scoring import apply_answer #Importiamo la funzione per il punteggio

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Progetto Informatica - Fase 7")

    clock = pygame.time.Clock()
    rng = random.Random()
    
    #Inizializziamo le variabili del gioco
    current_trial = generate_trial(rng)
    score = 0
    correct_count = 0
    wrong_count = 0

    running = True
    
    #Inizio del loop principale del gioco
    while running:
        #Recuperiamo tutti gli eventi (mouse, tastiera, ecc.) avvenuti in questo frame
        for event in pygame.event.get():
            
            #Se l'utente preme la "X" della finestra, il gioco si chiude
            if event.type == pygame.QUIT:
                running = False
            
            #Controlliamo se è stato premuto un tasto sulla tastiera
            if event.type == pygame.KEYDOWN:
                
                #Se viene premuto ESC, usciamo dal gioco
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                #Inizializziamo la variabile per la risposta dell'utente come "vuota" (None)
                #Questo serve a resettare la scelta a ogni pressione di un tasto
                user_answer = None
                
                if event.key == pygame.K_RIGHT:
                    user_answer = True
                elif event.key == pygame.K_LEFT:
                    user_answer = False
                
                #Se l'utente ha premuto una delle due frecce
                if user_answer is not None:
                    #1. Calcoliamo se la risposta è corretta
                    is_correct = (user_answer == current_trial.expected_answer)
                    
                    #2. Aggiorniamo il punteggio
                    score = apply_answer(score, is_correct)
                    
                    #3. Aggiorniamo i contatori globali
                    if is_correct:
                        correct_count += 1
                    else:
                        wrong_count += 1

                    print(f"Risposta: {user_answer} | Corretta: {is_correct} | Score: {score}")
                    print(f"Totali -> Corrette: {correct_count}, Sbagliate: {wrong_count}")
                    
                    #4. Generiamo un nuovo trial per la prossima carta
                    current_trial = generate_trial(rng)

        #RENDERING
        screen.fill((0, 0, 0)) # Sfondo nero

        #Disegniamo la carta attuale
        draw_card(screen, current_trial, None)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()