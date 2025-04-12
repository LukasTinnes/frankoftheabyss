label SC_AI:
    scene background meeting abyss entity:
        xzoom 1.43 yzoom 1.75
    show abyss entity sprite 1

    entity "Oh! We have reached the abyss of future."
    you "What do you mean future?"
    entity "In this part of the abyss, everyone loves the next new thing."
    entity "You could say, everything is cutting edge!"
    you "Don't you mean everything is edgy?"
    entity "No. I said cutting edge."
    you "The last cutting edge achievement in my line of work was Excel."
    entity "Okay Frank..."
    entity "Maybe you should take a look around and see that things have changed since 1985."
    you "Excel has been the best tool for my work for a long time now!"
    show abyss entity sprite 3
    entity "Yeah. Just like the USB stick containing all your Kundendaten!"
    entity "With NO FUCKING backup."
    you "If it helps with my work, I could look around before venturing on!"
    entity "Good!"
    show abyss entity sprite 2
    entity "See you in the next abyss!"

    #scene TODO

    define ai = Character("AI Demon")

    ai "Hey there! 👋 How are you doing today fellow demon? 😈"
    you "Ehm. Hello? Why are you talking weirdly like that?"
    ai "I am here to help you with anything and everything! 😁"
    ai "Please tell me what you are looking for and I will gladly help you get going! 🛫"
    you "Hmm... What should I ask you?"
    
    menu ai_auswahl:
        "Cutting Edge":
            you ""
            #block of code to run
        "Steuerberatung":
            you "Can you tell me something about Steuerberatung?"
            ai "Absolutely! Steuerberatung is an invaluable asset for the people! 👩‍👩‍👧‍👧"
            ai "Steuerberater help everyone with all things taxes!"
            ai "Without them, the people would really struggle with filing out their tax forms! 📜"
            ai "What exactly do you want to know about Steuerberatung?"
            menu tax_auswahl:
                "":
                    you ""
                "":
                    you ""
            #block of code to run
        

return