from psychopy import visual, core, event, clock
from psychopy.hardware import keyboard



#create a window
mywin = visual.Window(fullscr=True, color=(-1,-1,-1), colorSpace='rgb', allowGUI=True, monitor="testMonitor", units="pix")

#Create message
text = visual.TextBox2(win=mywin, text='Mire el cuadro blanco en pantalla', font='Arial', pos=[0,0], color=(1,1,1), letterHeight=50, units='pix', anchor='center')



#create visual stimuli
#square = visual.GratingStim(win=mywin, size=100, pos=[-633,334], sf=1) #Fix for every kind of window
square = visual.Rect(win=mywin, width=200, height=200, pos=[-633,334], fillColor=(1,1,1))


#create a keyboard component
kb = keyboard.Keyboard()



#draw the stimuli and update the window
while True: #this creates a never-ending loop
    text.setAutoDraw(False)  # Do not draw automatically
    text.draw() #Place text
    mywin.flip() 
    core.wait(3.0) #show text for 3 seconds

    #1: 1 second
    square.draw() #draw square
    mywin.flip() 
    core.wait(1.0) #show square for 1 second
    mywin.flip()  # flip without drawing
    core.wait(2.0) #Wait 2 seconds

    #1: 2 seconds
    square.draw() #draw square
    mywin.flip() 
    core.wait(2.0) #show square for 2 seconds
    mywin.flip()  # flip without drawing
    core.wait(2.0)

    #1: 0.5 seconds
    square.draw() #draw square
    mywin.flip() 
    core.wait(0.5) #show square for half a second
    mywin.flip()  # flip without drawing
    core.wait(2.0)

    
    #Start again  
        



    if len(kb.getKeys()) > 0:
        break
    event.clearEvents()

#cleanup
mywin.close()
core.quit()


