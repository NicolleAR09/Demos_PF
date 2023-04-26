from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import visual, core, event, sound
from psychopy.hardware import keyboard
import psychtoolbox as ptb



#create a window
mywin = visual.Window(fullscr=True, color=(-1,-1,-1), colorSpace='rgb', allowGUI=True, monitor="testMonitor", units="pix")

#Create message
text = visual.TextBox2(win=mywin, text='En unos segundos se escuchará un sonido', font='Arial', pos=[0,0], color=(1,1,1), letterHeight=50, units='pix', anchor='center')

#Create sound stimuli
theSound = sound.backend_ptb.SoundPTB('A', loops=-1)
theSound2 = sound.backend_ptb.SoundPTB('A', loops=-1)
theSound3 = sound.backend_ptb.SoundPTB('A', loops=-1)
#now = ptb.getSecs()


#create a keyboard component
kb = keyboard.Keyboard()



#draw the stimuli and update the window
while True: #this creates a never-ending loop
    text.setAutoDraw(False)  # Do not draw automatically
    text.draw() #Place text
    mywin.flip() 
    core.wait(2.0) #show text for 5 seconds

    #nextFlip = mywin.getFutureFlipTime(clock='ptb')
    #theSound.play(when=nextFlip) 
    theSound.play() 
    mywin.flip() 
    core.wait(3.0)
    
    theSound2.play() 
    mywin.flip() 
    core.wait(1.0)

    theSound3.play() 
    mywin.flip() 
    core.wait(2.0)


    #Start again  
        



    if len(kb.getKeys()) > 0:
        break
    event.clearEvents()

#cleanup
mywin.close()
core.quit()


