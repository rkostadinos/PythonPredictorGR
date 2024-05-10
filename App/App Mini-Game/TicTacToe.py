import pygame
from sys import exit
"""
inf2021192 Κωνσταντίνος Ράπτης
Τρίλιζα με GUI χρησιμοποιώντας την Pygame βιβλιοθήκη
Ο κώδικας δεν είναι ολοκληρωμένος ακόμα, διότι έχει κάποια bug.
Βοήθεια για τον κώδικα πήρα από:
https://youtu.be/AY9MnQ4x3zk?si=MRJlrXhmpD3PlMQy
https://youtu.be/dK6gJw4-NCo?si=Q5uGz6X6o4kFAs5p
"""



pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Τρίλιζα")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 80)
TTT_Board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # Αυτή η λίστα αναπαριστά το grid της τρίλιζας

BackGround_surface = pygame.Surface((500, 500)) # Από εδώ και μέχρι screen.blit είναι η δημιουργία του grid της τρίλιζας
BackGround_surface.fill('White')
Horizontal_surface1 = pygame.Surface((500, 20))
Horizontal_surface1.fill('Black')
Horizontal_surface2 = pygame.Surface((500, 20))
Horizontal_surface2.fill('Black')
Vertical_surface1 = pygame.Surface((20, 500))
Vertical_surface1.fill('Black')
Vertical_surface2 = pygame.Surface((20, 500))
Vertical_surface2.fill('Black')
Omicron_Surface = pygame.image.load('Omicron.png')
Xi_Surface = pygame.image.load('Xi.png')
Xi_Surf_Boolean = True
screen.blit(BackGround_surface, (0, 0))
BreakerBool = False # Αυτή η μεταβλητή boolean χρησιμοποιείται για να σπάσει το main loop (γραμμή 38)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # screen.blit(BackGround_surface, (0, 0))
    screen.blit(Horizontal_surface1, (0, 137.5)) # Εδώ δημιουργούνται οι ευθείες γραμμές του grid της τρίλιζας
    screen.blit(Horizontal_surface2, (0, 317.5))
    screen.blit(Vertical_surface1, (137.5, 0))
    screen.blit(Vertical_surface2, (317.5, 0))
    # screen.blit(Omicron_Surface, (190, 360))
    keys = pygame.key.get_pressed()
    if BreakerBool:
        break
    def CheckRows(): # Αυτή η συνάρτηση τσεκάρει κάθε γραμμή, εμφανίζει 'YOU WON' και σπάει την while loop
        global BreakerBool
        if TTT_Board[0] == TTT_Board[1] == TTT_Board[2] and TTT_Board[0] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
        if TTT_Board[3] == TTT_Board[4] == TTT_Board[5] and TTT_Board[3] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
        if TTT_Board[6] == TTT_Board[7] == TTT_Board[8] and TTT_Board[6] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

    def CheckColumns(): # Αυτή η συνάρτηση τσεκάρει κάθε στήλη, εμφανίζει 'YOU WON' και σπάει την while loop
        global BreakerBool
        if TTT_Board[0] == TTT_Board[3] == TTT_Board[6] and TTT_Board[0] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
        if TTT_Board[1] == TTT_Board[4] == TTT_Board[7] and TTT_Board[1] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
        if TTT_Board[2] == TTT_Board[5] == TTT_Board[8] and TTT_Board[2] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
    def CheckDiagonals(): # Αυτή η συνάρτηση τσεκάρει κάθε διαγώνιο, εμφανίζει 'YOU WON' και σπάει την while loop
        global BreakerBool
        if TTT_Board[0] == TTT_Board[4] == TTT_Board[8] and TTT_Board[0] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True
        if TTT_Board[2] == TTT_Board[4] == TTT_Board[6] and TTT_Board[2] == '1':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('YOU WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

    def switchPlayer(): # Η χρήση της συνάρτησης είναι να αλλάζει τον παίχτη (δηλαδή, σειρά 1 ειναι Χ και σειρά 2 ειναι Ο, κλπ) και τσεκάρει τις συνθήκες νίκης
        if keys[pygame.K_1] and TTT_Board[0] == '-':
            screen.blit(Omicron_Surface, (20, 20))
            TTT_Board[0] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_2] and TTT_Board[1] == '-':
            screen.blit(Omicron_Surface, (190, 20))
            TTT_Board[1] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_3] and TTT_Board[2] == '-':
            screen.blit(Omicron_Surface, (190, 20))
            TTT_Board[2] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_4]:
            screen.blit(Omicron_Surface, (20, 185))
            TTT_Board[3] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_5]:
            screen.blit(Omicron_Surface, (185, 185))
            TTT_Board[4] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_6]:
            screen.blit(Omicron_Surface, (365, 185))
            TTT_Board[5] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_7]:
            screen.blit(Omicron_Surface, (20, 360))
            TTT_Board[6] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_8]:
            screen.blit(Omicron_Surface, (190, 360))
            TTT_Board[7] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()
        if keys[pygame.K_9]:
            screen.blit(Omicron_Surface, (360, 360))
            TTT_Board[8] = '1'
            CheckRows()
            CheckColumns()
            CheckDiagonals()

    if keys[pygame.K_1]: #Οι if snippets τσεκάρουν για τους εισόδους του πληκτρολογίου και βάζουν στην επιφάνεια το Χ
        screen.blit(Xi_Surface, (20, 20))
        TTT_Board[0] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_2]:
        screen.blit(Xi_Surface, (190, 20))
        TTT_Board[1] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_3]:
        screen.blit(Xi_Surface, (365, 20))
        TTT_Board[2] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_4]:
        screen.blit(Xi_Surface, (20, 185))
        TTT_Board[3] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_5]:
        screen.blit(Xi_Surface, (185, 185))
        TTT_Board[4] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_6]:
        screen.blit(Xi_Surface, (365, 185))
        TTT_Board[5] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_7]:
        screen.blit(Xi_Surface, (20, 360))
        TTT_Board[6] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_8]:
        screen.blit(Xi_Surface, (190, 360))
        TTT_Board[7] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()
    if keys[pygame.K_9]:
        screen.blit(Xi_Surface, (360, 360))
        TTT_Board[8] = '1'
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        switchPlayer()


    pygame.display.update() # Ανανέωση του display
    clock.tick(60) # βάζει την το παιχνίδι σε 60 Frames Per Second
