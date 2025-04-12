label SC_DOPPEL:

scene background doppelgaenger

show abyss entity sprite 1 at left
entity "This is the abyss of double sta..."
show marriage counsellor of the abyss sprite at right
counsellor "Hello, I am a marriage counsellor"
entity "Nah, you're on your own..."
hide abyss entity sprite 1

counsellor "Hello Frank I am your marriage councellor"
you "It's spelled \"counsellor\""
counsellor "Like I said, your marriage counseller"
you "That is..."
counsellor "Tonight, I invited you and you to have a chat with your wife"
you "what?"
show frank bankmeier sprite at topleft
bankmaier "Hello, I am Frank Bankmaier, a Steuerberater"
you "..."
counsellor "And here is your wife now..."
show wife hologram sprite at left
wife "Hi love"
you "uhh"
bankmaier "Hi honey"

counsellor "Tonight, I will help you decide which Frank is the better one to keep being married to"
bankmaier "I love you honey, I will win this in no time and then tere's dinner at Refi's"
you "huh? I don't want to do this!"
wife "I'll root for you boys!"

counsellor "Tonight's first question."
counsellor "Who is sexier? Your wife, or singer/song writer Peter Maffay?"

menu:
    "My Wife":
        counsellor "WRONG!"
        bankmaier "Pfft, idiot"
        wife "I can't belief, you would think that I am prettier"
        jump SC_DOPPEL_DEFEAT
    "Peter Maffay":
        counsellor "CORRECT!"
        bankmaier "Ha, you got lucky"
        wife "I already drank like 2 bottles of wine since you left"
        you "This is embarassing."

counsellor "And the next question!"
counsellor "Frank, a year ago your wife asked to have pancakes and you refused to make her some"
counsellor "..."

you "That's not a question"
counsellor "CORRECT"
bankmaier "Damn, you are better than I thought you would be"
wifer "*hic* I rweally wanded thousch pancakes"

counsellor "And the third question"
counsellor "What was your wife doing before you left the home"

menu:
    "Drinking Wine":
        counsellor "WRONG!"
        bankmaier "Did you see that honey, I won!"
        wife "*vomits*"
        jump SC_DOPPEL_DEFEAT
    "Playing mobile games":
        counsellor "WRONG!"
        bankmaier "Did you see that honey, I won!"
        wife "*vomits*"
        jump SC_DOPPEL_DEFEAT
    "Reading AI generated Memes":
        counsellor "Correct!"
        bankmaier "I can't beleif I lost to him"
        you "Did you see that, I won!"
        bankmayer "Not now honey, I am reading memes..."

return

label SC_DOPPEL_DEFEAT:
    show game over doppelgaenger
    "Frank was not able to win the affection of his wife, over his evil doppelganger."
    pause
    $ dead = True


