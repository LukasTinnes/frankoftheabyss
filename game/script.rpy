# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Frank Bankmayer")
define entity = Character("Abyss Entity")


# The game starts here.

label start:

    show frank 1:
        xzoom 1.37 yzoom 1.37

    pause

    show frank 2
    
    pause

    show frank 3
    
    pause

    show frank 4

    pause

    show frank 5
    
    pause

    show frank 6

    pause

    show frank 7
    
    pause
 
    show frank 8
    
    pause

    show frank 9
    
    pause

    show frank 10
    
    pause

    show frank 11
    
    pause

    show frank 12
    
    pause

    show frank 13
    
    pause

    show frank 14

    pause

    call SC_CAVE from _call_SC_CAVE

    entity "This is the first transition"

    call SC_DOPPEL from _call_SC_DOPPEL

    entity "This is the second transition"

    call SC_SCHWIEGER from _call_SC_SCHWIEGER

    entity "This is the third transition"

    call SC_USB from _call_SC_USB

    entity "This ist the fourth transition"

    call SC_AI from _call_SC_AI

    entity "This is the fifth transition"

    call SC_DEVS from _call_SC_DEVS

    entity "This is the last transition"

    return
