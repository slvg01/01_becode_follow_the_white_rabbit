# Matrix_Has_You 3
#This python code reproduces messages on the terminal emulating those from the film "The Matrix" (1999).
from os import system, name
from time import sleep
from tkinter import *
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
import time

def jouer_musique(fichier_mp3):
    pygame.init()
    pygame.mixer.init()
 
    pygame.mixer.music.load(fichier_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): #atttendez que la musique se termine
        time.sleep(0)
    
    pygame.mixer.quit()
    pygame.quit()

fichier_mp3 = r"P:\8 - Sylvain PERSO\7 - Jobsrch\10 - New Job\Formation\FORMATION\2 - DATA SCIENCE INITIATION - Digitalcity\Exo PYTHON\01_DGCY_01_intro_python\Matrix\phone2.mp3"
jouer_musique(fichier_mp3)

fichier_mp3 = r"P:\8 - Sylvain PERSO\7 - Jobsrch\10 - New Job\Formation\FORMATION\2 - DATA SCIENCE INITIATION - Digitalcity\Exo PYTHON\01_DGCY_01_intro_python\Matrix\phone3.mp3"
jouer_musique(fichier_mp3)

fichier_mp3 = r"P:\8 - Sylvain PERSO\7 - Jobsrch\10 - New Job\Formation\FORMATION\2 - DATA SCIENCE INITIATION - Digitalcity\Exo PYTHON\01_DGCY_01_intro_python\Matrix\phone4.mp3"
jouer_musique(fichier_mp3)


def liveType (text='liveType demo text', delay=0.02, remain=2.5):
    for letter in text:
        print (letter, end='', flush=True)
        sleep (delay)
    sleep (remain)


LIGHT_GREEN = '\033[92m' # These special strings here are called ANSI escape codes, also SGR. They are here for text formating.
DARK_GREEN = "\033[0;32m"
BOLDON = '\033[1m'
CURSORON = '\x1b[?25h'
CURSOROFF = '\x1b[?25l'


remainFactor = 0.2    # Affects typing speed. Lower for faster emulation. '1' for real scene times.
delayFactor = 0.7     # Affects messages display time. Lower for faster emulation. '1' for real scene times. 
_here = "\n\n\n      " # This is meant for later prints positioning

urName = "BeCode" # If you change this to a name longer than "Neo" provide times accordingly to "secs1" list.
msg1 = f"Knock, Knock, Knock, {urName}..."
msg2 = "Greetings from Sylvain"
msg3 = f"Looking for the white rabbit, {urName}...? "
  


# The following lists (secs1 and secs2) are the time lapses for the appearing of each character
# They have been measured directly from the real film scene.
secs1 = [0, 0.1500, 0.1625, 0.1500, 0.1625, 0.1500, # The last 3 times in secs1 are for the 3 dots (...)
            0.1625, 1.3500, 0.1200, 0.1250, 0.1200, # so you want *them* to always be the last 3.
            0.1250, 0.1250, 0.1625, 0.1575, 0.0625, # Insert your new times per character right *before* them!
            0.1250, 0.1250, 0.0625, 0.0875, 2.0625,         
            0.1250, 0.1250, 0.0625, 0.0875, 0.0995,         
            0.0925, 0.0625, 0.0625, 0.0675, 0.0625]         
    
secs2 = [0, 0.5325, 0.4700, 0.4000, 0.5800, 0.0950, 
            0.1350, 0.1075, 0.5275, 0.6225, 0.0080, 
            0.1200, 0.1475, 0.4500, 0.0080, 0.4275, 
            0.1275, 0.1425, 0.3550, 0.1475, 0.4500, 
            0.0080, 0.2275, 0.1450]
    
secs3 = [0, 0.1500, 0.1625, 0.1500, 0.1625, 0.1500, 
            0.1625, 1.0500, 0.1200, 0.1250, 0.1200, 
            0.1250, 0.1250, 0.0625, 0.1575, 0.0625,        
            0.1250, 0.1250, 0.0625, 0.0875, 0.0625,        
            1.1250, 0.1250, 0.0625, 0.0875, 0.0625,
            0.5250, 0.1250, 1.2625, 0.0875, 0.0625,        
            0.0875, 0.0875, 0.0875, 0.0875, 0.0875, 0.0875, 0.0625, 0.0625, 0.0625, 0.0625] 


system ('cls')

print(BOLDON + LIGHT_GREEN + CURSOROFF, end = '') 
print(_here, end = '')
x1 = 0
for i in msg1:
    sleep (secs1[x1]*delayFactor)
    print (msg1[x1], end='', flush=True)
    x1 += 1
sleep(13.03*remainFactor)   # 13.03 seconds measured from the real scene from film "The Matrix"
system ('cls')

print(_here, end = '')
x2 = 0
for i in msg2:
    sleep (secs2[x2]*delayFactor)
    print (msg2[x2], end='', flush=True)
    x2 += 1
sleep(12.54*remainFactor)   
system ('cls')



print(_here, end = '')
x3 = 0
for i in msg3:
    sleep (secs3[x3]*delayFactor)
    print (msg3[x3], end='', flush=True)
    x3 += 1
sleep(7.54*remainFactor)    # 7.54 seconds measured from the real scene from film "The Matrix"





fen = Tk() #creation fenetre tk
#centrage de la fenetre  tk 
largeur_fenetre = 700
hauteur_fenetre = 560
largeur_ecran = fen.winfo_screenwidth()
hauteur_ecran = fen.winfo_screenheight()
x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2
fen.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")


can = Canvas(fen, width=700, height=560, bg='black') #creation d'un canevas a fond blanc
can.pack(side='top', fill='both', expand='yes') # Le canevas est  emballé (pack) dans la fenêtre pour qu'il occupe tout l'espace disponible.
photo = PhotoImage(file=r"P:\8 - Sylvain PERSO\7 - Jobsrch\10 - New Job\Formation\FORMATION\2 - DATA SCIENCE INITIATION - Digitalcity\Exo PYTHON\01_DGCY_01_intro_python\Matrix\gif1.gif")
can.create_image(0,0,anchor='nw', image=photo, tag='photo')
 
ind = -1
def update(delay=90):
    global ind
    ind += 1
    if ind == 4: ind = 0
    print (ind)
    photo.configure(format="gif -index " + str(ind))
    fen.after(delay, update)
 
update()
fen.mainloop()


