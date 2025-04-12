label SC_USB:

scene bg black

show background usb stick:
    xzoom 1.5 yzoom 1.5

show abyss entity sprite 1

entity "Welcome to the Abyss of Illusion."

entity "Be careful, many advetures were done in by thes treacherous lands."

you "You are not going to start speaking weridly again, are you?"

hide abyss entity sprite 1
show abyss entity sprite 2

entity "Arrr, what be you blubbering ybout landrat!?"

you "..."

entity "Aye, this ship is your's to sail."

hide abyss entity sprite 2

pause

"Frank looks around and sees a USB Stick"

you "It couldn't be"

show usb sprite at top

usb "Yes Frank, it's me, your Kundendaten USB Stick"

you "..."

you "You know, after losing you I realized something..."

usb "... yes?"

you "I realzied just how much you mean"

you "How much I, without any backup whatsoever, really rely on you for my Kundendaten"

usb "I didn't know you felt that way Frank"

you "Oh, Kundendaten USB Stick"

usb "Oh Frank"

you "I lo-"

you "!?"

you "IS THAT A NEW LAPTOP!?"

usb "HEY, hey Frank, focus, weren't you about to tell me something."

you "Yeah, but what was it?"

menu:
    "I love you":
        jump SC_USB_LOVE
    "I loath you":
        jump SC_USB_HATE
    "I long for you":
        jump SC_USB_LOVE
    "I loaned you, you are not my Kundendaten USB Stick":
        jump SC_USB_HATE
    "Some other word with I lo- that means something good idk...":
        jump SC_USB_LOVE
    "I lost you on purpose":
        jump SC_USB_HATE

label SC_USB_LOVE:

usb "Oh Frank, put me in..."

show game over usb stick animation 1

pause

show game over usb stick animation 2

pause

show game over usb stick animation 3

pause

show game over usb stick animation 4

pause

show game over usb stick animation 5

pause

show game over usb stick animation 6

pause

show game over usb stick animation 7

pause

$ dead = True

"Frank accidentally downlaoded a car."
"He has ruined his career"

return

label SC_USB_HATE:

usb "I understand Frank, it couldn't have worked between us anyway"
usb "I am sorry, my love"

you "Don't cry because it ended, ..."
you "laugh because it happened"

you "My USB Stick was blue anyways."


return