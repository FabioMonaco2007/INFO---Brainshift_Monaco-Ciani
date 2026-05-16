import pygame
import random
import time
from generator import generate_trial
from ui import draw_card
from scoring import apply_answer

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    rng = random.Random()
    font = pygame.font.SysFont("times-new-roman", 35)
    instruction_font = pygame.font.SysFont("times-new-roman", 24)
    
    # --- VARIABILI DI STATO ---
    state = "PLAYING"
    score = 0
    correct_count = 0
    wrong_count = 0
    
    start_time = time.time()
    current_trial = generate_trial(rng)

    # --- VARIABILI PER IL FEEDBACK  ---
    #Registra fino a quale momento nel tempo il feedback deve rimanere attivo
    feedback_until = 0.0
    #Memorizza il colore da dare alla carta durante il feedback
    feedback_color = (240, 240, 240) #Bianco morbido di default (nessun feedback)
    #Conserva la carta a cui l'utente sta rispondendo per mostrarla colorata
    feedback_trial = None

    running = True
    while running:
        #Calcolo del tempo per il gioco
        elapsed = time.time() - start_time
        
        if state == "PLAYING" and elapsed >= 60:
            state = "RESULTS"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                #LOGICA DURANTE IL GIOCO
                if state == "PLAYING":
                    #ATTENZIONE: Se il feedback visivo è attivo, ignoriamo i tasti premuti per evitare che l'utente risponda a raffica durante i 150ms
                    if time.time() < feedback_until:
                        continue

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
                        
                        #LOGICA FEEDBACK VISIVO
                        #Impostiamo il timer per il feedback a 150ms nel futuro (+ 0.15)
                        feedback_until = time.time() + 0.15
                        
                        #Scegliamo il colore in base alla correttezza: Verde o Rosso
                        if is_correct:
                            feedback_color = (46, 139, 87)   #Verde SeaGreen (Morbido)
                        else:
                            feedback_color = (178, 34, 34)   #Rosso FireBrick (Morbido)

                        #Salviamo il vecchio trial per mostrarlo colorato durante il feedback
                        feedback_trial = current_trial

                        #Carichiamo subito la carta successiva
                        current_trial = generate_trial(rng)
                
                #LOGICA NELLA SCHERMATA RISULTATI
                elif state == "RESULTS":
                    if event.key == pygame.K_r:
                        state = "PLAYING"
                        score = 0
                        correct_count = 0
                        wrong_count = 0
                        start_time = time.time()
                        feedback_until = 0.0
                        feedback_trial = None
                        current_trial = generate_trial(rng)

        # --- RENDERING ---
        #Sfondo grigio scurissimo molto più elegante del nero puro
        screen.fill((30, 30, 30))

        if state == "PLAYING":
            #CONTROLLO SE IL FEEDBACK È ANCORA ATTIVO 
            if time.time() < feedback_until and feedback_trial is not None:
                
                #Disegniamo un rettangolo colorato (Verde/Rosso) grande come la carta
                card_width = 100
                card_height = 140
                x = (screen_width - card_width) // 2
                y = 100 if feedback_trial.position == 'TOP' else 350
                
                #Disegniamo lo sfondo colorato di feedback
                pygame.draw.rect(screen, feedback_color, pygame.Rect(x, y, card_width, card_height))
                
                #Sopra ci stampiamo il testo della carta
                font_card = pygame.font.SysFont("times-new-roman", 50)
                content = f"{feedback_trial.letter} {feedback_trial.number}"
                text_surface = font_card.render(content, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(x + card_width//2, y + card_height//2))
                screen.blit(text_surface, text_rect)
            else:
                #Se il feedback non è attivo, disegna la carta normale (Bianca)
                draw_card(screen, current_trial, None)
            
            # --- ISTRUZIONI DI BASE CON FADING ---
            #Smettiamo di disegnarlo quando corrette >= 10
            if correct_count < 10:
                #Definiamo il colore grigio chiaro (200, 200, 200)
                rule_color = (180, 180, 180)
                
                #Regola per la posizione ALTO (TOP)
                top_text = instruction_font.render("In ALTO: Il numero è PARI?", True, rule_color)
                screen.blit(top_text, (screen_width // 2 - top_text.get_width() // 2, 60))
                
                #Regola per la posizione BASSO (BOTTOM)
                bottom_text = instruction_font.render("In BASSO: La lettera è una VOCALE?", True, rule_color)
                screen.blit(bottom_text, (screen_width // 2 - bottom_text.get_width() // 2, 510))
            
            #Mostriamo il timer
            countdown = max(0, int(60 - elapsed))
            timer_text = font.render(f"Timer: {countdown}", True, (240, 240, 240))
            screen.blit(timer_text, (screen_width // 2 - timer_text.get_width() // 2, 15))
            
        elif state == "RESULTS":
            total = correct_count + wrong_count
            accuracy = (correct_count / total * 100) if total > 0 else 0
            
            lines = [
                f"Punteggio: {score}",
                f"Corrette: {correct_count}",
                f"Sbagliate: {wrong_count}",
                f"Accuratezza: {accuracy:.1f}%",
                "Premi R per rigiocare"
            ]
            
            for i, line in enumerate(lines):
                text_surf = font.render(line, True, (240, 240, 240))
                screen.blit(text_surf, (screen_width // 2 - text_surf.get_width() // 2, 200 + (i * 45)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()