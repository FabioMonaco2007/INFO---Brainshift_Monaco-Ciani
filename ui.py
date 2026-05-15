import pygame

def draw_card(surface, trial, config):
    """Disegna la carta (rettangolo con lettera e numero) sullo schermo."""
    
    #Impostiamo le dimensioni e i colori della card
    card_width = 100
    card_height = 140
    card_color = (255, 255, 255)  # Bianco
    text_color = (0, 0, 0)        # Nero
    
    #Calcoliamo la posizione della X (centrata orizzontalmente)
    screen_width = surface.get_width()
    x = (screen_width - card_width) // 2
    
    #Calcoliamo la posizione della Y in base alla consegna (TOP o BOTTOM)
    if trial.position == 'TOP':
        y = 100
    else:
        y = 350

    #1. Disegniamo il rettangolo della carta
    card_rect = pygame.Rect(x, y, card_width, card_height)
    pygame.draw.rect(surface, card_color, card_rect)
    
    #2. Prepariamo il font per il testo
    font = pygame.font.SysFont("Arial", 50)
    
    #Creiamo la stringa da visualizzare (es. "A 7")
    content = f"{trial.letter} {trial.number}"
    
    #Creiamo l'immagine del testo (render)
    text_surface = font.render(content, True, text_color)
    
    #Centriamo il testo all'interno della carta
    text_rect = text_surface.get_rect(center=card_rect.center)
    
    #Disegniamo il testo sopra la carta
    surface.blit(text_surface, text_rect)