label SC_CAVE:

scene bg black

show background meeting abyss entity:
    xzoom 1.5 yzoom 1.5

show abyss entity sprite 1 at top

voice "reached_temptation.mp3"
entity "Oh you have reached the abyss of temptation"
entity "..."
show abyss entity sprite hot at top
voice "sexy.mp3"
entity "sexy"

you "..."
show abyss entity sprite 1 at top

entity "Thou should'th be'th carefuleth around these partths" 
entity "hearsay hear thaeyat hearyeath beeth Paths mostth dangerous"

show background cave of eternal torment
show abyss entity sprite 1 at top

you "Why do you talk like that?"

entity "To thine Rhinght'th is the TÜV GEPRÜFTER GEHWEG and to thee leftht is the roadth known'n by ye old folkth as \"The devil's behind\""
entity "Would'th thouth liketh to enter thee pathee lefeth? or Rigththth?"

menu:

    "left":
        entity "Dust though trooly wish to enter the devils behind, it is a most tigth cavern!?"
        you "Please just stop talking like that"
        entity "Mine thesaurs iseth maysay excellentium, my dearest Bankmayer"
        you "Was that even a real world"
        entity "Neverthedevil, do you wishes to enter the devils behind now?"
        menu:         
            "Yes":
                entity "Thee should really beath EXRTAYTH..."
                you "STOP!!!"
                you "For the love of god just stop with this"
                you "I don't even recognize you anymore"
                entity "..."
                you "..."
                you "It's almost like there is an imposter among us..."
                
                show abyss entity sprite 5

                pause

                show abyss entity sprite 4
                
                pause
                
                "Frank offended the abyss entity so much she left."

                $ dead = True
                jump SC_CAVE_LEFT
            "No":
                show abyss entity sprite hot at top
                entity "I knew you weren't sexy enough"
                return
    "right":
        show abyss entity sprite 3
        entity "You are boring old man"
        you "rude"
        return

label SC_CAVE_LEFT:

show gameover animation cave diving 1 at top

pause 1

show gameover animation cave diving 2 at top

pause 1

show gameover animation cave diving 3 at top

pause 1

show gameover animation cave diving 4 at top

pause 1

show gameover cave diving

pause

"Frank Bankmayer has suffocated in the devil's behind, may he rest in peace..."


return