import Tkinter as tk
import itertools as it

import pyglet
import pygame
pygame.init()
import os

SAMPLE_DIRECTORY = 'samples/'

sorted_keys = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?"

samples = sorted([ os.path.join(SAMPLE_DIRECTORY, f) for f in os.listdir(SAMPLE_DIRECTORY) if os.path.isfile(os.path.join(SAMPLE_DIRECTORY, f)) ])
connections = dict(
    zip(
        sorted_keys, 
        map(
            pygame.mixer.Sound, 
            samples
        )
    )
)

pygame.mixer.init(frequency=44100, buffer=512)

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
    
    c = event.char
    
    if(connections.has_key(c)):
        connections[c].play(loops=0, maxtime=0, fade_ms=0) 

root = tk.Tk()
print "Press a key (Escape key to exit):"
root.bind_all('<Key>', keypress)
root.mainloop()

