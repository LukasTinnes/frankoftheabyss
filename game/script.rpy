# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define you = Character("Frank Bankmayer")


# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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
