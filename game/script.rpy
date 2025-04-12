# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Frank Bankmayer")
define entity = Character("Entity")


# The game starts here.

label start:

    show frank 1:
        xzoom 1.3 yzoom 1.3

    pause 2

    show frank 2
    
    pause 2

    show frank 3
    
    pause 2

    show frank 4

    pause 2

    show frank 5
    
    pause 2

    show frank 6

    pause 2

    show frank 7
    
    pause 2
 
    show frank 8
    
    pause 2

    show frank 9
    
    pause 2

    show frank 10
    
    pause 2

    show frank 11
    
    pause 2

    show frank 12
    
    pause 2

    show frank 13
    
    pause 2

    show frank 14

    pause 2

    call SC_CAVE from _call_SC_CAVE

    call SC_DOPPEL from _call_SC_DOPPEL

    call SC_SCHWIEGER from _call_SC_SCHWIEGER

    call SC_USB from _call_SC_USB

    call SC_AI from _call_SC_AI

    call SC_DEVS from _call_SC_DEVS


    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
