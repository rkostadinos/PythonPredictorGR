import pygame
import random
from sys import exit
"""
inf2021192 Κωνσταντίνος Ράπτης
Τρίλιζα με GUI χρησιμοποιώντας την Pygame βιβλιοθήκη
Δεν έχει bug από ό,τι γνωρίζουμε.
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
screen.blit(BackGround_surface, (0, 0))
BreakerBool = False # Αυτή η μεταβλητή boolean χρησιμοποιείται για να σπάσει το main loop (γραμμή 38)
M_counter = 0



while BreakerBool == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Horizontal_surface1, (0, 137.5)) # Εδώ δημιουργούνται οι ευθείες γραμμές του grid της τρίλιζας
    screen.blit(Horizontal_surface2, (0, 317.5))
    screen.blit(Vertical_surface1, (137.5, 0))
    screen.blit(Vertical_surface2, (317.5, 0))
    keys = pygame.key.get_pressed()

    # Αυτή η συνάρτηση δίνει ένα ψευδοτυχαίο αριθμό απο το 1 μέχρι το 20
    # με σκοπό να χρησιμοποιηθεί η μεταβλητή altPredict για την αλλαγή της αρχικής πρόβλεψης
    def winnerChance():
        AltPredict = random.randint(1, 20)





    # Αυτή η συνάρτηση τσεκάρει κάθε γραμμή, εμφανίζει 'X/O WON' και σπάει την while loop
    def CheckRows():
        global BreakerBool
        if TTT_Board[0] == TTT_Board[1] == TTT_Board[2] and TTT_Board[0] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[0] == TTT_Board[1] == TTT_Board[2] and TTT_Board[0] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        if TTT_Board[3] == TTT_Board[4] == TTT_Board[5] and TTT_Board[3] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[3] == TTT_Board[4] == TTT_Board[5] and TTT_Board[3] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True


        if TTT_Board[6] == TTT_Board[7] == TTT_Board[8] and TTT_Board[6] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[6] == TTT_Board[7] == TTT_Board[8] and TTT_Board[6] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True




    # Αυτή η συνάρτηση τσεκάρει κάθε στήλη, εμφανίζει 'X/O WON' και σπάει την while loop
    def CheckColumns():
        global BreakerBool
        if TTT_Board[0] == TTT_Board[3] == TTT_Board[6] and TTT_Board[0] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[0] == TTT_Board[3] == TTT_Board[6] and TTT_Board[0] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        if TTT_Board[1] == TTT_Board[4] == TTT_Board[7] and TTT_Board[1] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[1] == TTT_Board[4] == TTT_Board[7] and TTT_Board[1] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True


        if TTT_Board[2] == TTT_Board[5] == TTT_Board[8] and TTT_Board[2] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[2] == TTT_Board[5] == TTT_Board[8] and TTT_Board[2] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True



    def CheckDiagonals(): # Αυτή η συνάρτηση τσεκάρει κάθε διαγώνιο, εμφανίζει 'X/O WON' και σπάει την while loop
        global BreakerBool
        if TTT_Board[0] == TTT_Board[4] == TTT_Board[8] and TTT_Board[0] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[0] == TTT_Board[4] == TTT_Board[8] and TTT_Board[0] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        if TTT_Board[2] == TTT_Board[4] == TTT_Board[6] and TTT_Board[2] == 'x':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('X WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True

        elif TTT_Board[2] == TTT_Board[4] == TTT_Board[6] and TTT_Board[2] == 'o':
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('O WON', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True



    # Αυτή η συνάρτηση τσεκάρει για ισοπαλία και εμφανίζει την κατάσταση ισοπαλίας στο τέλος
    def CheckTie():
        global BreakerBool
        if M_counter >= 9:
            screen.blit(BackGround_surface, (0, 0))
            text_surface = font.render('TIE', True, 'Black')
            screen.blit(text_surface, (105, 100))
            BreakerBool = True






    #switchP Αλλάζει την/τον παίχτη, M_counter λειτουργεί ως μετρητής για να ελέγχει την σειρά κάθε παίχτη
    #Μιας και η πρώτη σειρά θα είναι πάντα το X η πρώτη κίνηση θα αυξήσει το M_counter ανά 1, κ.ο.κ

    def switchP():
        CheckWinConditions()
        if M_counter == 0:
            Player_X()
        elif M_counter == 1:
            Player_O()
        elif M_counter == 2:
            Player_X()
        elif M_counter == 3:
            Player_O()
        elif M_counter == 4:
            Player_X()
        elif M_counter == 5:
            Player_O()
        elif M_counter == 6:
            Player_X()
        elif M_counter == 7:
            Player_O()
        elif M_counter == 8:
            Player_X()
        elif M_counter == 9:
            CheckTie()
            CheckWinConditions()





    # Η χρησιμότητα της συνάρτησης είναι να αναπαριστά τον παίχτη όμικρον
    # καθώς τσεκάρει αν κάθε κελί είναι άδειο και το πλήκτρο που πατήθηκε είναι κάποιο από τα νούμερα 1 εώς 9
    def Player_O():
        global M_counter
        global TTT_Board
        if keys[pygame.K_1] and TTT_Board[0] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (20, 20))
            TTT_Board[0] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_2] and TTT_Board[1] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (190, 20))
            TTT_Board[1] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_3] and TTT_Board[2] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (365, 20))
            TTT_Board[2] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_4] and TTT_Board[3] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (20, 185))
            TTT_Board[3] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_5] and TTT_Board[4] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (185, 185))
            TTT_Board[4] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_6] and TTT_Board[5] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (365, 185))
            TTT_Board[5] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_7] and TTT_Board[6] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (20, 360))
            TTT_Board[6] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_8] and TTT_Board[7] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (190, 360))
            TTT_Board[7] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_9] and TTT_Board[8] == '-':
            Omicron_Surface = pygame.image.load('Omicron.png')
            screen.blit(Omicron_Surface, (360, 360))
            TTT_Board[8] = 'o'
            M_counter += 1
            CheckWinConditions()
            switchP()


    # Η χρησιμότητα της συνάρτησης είναι να αναπαριστά τον παίχτη Χι
    # καθώς τσεκάρει αν κάθε κελί είναι άδειο και το πλήκτρο που πατήθηκε είναι κάποιο από τα νούμερα 1 εώς 9
    def Player_X():
        global TTT_Board
        global M_counter
        if keys[pygame.K_1] and TTT_Board[0] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (20, 20))
            TTT_Board[0] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()


        elif keys[pygame.K_2] and TTT_Board[1] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (190, 20))
            TTT_Board[1] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_3] and TTT_Board[2] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (365, 20))
            TTT_Board[2] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_4] and TTT_Board[3] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (20, 185))
            TTT_Board[3] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_5] and TTT_Board[4] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (185, 185))
            TTT_Board[4] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()


        elif keys[pygame.K_6] and TTT_Board[5] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (365, 185))
            TTT_Board[5] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_7] and TTT_Board[6] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (20, 360))
            TTT_Board[6] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

        elif keys[pygame.K_8] and TTT_Board[7] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (190, 360))
            TTT_Board[7] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()


        elif keys[pygame.K_9] and TTT_Board[8] == '-':
            Xi_Surface = pygame.image.load('Xi.png')
            screen.blit(Xi_Surface, (360, 360))
            TTT_Board[8] = 'x'
            M_counter += 1
            CheckWinConditions()
            switchP()

    def CheckWinConditions():
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        CheckTie()




    switchP()



    pygame.display.update() # Ανανέωση του display
    clock.tick(60) # βάζει το παιχνίδι σε 60 Frames Per Second
