from pygame import mixer
import sys


mixer.init()
ablum_name = input("Enter song name or path:")
mixer.music.load(ablum_name)
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print(""" 'P' for play , 'S' for stop, 'V' for volumne, 'E' for exit """)
    
    ch = input("['p','s','v','e'] >> ")
    if ch.lower() == "p":
        new = input('Enter song name or path:')
        mixer.music.load(new)
        mixer.music.play()
    elif ch.lower() == "s":
        mixer.music.pause()
    elif ch.lower() == 'v':
        vol = float(input("Enter a value from 0 to 1 in decimal to set volume: "))
        mixer.music.set_volume(vol)
    elif ch.lower() == "e":
        mixer.music.stop()
        sys.exit()
    else:
        pass