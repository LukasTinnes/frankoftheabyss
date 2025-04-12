label SC_BOSS:

scene bg black

show background final boss:
    xzoom 1.5 yzoom 1.5

show abyss entity sprite 1

entity "We have been through a lot haven't we"

you "I was, you just made dumb jokes and talked weird..."

you "and called me old!"

show abyss entity sprite 3

entity "whatever..."

show abyss entity sprite 2

entity "Anways, good luck Frank"

you "What is even coming next?"

you "where is my Kundendaten USB Stick?"

you "What was all of that?"

you "Why was my USB Stick thrown down here in the first place?"

pause

hide abyss entity sprite 2

you "and she's gone, great..."

you "now, what..."

show lucifer sprite at top

lucifer "I see, you met my daughter!"

you "I guess this is suposed to be a plot twist?"

lucifer "Did she behave well?"

you "Well..."

menu:
    "She dragged me through a whole bunch of uneccesary degrading trials":
        lucifer "Don't you see Frank? These trials were designed to help you become a better person."
        you "An uncontably infinite number people died on the train tracks"
        lucifer "Don't worry, those were syntheticy humans. They feel and think just like real humans, but they are all lab grown for the purpose of giving lessons."
        you "..."
        you "wow"
    "She was scared of the marriage counseller":
        lucifer "We are all scared of the mariage counseller"
        you "figures..."
    "She talks weird":
        lucifer "I apologize, it is the brain damage she received at child birth."
        you "oh..."
        you "... sorry"
        lucifer "Check your privilege next time"
    "She is the reason I am down here in the first place":
        lucifer "And how many lessons you have learned from that"
        you "An uncontably infinite number people died on the train tracks"
        lucifer "Don't worry, those were syntheticy humans. They feel and think just like real humans, but they are all lab grown for the purpose of giving lessons."
        you "..."
        you "wow"

hide lucifer sprite
show refi sprite at top

refi "hi"

you "Oh, hey it's the kid that summoned me in the last game!"

refi "I opened a restaurant now with the protagonist form the last game"

you "Wow, those math lessons really paid for themselves."

refi "We even had real artists paint some paintings, because we were inspired by you"

you "Impressive, I will definitely come by, once I retrieved my Kundendaten USB Stick"

hide refi sprite

show lucifer sprite at top

lucifer "Oh about that..."

you "...yes?"

lucifer "you are my Steuerberater, and I like you, want it back?"

menu:
    "Yes":
        lucifer "Ok, here you go"
        you "thanks"
        lucifer "Want to go to the restaurant of my son?"
        you "ehh, sounds good, my wife is drunk anyways"
        scene bg black
        show end:
            xzoom 1.5 yzoom 1.5
        "A good time was had by all at Revi's restaurant."
    "No":
        lucifer "What? What do you mean no?"
        lucifer "didn't you come all this way down here to get your Kundendaten back"
        you "Well no, do you really think I am stupid enpugh not to back up my Kundendaten?"
        you "This was all part of my sophisticated plan"
        lucifer "huh?"
        you "What I am really here for is..."
        menu:
            "To take control of this abyss":
                lucifer "Very well..."
                lucifer "YOU SHALL BE..."
                lucifer "STEUERBERATER OF THE ENTIRE ABYSS"
                you "My life's work, is complete!"    
            "To kill my Schwiegermutter":
                lucifer "I mean she was right there on the tracks"
                lucifer "I can route another trolley there, I guess"
                you "Thanks man"
                lucifer "Alright"
            "To divorce my wife":
                lucifer "Sorry mate, you need to speak to the counseller for that"
                you "... damn"
                you "that guy is scary"
                lucifer "true"
                show marriage counsellor of the abyss sprite
                counsellor "hello..."
                you "AHHHH"
                lucifer "AHHHH"
                counsellor "AHHHH"
                "AHHHHH"
            "... I just appreciate artistic expressions like this game":
                lucifer "You call this artistic expression?"
                you "Supporting the youth is important"
                lucifer "None of the developers are especially young you know"
                you "Art is timeless"
                lucifer "I guess."

"And thus the story of Frank draws to a close. What did we learn today?"
"..."
"Not sure either..."

scene bg black
show thx for playing:
    xzoom 1.5 yzoom 1.5
"Thank you for playing!"

pause

return