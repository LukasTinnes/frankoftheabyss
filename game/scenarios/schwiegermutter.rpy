label SC_SCHWIEGER:

    scene background meeting abyss entity:
        xzoom 1.43 yzoom 1.75
    show abyss entity sprite 2

    entity "Welcome to the abyss of ethics!"
    entity "This place is all about ethics and moral dilemmas."
    define schweiger = Character("Schwiegermutter of the abyss")
    show schwiegermutter sprite

    schweiger "FRANK? IS THAT YOU?!"
    schweiger "Get your lazy ass here right now!"
    schweiger "You lazy ass good for nothing!"
    show abyss entity sprite hot
    entity "Good fucking luck."
    entity "I am off now!"

    scene background trolley problem:
        xzoom 1.43 yzoom 1.75

    you "What even happened here?"
    you "Why was the lever pulled to save one person?"
    you "There are uncountably infinite people on the other track?!"
    you "Who would even save my Schwiegermutter?"
    schweiger "Shut up and get me out of here! There is another train coming."
    schweiger "Whatever you do. Do not pull that lever!"

    "The train is approaching fast. What should Frank do?"
    "He hesitates and takes a deep breath."

    schweiger "I also found this USB stick down here..."

    menu peter_maffay_epic_menu_not_really_peter_maffay_here:
        "Pull the Lever":
            "The train approaches and it approaches fast"
            schweiger "You better leave it Frank!"
            schweiger "You will never hear the end of it!"
            "Frank is sweating nervously."
            "Once and for all, he could finish his Schwiegermutter!"
            "He pulls the lever!"
            "The train arrives, barreling over the railway."
            "It charges in, ready to roll over his Schwiegermutter."
            "And then it stops."
            show marriage counsellor of the abyss sprite
            counsellor "Hello Frank! Just checking in how you are doing!"
            "The Counseller was conducting the train"
            counsellor "I see you tried killing your Schwiegermutter."
            counsellor "That's a great step! She really had it coming."
            counsellor "Say.... Have you seen a USB stick?"
            counsellor "I have dropped it somewhere around here."
            counsellor "I have backups in the cloud and all."
            counsellor "Who would be dumb enough to not backup his data?"
            counsellor "But that was a limited edition TCU USB stick."
            counsellor "Would not want to lose that!"
        "Leave it":
            "The train approaches and it approaches fast"
            schweiger "You better leave it Frank!"
            schweiger "You will never hear the end of it!"
            "Frank is sweating nervously."
            "Once and for all, he could finish his Schwiegermutter!"
            "Against his better judgement..."
            "..."
            "He does not pull the lever."
            "The train arrives, barreling over the railway."
            "It charges in, ready to roll over infinite dead people."
            "At the last second... desaster strikes!"
            scene game over trolley problem:
                xzoom 1.43 yzoom 1.75
            "The train derails and drops on Frank. Karma is a bitch?"
            pause 
            $dead=True
            return

        
    

return