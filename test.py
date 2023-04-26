import psychtoolbox as ptb
from psychopy import sound, visual

mySound = sound.Sound('A')

win = visual.Window()
win.flip()
nextFlip = win.getFutureFlipTime(clock='ptb')

mySound.play(when=nextFlip)  # sync with screen refresh

