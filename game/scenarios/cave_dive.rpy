label SC_CAVE:


scene background meeting abyss entity:
    xzoom 1.37 yzoom 1.37

show abyss entity sprite 1 at top

entity "Oh you have reached the abyss of temptation"
entity "..."
entity "sexy"

you "..."

entity "Thou should'th be'th carefuleth around these partths" 
entity "hearsay hear thaeyat hearyeath beeth Paths mostth dangerous"

you "Why do you talk like that?"

entity "To thine Rhinght'th is the TÜV GEPRÜFTER GEHWEG and to thee leftht is the roadth known'n by ye old folkth as \"The devil's behind\""
entity "Would'th thouth liketh to enter thee pathee lefeth? or Rigththth?"

menu:

    "left":
         entity "Go forth"
         $ dead = True
         jump SC_CAVE_LEFT
    "right":
         show abyss entity sprite 3
         entity "You are fucking boring old man"
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