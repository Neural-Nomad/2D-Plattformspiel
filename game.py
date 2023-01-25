import pygame

# Initialisieren von Pygame
pygame.init()

# Bildschirmgröße festlegen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Titel des Fensters festlegen
pygame.display.set_caption("Mein 2D-Plattformspiel")

# Hintergrundbild laden
background_image = pygame.image.load("background.png")

# Spieler-Charakter erstellen
player_image = pygame.image.load("player.png")
player_x = 50
player_y = 50
player_speed = 5

# Hindernisse erstellen
obstacle_image = pygame.image.load("obstacle.png")
obstacle_list = [(300, 400), (500, 100), (150, 250)]

# Hauptschleife des Spiels
running = True
while running:
    # Bildschirm auf Hintergrundbild zurücksetzen
    screen.blit(background_image, (0, 0))
    
    # Hindernisse auf Bildschirm zeichnen
    for obstacle in obstacle_list:
        screen.blit(obstacle_image, obstacle)
    
    # Spieler-Charakter auf Bildschirm zeichnen
    screen.blit(player_image, (player_x, player_y))
    
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Tasteneingabe abfragen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Bildschirm aktualisieren
    pygame.display.update()

# Beenden von Pygame
pygame.quit()
