# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

"TRIGGER WARNING: THIS GAME CONTAINS SATANIC, EROTIC AND VIOLENT CONTENT"

define you = Character("Frank Bankmayer")
define entity = Character("Abyss Entity")

define bankmaier = Character("Frank Bankmaier")
define wife = Character("Astral Projection of Frank's Wife")
define counsellor = Character("Marriage Counsellor")

image frank:
    "walkcycle 1.png"
    pause 0.2
    "walkcycle 2.png"
    pause 0.2
    "walkcycle 3.png"
    pause 0.2
    repeat

define dead = False



# The game starts here.

label start:

    pause

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

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "Frank begins his journey to find the Kundendaten USB Stick"

    call SC_CAVE from _call_SC_CAVE
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "Frank survied his first encounter in the abyss, he marches on, bravely"

    call SC_DOPPEL from _call_SC_DOPPEL
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "With two encounters under his belt, Fank begins to grow confident, maybe he can do this. He charges ahead!"

    call SC_SCHWIEGER from _call_SC_SCHWIEGER
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "Half of all encounters are finished..."
    "Shit, was that a spoiler?"
    "Ahh, never mind, keep walking Franky"

    call SC_USB from _call_SC_USB
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "Frank rests to consume ISO Getränke."
    pause
    "Refreshed, Frank charges ahead"


    call SC_AI from _call_SC_AI
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "The Kundendaten USB draws near, Frank tastes the bytes as if he was eating"

    call SC_DEVS from _call_SC_DEVS
    if dead:
        return

    scene bg black    
    show background meeting abyss entity:
        xzoom 1.5 yzoom 1.5
    show frank at top
    "After all that time, after all those marriage counselors, Schwiegermütters, and cave diving accidents..."
    "Frank races to his final destination."


    return
