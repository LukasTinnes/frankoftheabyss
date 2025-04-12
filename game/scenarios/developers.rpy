label SC_DEVS:
    scene background developers:
        xzoom 1.43 yzoom 1.75
    show abyss entity sprite 1
    entity "The abyss of Zealots..."
    entity "It feels pretty cozy in here."
    show lukasmogus sprite at center
    define lukas = Character("Lukasmogus")
    lukas "Prepare for trouble!"
    show tobimogus sprite at left
    define tobi = Character("Tobimogus")
    tobi "And make it double!"
    show beltenmogus sprite at right
    define belten = Character("Beltenmogus")
    belten "And triple!"
    show timogus sprite at top
    define tim = Character("Timogus")
    tim "AirBnB"

    lukas "Do"
    tobi "You"
    belten "Want"
    tim "To"
    lukas "See"
    tobi "Something"
    belten "Fun?"

    menu epicepicnessepic:
        "Yes":
            scene bg black

            image gato:
                "el gato gif 1.png" 
                pause 0.2
                "el gato gif 2.png" 
                pause 0.2
                "el gato gif 3.png" 
                pause 0.2
                "el gato gif 2.png"
                pause 0.2
                repeat
            show gato at top
            pause
            "Wait... Where is the data corruption cat?"
            "It should not be touched at all cost!"
            scene game over developers:
                xzoom 1.43 yzoom 1.75
            "The developers have accidentally eradicated Frank."
            "We hope it was worth it."
            pause
            $dead=True
            return
        "Maybe later":
            lukas "It was great meeting you. Good luck with the final Boss. I'll implement the USB Kundendaten Backup next game. Promised!"
            tobi "I hope your freakish, abnormal obsession with eating blueberries gets cured some day."
            you "How do you know that?"
            tobi "I have created you, I thought it was funny."
            belten "How do you like your travelling partner?"
            you "hot"
            tim "C'est une bonbon parce que c'est plus bon que bon"
            belten "un! männlich schhhhh"
            lukas "Shuddup!"
            #block of code to run
        
return 