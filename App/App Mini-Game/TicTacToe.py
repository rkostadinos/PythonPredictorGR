#!/usr/bin/python3

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
Horizontal_surface = pygame.Surface((500, 20))
Horizontal_surface.fill('Black')
Vertical_surface = pygame.Surface((20, 500))
Vertical_surface.fill('Black')
screen.blit(BackGround_surface, (0, 0))
BreakerBool = False # Αυτή η μεταβλητή boolean χρησιμοποιείται για να σπάσει το main loop (γραμμή 38)
M_counter = 0


while BreakerBool == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Horizontal_surface, (0, 137.5)) # Εδώ δημιουργούνται οι ευθείες γραμμές του grid της τρίλιζας
    screen.blit(Horizontal_surface, (0, 317.5))
    screen.blit(Vertical_surface, (137.5, 0))
    screen.blit(Vertical_surface, (317.5, 0))
    keys = pygame.key.get_pressed()

    # Αυτή η συνάρτηση δίνει ένα ψευδοτυχαίο αριθμό απο το 1 μέχρι το 20
    # με σκοπό να χρησιμοποιηθεί η μεταβλητή altPredict για την αλλαγή της αρχικής πρόβλεψης
    def winnerChance():
        AltPredict = random.randint(1, 20)

    WonMessageX = 'Το X νίκησε!'
    WonMessageO = 'Το Ο νίκησε!'
    # Αυτή η συνάρτηση χρησιμοποιείται για να εμφανιστεί μήνυμα νίκης στο τέλος
    def showmessage(WonMessage):
        global BreakerBool
        screen.blit(BackGround_surface, (0, 0))
        text_surface = font.render(WonMessage, True, 'Black')
        screen.blit(text_surface, (105, 100))
        BreakerBool = True           
        
    
    def rows(num):
        if TTT_Board[num] == TTT_Board[num + 1] == TTT_Board[num + 2] and TTT_Board[num] == 'x':
            showmessage(WonMessageX)

        elif TTT_Board[num] == TTT_Board[num + 1] == TTT_Board[num + 2] and TTT_Board[num] == 'o':
           showmessage(WonMessageO)
    # Αυτές οι δύο συναρτήσεις τσεκάρουν κάθε γραμμή, εμφανίζεται 'X/O WON' και σπάει την while loop στο τ
    def CheckRows():
        rows(0)
        rows(3)
        rows(6)
    
    def colms(num): # αυτή η συνάρτηση τσεκάρει αν σε κάθε στήλη υπάρχουν 3 ίδια γράμματα στην σειρά
        if TTT_Board[num] == TTT_Board[num + 3] == TTT_Board[num + 6] and TTT_Board[num] == 'x':
            showmessage(WonMessageX)

        elif TTT_Board[num] == TTT_Board[num + 3] == TTT_Board[num + 6] and TTT_Board[num] == 'o':
           showmessage(WonMessageO)    


    # Αυτή η συνάρτηση τσεκάρει κάθε στήλη χρησιμοποιώντας την πάνω
    def CheckColumns():
        colms(0)
        colms(1)
        colms(2)
                

    def Diags(num):
        
        third_cell = 8 - num 
            
        if TTT_Board[num] == TTT_Board[4] == TTT_Board[third_cell] and TTT_Board[num] == 'x':
            showmessage(WonMessageX)
        elif TTT_Board[num] == TTT_Board[4] == TTT_Board[third_cell] and TTT_Board[num] == 'o':
            showmessage(WonMessageO)
                    

    def CheckDiagonals(): # Αυτή η συνάρτηση τσεκάρει κάθε διαγώνιο χρησιμοποιώντας την πάνω
        Diags(0)
        Diags(2)
                

    TieMessage = 'TIE'
    # Αυτή η συνάρτηση τσεκάρει για ισοπαλία και εμφανίζει την κατάσταση ισοπαλίας στο τέλος
    def CheckTie():
        global BreakerBool
        if M_counter >= 9:
            showmessage(TieMessage)


    #switchP Αλλάζει την/τον παίχτη, M_counter λειτουργεί ως μετρητής για να ελέγχει την σειρά κάθε παίχτη
    #Μιας και η πρώτη σειρά θα είναι πάντα το X η πρώτη κίνηση θα αυξήσει το M_counter ανά 1, κ.ο.κ
    #όμως, κάθε φορά που είναι σειρά του player_x το m_counter είναι άρτιος αριθμός
    #επομένως χρειάζεται μόνο να ελέγχεται αν η τιμή του m_counter είναι ζυγός αριθμός
    #ώστε να καθοριστεί ποιό άτομο θα παίξει
    def switchP():
        CheckWinConditions()
        if M_counter % 2 == 0:
            Player_X()
        else:
            Player_O()
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
    # αυτή η συνάρτηση καλεί όλες τις συναρτήσεις που ελέχγουν τις προϋποθέσεις νίκης
    def CheckWinConditions():
        CheckRows()
        CheckColumns()
        CheckDiagonals()
        CheckTie()


    switchP()


    pygame.display.update() # Ανανέωση του display
    clock.tick(60) # βάζει το παιχνίδι σε 60 Frames Per Second
clock.tick(1)
