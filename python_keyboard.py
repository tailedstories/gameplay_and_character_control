import keyboard  # using module keyboard
import rtmidi
import time

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
            currposition -= 5
            # cannot go below zero
            if currposition < 0:
                currposition = 0
            # send to character animator
            midiout.send_message([176, 77, currposition])
            # wait a bit
            time.sleep(0.02)
        elif keyboard.is_pressed('right arrow'):  # if key 'q' is pressed 
            #print('→')
            # step to turn wheel right
            currposition += 5
            # cannot go over 127
            if currposition > 127:
                currposition = 127
            # send to character animator
            midiout.send_message([176, 77, currposition])
            time.sleep(0.02)
        else:
            #print('↑')
            # for straight keep sending signal to wiggle the wheel
            if currposition > 60:
                currposition -= 5
            else:
                currposition += 5
            midiout.send_message([176, 77, currposition])
            time.sleep(0.02)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

# close midi connection
midiout.close_port()