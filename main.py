import pygame
import random
import time
from generator import generate_trial
from ui import draw_card
from scoring import apply_answer

def main():
    pygame.init()

    #Dimensioni richieste
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    clock = pygame.time.Clock()
    rng = random.Random()
    font = pygame.font.SysFont("Arial", 30)
    
    state = "PLAYING" #Stato iniziale
    score = 0
    correct_count = 0
    wrong_count = 0
    
    #Al primo trial salvate start_time
    start_time = time.time()

    current_trial = generate_trial(rng)

    running = True
    while running:
        #A ogni frame calcolate elapsed
        elapsed = time.time() - start_time
        
        #Se elapsed >= 60, passate allo stato RESULTS
        if state == "PLAYING" and elapsed >= 60:
            state = "RESULTS"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                #Gestione durante il gioco
                if state == "PLAYING":
                    user_answer = None
                    if event.key == pygame.K_RIGHT:
                        user_answer = True
                    elif event.key == pygame.K_LEFT:
                        user_answer = False
                    
                    if user_answer is not None:
                        is_correct = (user_answer == current_trial.expected_answer)
                        score = apply_answer(score, is_correct)
                        if is_correct:
                            correct_count += 1
                        else:
                            wrong_count += 1
                        #Genera nuovo trial
                        current_trial = generate_trial(rng)
                
                #Premendo R reimpostate tutto e tornate in PLAYING
                elif state == "RESULTS":
                    if event.key == pygame.K_r:
                        state = "PLAYING"
                        score = 0
                        correct_count = 0
                        wrong_count = 0
                        start_time = time.time()
                        current_trial = generate_trial(rng)

        #RENDERING
        screen.fill((0, 0, 0))

        if state == "PLAYING":
            #Disegnate la carta
            draw_card(screen, current_trial, None)
            
            #Mostrate il timer in alto (conto alla rovescia)
            countdown = max(0, int(60 - elapsed))
            timer_text = font.render(f"Timer: {countdown}", True, (255, 255, 255))
            screen.blit(timer_text, (350, 20))
            
        elif state == "RESULTS":
            #Mostrate il riepilogo
            total = correct_count + wrong_count
            accuracy = (correct_count / total * 100) if total > 0 else 0
            
            #Linee di testo
            lines = [
                f"Punteggio: {score}",
                f"Corrette: {correct_count}",
                f"Sbagliate: {wrong_count}",
                f"Accuratezza: {accuracy:.1f}%",
                "Premi R per rigiocare"
            ]
            
            for i, line in enumerate(lines):
                text_surf = font.render(line, True, (255, 255, 255))
                screen.blit(text_surf, (300, 200 + (i * 40)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()