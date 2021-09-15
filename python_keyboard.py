import keyboard  # using module keyboard
import rtmidi
import time

##########
# Set Up #
##########

# midi value in Character Animator
mymidi_knob = 77
# time delay between key presses
mytimedelay = 0.02
# how much bigger/smaller next knob position
mupositionchangestep = 5
# set to True to fix in the middle
fix_middle = False

####################################################
####################################################

# this should be a reference to a loopmidi (number)
midiout = rtmidi.MidiOut()
midiout.open_port(4)

# middle position
currposition = 60

# infitite loop
while True:  
    try:  
        # pressed left?
        if keyboard.is_pressed('left arrow'):  # if key 'q' is pressed 
            #print('←')
            # step to turn wheel left
            currposition -= mupositionchangestep
            # cannot go below zero
            if currposition < 0:
                currposition = 0
            # send to character animator
            midiout.send_message([176, mymidi_knob, currposition])
            # wait a bit
            time.sleep(mytimedelay)
        elif keyboard.is_pressed('right arrow'):  # if key 'q' is pressed 
            #print('→')
            # step to turn wheel right
            currposition += mupositionchangestep
            # cannot go over 127
            if currposition > 127:
                currposition = 127
            # send to character animator
            midiout.send_message([176, mymidi_knob, currposition])
            time.sleep(mytimedelay)
        else:
            #print('↑')
            # for straight keep sending signal to wiggle the wheel
            if currposition > 60:
                currposition -= mupositionchangestep
            else:
                currposition += mupositionchangestep
            if fix_middle:
                if round(currposition,0) == 60:
                    currposition = 60
            midiout.send_message([176, mymidi_knob, currposition])
            time.sleep(mytimedelay)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

# close midi connection
midiout.close_port()